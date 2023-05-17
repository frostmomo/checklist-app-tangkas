from flask import request, jsonify
from flask import Blueprint

from model.checklist_items import ChecklistItems
from common.responses import BaseResponse

from flask_jwt_extended import *
from datetime import datetime as timestamp

current_time = timestamp.now()

checklist_item_api = Blueprint('checklist_item_api', __name__)

# 1.3  === Get Checklist Item API === 
@checklist_item_api.route("/checklist/<int:id>/item", methods=["GET"])
def get_all_checklist_item_by_checklist_id():
    json = request.json
    try:
        checklist_item = (ChecklistItems.query.filter_by(name=json.get("username")).first())
        return checklist_item
    
    except Exception as error:
        return error

@checklist_item_api.route("/checklist/<int:id>/item", methods=["POST"])
def create_checklist_item_by_checklist_id():
    try:
        return None
    
    except Exception as error:
        return error

@checklist_item_api.route("/checklist/<int:id>/item/<int:item_id>", methods=["GET"])
def get_checklist_item_in_checklist_by_checklist_id():
    try:
        return None
    
    except Exception as error:
        return error

@checklist_item_api.route("/checklist", methods=["PUT"])
def get_all_checklist():
    try:
        return None
    
    except Exception as error:
        return error

@checklist_item_api.route("/checklist", methods=["DELETE"])
def create_checklist():
    try:
        return None
    
    except Exception as error:
        return error

@checklist_item_api.route("/checklist/<int:id>", methods=["PUT"])
def delete_checklist():
    try:
        return None
    
    except Exception as error:
        return error
