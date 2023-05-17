from app import db
from model.users import Users


class UserRepository(db.Model):
    __tablename__ = "users"

    def get_by_id(id):
        data = Users.query.filter_by(id=id, deleted_at=None).first()
        return data

    def get_by_email(email):
        data = Users.query.filter_by(email=email).first()
        return data
    
    def get_by_username(username):
        data = Users.query.filter_by(username=username).first()
        return data