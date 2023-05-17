import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from common.responses import BaseResponse
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
app.config.from_pyfile('config.py')

jwt = JWTManager(app)
CORS(app)
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app=app, db=db)

from route.auth_route import auth_api
from route.checklist_route import checklist_api
from route.checklist_item_route import checklist_item_api

@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    response = BaseResponse(None, "Token Expired", 0, 0, 0, False)
    return jsonify(response.serialize()), 401

@jwt.unauthorized_loader
def my_unauthorize_callback(jwt_header):
    response = BaseResponse(None, "Unauthorized", 0, 0, 0, False)
    return jsonify(response.serialize()), 401

def method_not_allowed_exception(e):
    response = BaseResponse(None, "Method not Allowed", 0, 0, 0, False)
    return jsonify(response.serialize()), 405

def notfound_exception(e):
    response = BaseResponse(None, "Endpoint Not Found", 0, 0, 0, False)
    return jsonify(response.serialize()), 404

@app.errorhandler(Exception)
def handle_exception(e):
    res = BaseResponse(None, str(e), 0, 0, 0, False).serialize()
    return jsonify(res), 500


app.register_error_handler(404, notfound_exception)
app.register_error_handler(405, method_not_allowed_exception)

app.register_blueprint(auth_api)
app.register_blueprint(checklist_api)
app.register_blueprint(checklist_item_api)


if __name__ == '__main__':

    app.run()


