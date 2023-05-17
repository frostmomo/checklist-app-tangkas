from app import db
import json

from flask import request, jsonify
from flask import Blueprint

from model.checklists import Checklists
from repository.checklist_repository import ChecklistsRepository
from common.responses import BaseResponse

from flask_jwt_extended import *
from datetime import datetime as timestamp

current_time = timestamp.now()

checklist_api = Blueprint('checklist_api', __name__)

# 1.2  === Get Checklist API === 
@checklist_api.route("/checklist", methods=["GET"])
@jwt_required()
def get_all_checklist():
    try:
        data = ChecklistsRepository.get_all_checklist()
        
        return (
                jsonify(
                    BaseResponse(
                        [e.serialize() for e in data] if data is not None else None,
                        "Checklist Successfully Showed",
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


@checklist_api.route("/checklist", methods=["POST"])
@jwt_required()
def create_checklist():
    json = request.json
    try:
        user_auth = get_jwt_identity()

        added_by = user_auth['username']
        name = json.get("name")

        if name is None or name == "":
            return jsonify(
                {"message": "Name is Required", "status": 400}
            ),400
        
        checklist = Checklists(
            name=name,
            created_at=current_time,
            updated_at=current_time,
            deleted_at=None
        )

        db.session.add(checklist)
        db.session.commit()

        return jsonify(
            {
                "message": "Checklist Added by " + added_by,
                "status": 200,
                "data": {
                    "name": name,
                }
            }
        ),200
    
    except Exception as e:
        response = BaseResponse(None, str(e), 0, 0, 0, False)
        return jsonify(response.serialize())
    
@checklist_api.route("/checklist/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_checklist(id):

    if id is None or id == "":
        return jsonify(
            {"message":"ID is Required", "status":400}
        ),400

    try:
        data = ChecklistsRepository.get_by_id(id)

        if data is None or data == "":
            return jsonify(
                {"message": "Checklist is not Found", "status": 400}
            ),400
        
        data.deleted_at = current_time
        db.session.commit()

        return (
            jsonify(
                BaseResponse(
                    "{}".format(data.id),
                    "Checklist Successfully Soft Deleted",
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
