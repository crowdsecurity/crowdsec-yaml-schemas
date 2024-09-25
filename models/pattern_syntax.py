#!/usr/bin/env python3

from pydantic import BaseModel, Field, validator
from typing import Dict
import re


class PatternSyntax(BaseModel):
    pattern_syntax: Dict[str, str] = Field(
        ...,
        description="pattern_syntax allows user to define named capture group "
        "expressions for future use in grok patterns. Regexp must be a valid RE2 expression.",
    )

    @validator("pattern_syntax", pre=True)
    def check_key_constraint(cls, values):
        pattern = r"^[A-Z][A-Z0-9_v]*$"
        for key in values.get("pattern_syntax", {}).keys():
            if not re.match(pattern, key):
                raise ValueError(f"Key '{key}' does not match pattern '{pattern}'")

    class Config:
        json_schema_extra = {
            "properties": {
                "pattern_syntax": {
                    "patternProperties": {
                        "^[A-Z][A-Z0-9_v]*$": {"type": "string"},
                    },
                }
            }
        }
