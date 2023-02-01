# crowdsec-yaml-schema

## Yaml schema

This repository provides three yaml schema files that may be used to
check parsers/scenarios/postoverflows/collection yaml file.


## What's the plan

One has to use
https://github.com/redhat-developer/yaml-language-server as a lsp
server. This is included basically in all yaml package plugin proposed
with most common editors.

The lsp server has to know the schema it has to apply to each yaml
file. For example if one edits github ci workflow files, the lsp
server will recognize the file and apply its schema by leveraging the
path of the filesystem. The information the lsp server is using is
stored on https://www.schemastore.org/json/. It seems easy to add ours
there, but I want the schemas thoroughly tested before proceeding.

## How to test it

For now, we can indicate to the lsp server how to apply the schema by
adding a line on top on the parsed yaml file.

`# yaml-language-server: $schema=https://raw.githubusercontent.com/crowdsecurity/yaml-schemas/main/parser_schema.yaml`

As it is undserstood by the lsp server, it will be working in most
common editors.

## What's left to be done

* Testing this as much as possible and report issues in this repository
* Decide if we add yaml schema for crowdsec configuration file
