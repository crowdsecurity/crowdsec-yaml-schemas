#!/usr/bin/env python3
from __future__ import annotations
from models.pattern_syntax import PatternSyntax
from models.statics import Statics
from models.grok import Grok
from models.stash import Stash
from pydantic import BaseModel, Field
from typing import List, Optional


class ChildrenNodes(BaseModel):
    onsuccess: Optional[str] = Field(
        None,
        pattern=r"^next_stage$",
        description="If node is successful and onsuccess equals next_stage, event is moved to the next stage",
    )

    debug: Optional[bool] = Field(
        None, description="If true, enables the debug. Default is false."
    )
    filter: Optional[str] = Field(
        None,
        description="filter must be a valid expr expression that will be evaluated\nagainst the event.  If filter evaluation returns true or is\nabsent, node will be processed.  If filter returns false or a\nnon-boolean, node won't be processed.\n",
    )
    pattern_syntax: Optional[PatternSyntax] = None
    grok: Optional[Grok] = None
    stash: Optional[Stash] = None
    statics: Optional[Statics] = None
    nodes: Optional[List[ChildrenNodes]] = Field(
        None,
        description="nodes is a list of parser nodes, allowing you to build\ntrees. Each subnode must be valid, and if any of the subnodes\nsucceed, the whole node is considered successful.\n",
    )
