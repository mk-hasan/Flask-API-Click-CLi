"""OpenAPI v3 Specification"""

# apispec via OpenAPI
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

# Create an APISpec
spec = APISpec(
    title="My App",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# Define schemas
class InputSchema(Schema):
    number = fields.Int(description="An integer.", required=True)

class OutputSchema(Schema):
    msg = fields.String(description="A message.", required=True)

class InputSchemaJson(Schema):
    json_msg = fields.String(description=str({
   "event": "Outbreak",
   "event_category": "Dengue",
   "id": 8,
   "year": "2029"
  }) , required=True)

# register schemas with spec
spec.components.schema("Input", schema=InputSchema)
spec.components.schema("InputJson", schema=InputSchemaJson)
spec.components.schema("Output", schema=OutputSchema)

# add swagger tags that are used for endpoint annotation
tags = [
            {'name': 'Data Manipulation',
             'description': 'For testing the API.'
            }
       ]

for tag in tags:
    print(f"Adding tag: {tag['name']}")
    spec.tag(tag)