import datetime
from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import ForeignKey

class ChecklistItems(db.Model):
    __tablename__ = "checklist_items"

    id = db.Column(db.Integer(),primary_key=True, autoincrement=True)
    checklist_id = db.Column(db.Integer(), ForeignKey("checklists.id"))
    name = db.Column(db.String())
    status = db.Column(db.String(), default="Deactivated")
    
    created_at = db.Column(db.TIMESTAMP(), nullable=True, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.TIMESTAMP(), nullable=True, default=datetime.datetime.utcnow())
    deleted_at = db.Column(db.TIMESTAMP(), nullable=True)

    checklist = relationship("Checklists", backref="checklist_items", uselist=False)
    
    def __init__(
        self,
        checklist_id,
        name,
        deleted_at,
        created_at,
        updated_at,
    ):
        self.name = name
        self.checklist_id = checklist_id
        self.deleted_at = deleted_at
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "checklist":{
                "id":self.checklist.id if self.checklist is not None else None,
                "name":self.checklist.name if self.checklist is not None else None
            },
            "status": self.status
        }
