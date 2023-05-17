import datetime
from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    
    created_at = db.Column(db.TIMESTAMP(), nullable=True, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.TIMESTAMP(), nullable=True, default=datetime.datetime.utcnow())
    deleted_at = db.Column(db.TIMESTAMP(), nullable=True)
    
    def __init__(
        self,
        username,
        email,
        password,
        deleted_at,
        created_at,
        updated_at,
    ):
        self.username = username
        self.email = email
        self.password = password
        self.deleted_at = deleted_at
        self.created_at = created_at
        self.updated_at = updated_at

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }