import json
import logging
import os

from elasticapm.contrib.flask import ElasticAPM
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from .views import healthcheck, postcode


app = Flask(__name__)
apm = ElasticAPM(app, logging=logging.ERROR)

SWAGGER_URL = '/api/docs' # URL for exposing Swagger UI
API_URL = 'http://localhost:8080/file://docs/swagger.json' 

# Call factory function to create our blueprint
swagger_file_dir = os.path.abspath('./docs/api.json')
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'spec': json.load(open(swagger_file_dir))},
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

app.add_url_rule('/healthcheck', view_func=healthcheck, methods=['GET'])
app.add_url_rule('/v1/postcode', view_func=postcode, methods=['GET'])
