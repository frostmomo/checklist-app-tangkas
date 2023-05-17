from app import db

from model.checklist_items import ChecklistItems


class ChecklistItemRepository(db.Model):
    __tablename__ = "checklist_items"

    def get_by_id(id):
        data = ChecklistItems.query.filter_by(id=id, deleted_at=None).first()
        return data

    def get_by_email(emailaccount):
        data = ChecklistItems.query.filter_by(email=emailaccount).first()
        return data
  
    def get_by_phone(dataPhone):
        data = ChecklistItems.query.filter_by(phoneNumber=dataPhone).first()
        return data

    def get_by_client_id(dataClientId):
        data = ChecklistItems.query.filter_by(client_id=dataClientId).all()
        return data
