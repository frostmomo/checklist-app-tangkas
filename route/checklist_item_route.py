from app import db

from flask import request, jsonify
from flask import Blueprint

from model.checklist_items import ChecklistItems

from repository.checklist_repository import ChecklistsRepository
from repository.checklist_item_repository import ChecklistItemRepository
from common.responses import BaseResponse
 
from flask_jwt_extended import *
from datetime import datetime as timestamp

current_time = timestamp.now()
 
checklist_item_api = Blueprint('checklist_item_api', __name__)

# 1.3  === Get Checklist Item API === 
@checklist_item_api.route("/checklist/<int:id>/item", methods=["GET"])
@jwt_required()
def get_all_checklist_item_by_checklist_id(id):
    
    try:
        data = ChecklistItemRepository.get_all_by_checklist_id(id)

        return (
                jsonify(
                    BaseResponse(
                        [e.serialize() for e in data] if data is not None else None,
                        "Checklist Items Successfully Showed",
                        1,
                        1,
                        len(data) if data is not None else None,
                        True,
                    ).serialize()
                ),
                200,
    )
    
    except Exception as e:
        response = BaseResponse(None, str(e), 0, 0, 0, False)
        return jsonify(response.serialize())

@checklist_item_api.route("/checklist/<int:id>/item", methods=["POST"])
@jwt_required()
def create_checklist_item_in_checklist(id):
    user_auth = get_jwt_identity()

    added_by = user_auth['username']
    
    json = request.json

    if id is None or id =="":
        return jsonify(
            {"message": "ID is Required", "status": 400}
        ),400
    
    checklist = ChecklistsRepository.get_by_id(id)
    if checklist is None or checklist == "":
        return jsonify(
            {"message": "Checklist not found is Required", "status": 400}
        ),400
    
    itemName = json.get("itemName")
    if itemName is None or itemName == "":
        return jsonify(
            {"message": "Item Name is Required", "status": 400}
        ),400

    try:
        checklist_items = ChecklistItems(
            name=itemName,
            checklist_id=checklist.id,
            created_at=current_time,
            updated_at=current_time,
            deleted_at=None
        )

        db.session.add(checklist_items)
        db.session.commit()

        return jsonify(
            {
                "message": "Checklist Added by " + added_by,
                "status": 200,
                "data": {
                    "item name": itemName,
                }
            }
        ),200
    
    except Exception as e:
        response = BaseResponse(None, str(e), 0, 0, 0, False)
        return jsonify(response.serialize())

@checklist_item_api.route("/checklist/<int:id>/item/<int:checklist_id>", methods=["GET"])
@jwt_required()
def get_checklist_item_in_checklist_by_checklist_id(id,checklist_id):

    if id is None or id =="":
        return jsonify(
            {"message": "ID is Required", "status": 400}
        ),400
    
    if checklist_id is None or checklist_id =="":
        return jsonify(
            {"message": "Checklist ID is Required", "status": 400}
        ),400

    try:
        data = ChecklistItemRepository.get_by_checklist_id(id,checklist_id)

        if data is None or data == "":
            return jsonify(
                {"message": "Checklist Item is not Found", "status": 400}
            ),400

        return (
            jsonify(
                BaseResponse(
                    data.serialize() if data is not None else None,
                    "Checklist Item Successfully Showed",
                    1,
                    1,
                    1,
                    True,
                ).serialize()
            ),
            200,
        )
    
    except Exception as e:
        response = BaseResponse(None, str(e), 0, 0, 0, False)
        return jsonify(response.serialize())

@checklist_item_api.route("/checklist/<int:id>/item/<int:checklist_id>", methods=["PUT"])
@jwt_required()
def update_status_checklist_item_by_checklist_item_id(id, checklist_id):

    json = request.json

    status = json.get("status")

    if id is None or id =="":
        return jsonify(
            {"message": "ID is Required", "status": 400}
        ),400
    
    if checklist_id is None or checklist_id =="":
        return jsonify(
            {"message": "Checklist ID is Required", "status": 400}
        ),400

    try:
        data = ChecklistItemRepository.get_by_checklist_id(id,checklist_id)

        if data is None or data == "":
            return jsonify(
                {"message": "Checklist Item is not Found", "status": 400}
            ),400
        
        data.status = status
        data.updated_at = current_time
        db.session.commit()

        return (
            jsonify(
                BaseResponse(
                    data.serialize() if data is not None else None,
                    "Checklist Item Status Successfully Updated",
                    1,
                    1,
                    1,
                    True,
                ).serialize()
            ),
            200,
        )
    
    except Exception as e:
        response = BaseResponse(None, str(e), 0, 0, 0, False)
        return jsonify(response.serialize())

@checklist_item_api.route("/checklist/<int:id>/item/<int:checklist_id>", methods=["DELETE"])
@jwt_required()
def delete_item_by_checklist_item_id(id, checklist_id):

    if id is None or id =="":
        return jsonify(
            {"message": "ID is Required", "status": 400}
        ),400
    
    if checklist_id is None or checklist_id =="":
        return jsonify(
            {"message": "Checklist ID is Required", "status": 400}
        ),400

    try:
        data = ChecklistItemRepository.get_by_checklist_id(id,checklist_id)

        if data is None or data == "":
            return jsonify(
                {"message": "Checklist Item is not Found", "status": 400}
            ),400
        
        data.updated_at = current_time
        data.deleted_at = current_time
        db.session.commit()

        return (
            jsonify(
                BaseResponse(
                    "{}".format(data.id),
                    "Checklist item Successfully Soft Deleted",
                    0,
                    0,
                    0,
                    True,
                ).serialize()
            ),
            200,
        )
    
    except Exception as e:
        response = BaseResponse(None, str(e), 0, 0, 0, False)
        return jsonify(response.serialize())

@checklist_item_api.route("/checklist/<int:id>/item/rename/<int:checklist_id>", methods=["PUT"])
@jwt_required()
def rename_item_by_checklist_item_id(id,checklist_id):

    json = request.json

    name = json.get("itemName")

    if id is None or id =="":
        return jsonify(
            {"message": "ID is Required", "status": 400}
        ),400
    
    if checklist_id is None or checklist_id =="":
        return jsonify(
            {"message": "Checklist ID is Required", "status": 400}
        ),400

    try:
        data = ChecklistItemRepository.get_by_checklist_id(id,checklist_id)

        if data is None or data == "":
            return jsonify(
                {"message": "Checklist Item is not Found", "status": 400}
            ),400
        
        data.name = name
        data.updated_at = current_time
        db.session.commit()

        return (
            jsonify(
                BaseResponse(
                    data.serialize() if data is not None else None,
                    "Checklist Item Name Successfully Updated",
                    1,
                    1,
                    1,
                    True,
                ).serialize()
            ),
            200,
        )
    
    except Exception as e:
        response = BaseResponse(None, str(e), 0, 0, 0, False)
        return jsonify(response.serialize())
