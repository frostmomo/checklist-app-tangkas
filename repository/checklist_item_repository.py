from app import db

from model.checklist_items import ChecklistItems

 
class ChecklistItemRepository(db.Model):
    __tablename__ = "checklist_items"

    def get_all_by_checklist_id(checklist_id):
        data = ChecklistItems.query.filter_by(checklist_id=checklist_id, deleted_at=None).all()
        return data     

    def get_by_id(id):
        data = ChecklistItems.query.filter_by(id=id, deleted_at=None).first()
        return data
    
    def get_by_checklist_id(id,checklist_id):
        data = ChecklistItems.query.filter_by(id=id,checklist_id=checklist_id, deleted_at=None).first()
        return data

