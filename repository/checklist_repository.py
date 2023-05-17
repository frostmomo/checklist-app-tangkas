from app import db

from model.checklists import Checklists


class ChecklistsRepository(db.Model):
    __tablename__ = "checklists"

    def get_all_checklist():
        data = Checklists.query.filter_by(deleted_at=None).all()
        return data
    
    def get_by_id(id):
        data = Checklists.query.filter_by(id=id, deleted_at=None).first()
        return data