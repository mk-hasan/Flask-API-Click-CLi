from flask import Blueprint, jsonify, request
import json
import os
# define the blueprint
data_manipulate = Blueprint(name="data_manipulate", import_name=__name__)

# note: global variables can be accessed from view functions
json_url = os.path.join("data","data.json")

# add view function to the blueprint
@data_manipulate.route('/all', methods=['GET'])
def get_all_event():
    """
    ---
    get:
      description: get all event
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
      tags:
          - Data Manipulation
    """
    data_json = json.load(open(json_url))
    return jsonify(data_json['events'])

# add view function to the blueprint
@data_manipulate.route('/id/<id>', methods=['GET'])
def get_event_by_id(id):
    """
    ---
    get:
      description:  get event by id
      parameters:
        - name: id
          in: path
          description: ID of event to fetch
          required: true
          type: integer
          format: int64
      requestBody:
        required: true
        content:
            application/json:
                schema: InputSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
      tags:
          - Data Manipulation
    """
    data_json = json.load(open(json_url))
    data = data_json['events']
    id = request.view_args['id']
    output_data = [x for x in data if x['id']==int(id)]
    #render template is always looking in tempate folder 
    return jsonify(str(output_data))

# Endpoint for deleting a record
@data_manipulate.route("/remove/id/<id>", methods=["DELETE"])
def remove_event_by_id(id):
    """
    ---
    get:
      description: remove event by id
      parameters:
        - name: id
          in: path
          description: ID of event to delete
          required: true
          type: integer
          format: int64
      requestBody:
        required: true
        content:
            application/json:
                schema: InputSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
      tags:
          - Data Manipulation
    """
    data_json = json.load(open(json_url))
    data = data_json['events']
    id = request.view_args['id']
    output_data = [x for x in data if x['id']!=int(id)]
    final_data = {'events':output_data}
    with open(json_url, 'w') as data_file:
        data = json.dump(final_data, data_file)
    return jsonify(output_data)

@data_manipulate.route("/add", methods=["POST"])
def add_event():
    """
    ---
    get:
      description:  add a new event
      requestBody:
        required: true
        content:
            application/json:
                schema: InputSchemaJson
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: InputSchemaJson
              schema: OutputSchema
      tags:
          - Data Manipulation
    """

    year = request.args.get('year')
    #case sensitive, so be careful!
    id = request.args.get('ID')
    category = request.args.get('category')
    event = request.args.get('event')
    event_yr= { "year":year,
                "id":int(id),
                "event_category":category,
                "event":event
                }
    with open(json_url,"r+") as file:
        data_json = json.load(file)
        data_json["events"].append(event_yr)
        file.seek(0)
        json.dump(data_json, file, indent =1 )
    
    #Adding text
    text_success = "Data successfully added: " + str(event_yr)
    return text_success
