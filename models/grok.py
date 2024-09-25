#!/usr/bin/env python3

from typing import Optional
from pydantic import BaseModel, Field, Extra
from models.statics import Statics


class GrokItem(BaseModel):
    name: Optional[str] = None
    pattern: Optional[str] = None
    apply_on: Optional[str] = None
    expression: Optional[str] = None
    statics: Optional[Statics] = None

    model_config = {
        "extra": "forbid",
    }


class Grok(BaseModel):
    grok: Optional[GrokItem]
