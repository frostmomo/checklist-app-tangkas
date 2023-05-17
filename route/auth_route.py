from app import db

from flask import request, jsonify
from flask import Blueprint

from model.users import Users
from repository.user_repository import UserRepository
from common.responses import BaseResponse

from flask_jwt_extended import *
import datetime
from datetime import datetime as timestamp

current_time = timestamp.now()

auth_api = Blueprint('auth_api', __name__)

# 1.3  === Get User API === 
@auth_api.route("/register", methods=["POST"])
def register():
    json = request.json
    try:
        email = json.get("email")
        username = json.get("username")
        password = json.get("password")

        if email is None or email == "":
            return jsonify(
                {"message": "Email is Required", "status": 400}
            ),400
        
        if username is None or username == "":
            return jsonify(
                {"message": "Username is Required", "status": 400}
            ),400
        
        if password is None or password == "":
            return jsonify(
                {"message": "Password is Required", "status": 400}
            ),400
        

        user = Users(
            username=username,
            email=email,
            password=password,
            created_at=current_time,
            updated_at=current_time,
            deleted_at=None
        )

        db.session.add(user)
        user.set_password(password)

        db.session.commit()

        return jsonify(
            {
                "message": "User Registered Successfully",
                "status": 200,
                "data": {
                    "username": username,
                    "email": email
                }
            }
        ),200
    
    except Exception as e:
        response = BaseResponse(None, str(e), 0, 0, 0, False)
        return jsonify(response.serialize())

@auth_api.route("/login", methods=["POST"])
def login():
    json = request.json
    try:

        username = json.get("username")
        password = json.get("password")

        if username is None or password is None:
            return jsonify(
                {"message": "Required Credentials", "status": 400}
            ),400

        user = UserRepository.get_by_username(username)
        if not user or user is None:
            return jsonify({"message": "Credentials not found", "status": 400}),400
        
        if not user.check_password(json.get("password")):
            return jsonify({"message": "Wrong password", "status": 400}),400
        
        data = {
            "id": str(user.id),
            "email": user.email,
            "username": user.username
        }
        
        expires = datetime.timedelta(days=1)
        expires_refresh = datetime.timedelta(days=3)
        access_token = create_access_token(data, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
        
        return jsonify(
            {
                "message": "Login successfully",
                "status": 200,
                "data": {
                    "token_access": access_token,
                    "token_refresh": refresh_token,
                    "expire": str(expires),
                    "expire_refresh_token": str(expires_refresh),
                }
            }
        ),200
    
    except Exception as e:
        response = BaseResponse(None, str(e), 0, 0, 0, False)
        return jsonify(response.serialize())
