import datetime
from app import db
from sqlalchemy import ForeignKey

class ChecklistItems(db.Model):
    __tablename__ = "checklist_items"

    id = db.Column(db.Integer(),primary_key=True, autoincrement=True)
    checklist_id = db.Column(db.Integer(), ForeignKey("checklists.id"))
    name = db.Column(db.String())
    
    created_at = db.Column(db.TIMESTAMP(), nullable=True, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.TIMESTAMP(), nullable=True, default=datetime.datetime.utcnow())
    deleted_at = db.Column(db.TIMESTAMP(), nullable=True)
    
    def __init__(
        self,
        name,
        deleted_at,
        created_at,
        updated_at,
    ):
        self.name = name
        self.deleted_at = deleted_at
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }