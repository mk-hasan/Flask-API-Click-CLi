#load libraries
from flask import Flask, jsonify
import sys
from src.blueprints.swagger import swagger_ui_blueprint, SWAGGER_URL

# load modules
from src.blueprints.data_manipulate import data_manipulate
from src.api_spec import spec
# init Flask app
app = Flask(__name__)

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(data_manipulate, url_prefix="/gymondoapi/v1/data")
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)



with app.test_request_context():
    # register all swagger documented functions here
    for fn_name in app.view_functions:
        if fn_name == 'static':
            continue
        print(f"Loading swagger docs for function: {fn_name}")
        view_fn = app.view_functions[fn_name]
        spec.path(view=view_fn)

@app.route("/gymondoapi/swagger.json")
def create_swagger_spec():
    return jsonify(spec.to_dict())