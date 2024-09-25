#!/usr/bin/env python3

from typing import List, Optional
from pydantic import Field, BaseModel


class Static(BaseModel):
    meta: Optional[str] = None
    parsed: Optional[str] = None
    enriched: Optional[str] = None
    target: Optional[str] = None
    value: Optional[str] = None
    expression: Optional[str] = None
    method: Optional[str] = None

    model_config = {
        "extra": "forbid",
    }


class Statics(BaseModel):
    statics: List[Static] = Field(
        ...,
        description="Statics is a list of directives that will be evaluated when the\nnode is considered successful. Each entry of the list is\ncomposed of a target (where to write) and a source (what data to\nwrite).\n",
    )
