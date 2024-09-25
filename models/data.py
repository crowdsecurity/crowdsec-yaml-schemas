#!/usr/bin/env python3

from typing import List, Optional
from pydantic import BaseModel, Field


class DataItem(BaseModel):
    source_url: Optional[str] = Field(None, description="url to download file from")
    dest_file: Optional[str] = Field(
        None, description="destination to store the downloaded file to"
    )
    type: Optional[str] = Field(
        description="The type is mandatory if you want to evaluate the data"
        "inthe file, and should be regex for valid (re2) regular expression per"
        "line or string for string per line. The regexps will be compiled, the"
        "strings will be loaded intoa list and both will be kept in memory."
        "Without specifyinga type, the file will be downloaded and stored as file"
        "and not in memory.",
        pattern=r"^(string|regexp)$",
    )

    strategy: Optional[str] = Field(
        None,
        description="Strategy for cache behavior. See https://pkg.go.dev/github.com/bluele/gcache",
        pattern=r"^(LRU|LFU|ARC)$",
    )

    size: Optional[int] = Field(None, description="Maximum size of the cache")
    ttl: Optional[str] = Field(
        pattern=r"^([0-9]+(\.[0-9]+)*d)?([0-9]+(\.[0-9]+)*h)?([0-9]+(\.[0-9]+)*m)?([0-9]+(\.[0-9]+)*s)?([0-9]+(\.[0-9]+)*ms)?([0-9]+(\.[0-9]+)*(us|µs))?([0-9]+(\.[0-9]+)*ns)?$",
        description="Duration after which cache elements expire")



class Data(BaseModel):
    data: List[DataItem] = Field(
        ...,
        description="data allows user to specify an external source of data. This "
        "section is only relevant when cscli is used to install parser "
        "from hub, as it will download the source_url and store it to "
        "dest_file. When the parser is not installed from the hub,"
        "CrowdSec won't download the URL, but the file must exist for the "
        "parser to be loaded correctly.",
    )
