import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from langchain.output_parsers import ResponseSchema, StructuredOutputParser

name_schema = ResponseSchema(name="name", description="name of the furniture product")
description_schema = ResponseSchema(name="description", description="description of the furniture product")
ad_schema = ResponseSchema(name="ad", description="short punchy new ads of the furniture product")

response_schemas = [name_schema, description_schema, ad_schema]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()