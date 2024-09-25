#!/usr/bin/env python3

from typing import List, Optional, ClassVar
from pydantic import BaseModel, Field


class StashItem(BaseModel):
    description: ClassVar[str] = (
        "The stash section allows a parser to capture data, that can \
    be later accessed/populated via GetFromStash and SetInStash expr \
    helpers. Each list item defines a capture directive that is stored in a \
    separate cache (string:string), with its own maximum size, eviction \
    rules etc.",
    )
    name: str = Field(
        description="The name of the stash. Distinct parsers can manipulate the same cache",
    )
    key: str = Field(
        description="The expression that defines the string that will be used as a key",
    )
    value: str = Field(
        description="The expression that defines the string that will be used as a key",
    )
    ttl: Optional[str] = (
        Field(
            None,
            pattern=r"^([0-9]+(\.[0-9]+)*d)?([0-9]+(\.[0-9]+)*h)?([0-9]+(\.[0-9]+)*m)?([0-9]+(\.[0-9]+)*s)?([0-9]+(\.[0-9]+)*ms)?([0-9]+(\.[0-9]+)*(us|µs))?([0-9]+(\.[0-9]+)*ns)?$",
            description="The time to leave of items. Default strategy is LRU.",
        ),
    )
    size: Optional[int] = Field(None, description="The maximum size of the cache")
    strategy: Optional[str] = Field(
        None,
        pattern=r"^(LFU|LRU|ARC)$",
        description="The caching strategy to be used : LFU, LRU or ARC (see gcache doc for details). Defaults to LRU.\n",
    )


class Stash(BaseModel):
    stash: List[StashItem] = Field(
        ...,
        description="The stash section "
        "allows a parser to capture data, that can be later accessed/populated "
        "via GetFromStash and SetInStash exprhelpers. Each list item defines a"
        "capture directive that isstored in a separate cache (string:string),"
        "with its own maximumsize, eviction rules etc.",
    )
