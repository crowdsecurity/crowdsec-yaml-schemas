#!/usr/bin/env python3

from typing import Dict, Any, List, Optional, Union
from pydantic import BaseModel, Field, confloat
from models.children_nodes import ChildrenNodes
from models.pattern_syntax import PatternSyntax
from models.statics import Statics
from models.grok import Grok
from models.stash import Stash
from models.data import Data


class ParserType1(BaseModel):

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
        description="filter must be a valid expr expression that will be evaluated"
        "against the event.  If filter evaluation returns true or is absent, node "
        "will be processed.  If filter returns false or a"
        "non-boolean, node won't be processed.",
    )
    description: Optional[str] = Field(
        None, description="description of the parser usage"
    )
    pattern_syntax: Optional[PatternSyntax] = None
    name: str = Field(
        ...,
        description="The mandatory name of the node. If not present, node will be"
        "skipped at runtime. It is used for example in debug log to help"
        "you track things.",
    )
    grok: Optional[Grok] = None
    stash: Optional[Stash] = None
    statics: Optional[Statics] = None
    data: Optional[Data] = None
    format: Optional[float] = Field(
        None,
        ge=1.0,
        description="Non mandatory format version for the parser. configuration "
        "file. New features, may not be understood by old crowdsec version, "
        "filling this correctly ensures that crowdsec supports "
        "all the required parser features.",
    )
    nodes: Optional[List[ChildrenNodes]] = Field(
        None,
        description="nodes is a list of parser nodes, allowing you to build trees. "
        "Each subnode must be valid, and if any of the subnodes succeed, the whole "
        "node is considered successful.",
    )
    whitelist: Optional[Dict[str, Any]] = None

    model_config = {
        "extra": "forbid",
    }


class ParserType2(BaseModel):

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
        description="filter must be a valid expr expression that will be evaluated"
        "against the event.  If filter evaluation returns true or is absent, node "
        "will be processed.  If filter returns false or a non-boolean, node won't "
        "be processed.",
    )
    description: Optional[str] = Field(
        None, description="description of the parser usage"
    )
    pattern_syntax: Optional[PatternSyntax] = None
    name: str = Field(
        ...,
        description="The mandatory name of the node. If not present, node will be"
        "skipped at runtime. It is used for example in debug log to help you track "
        "things.",
    )
    grok: Optional[Grok] = None
    stash: Optional[Stash] = None
    statics: Optional[Statics] = None
    data: Optional[Data] = None
    format: Optional[str] = Field(
        None,
        ge=1.0,
        description="Non mandatory format version for the parser. configuration file. "
        "New features, may not be understood by old crowdsec version, filling this "
        "correctly ensures that crowdsec supports\nall the required parser features.",
    )
    nodes: Optional[List[ChildrenNodes]] = Field(
        None,
        description="nodes is a list of parser nodes, allowing you to build trees. Each "
        "subnode must be valid, and if any of the subnodes succeed, the whole node is "
        "considered successful.",
    )
    whitelist: Dict[str, Any]
    model_config = {
        "extra": "forbid",
    }


class Parser(BaseModel):
    parser: Union[ParserType1, ParserType2] = Field(..., title="CrowdSec Parser")
    model_config = {
        "extra": "forbid",
    }
