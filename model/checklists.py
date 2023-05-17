from sqlalchemy.orm import relationship
import datetime
from app import db


class Checklists(db.Model):
    __tablename__ = "checklists"

    id = db.Column(db.Integer(),primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    
    created_at = db.Column(db.TIMESTAMP(), nullable=True, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.TIMESTAMP(), nullable=True, default=datetime.datetime.utcnow())
    deleted_at = db.Column(db.TIMESTAMP(), nullable=True)

    # checklist_item = relationship("ChecklistItems", backref="checklists", uselist=False)
    
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
