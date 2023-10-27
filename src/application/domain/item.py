from datetime import datetime

from pydantic import BaseModel, ConfigDict

from .email import Email


class ItemModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    item_id: int
    name: str
    email: str
    updated_at: datetime
    created_at: datetime


class Item:
    def __init__(
        self,
        item_id: int,
        name: str,
        email: str,
        updated_at: datetime = datetime.utcnow(),
        created_at: datetime = datetime.utcnow(),
    ):
        self.item_id = item_id
        self.name = name
        self.email = Email(email)
        self.updated_at = updated_at if updated_at else datetime.now()
        self.created_at = created_at if created_at else datetime.now()

    def to_model(self) -> ItemModel:
        return ItemModel.model_validate(
            {
                "item_id": self.item_id,
                "name": self.name,
                "email": self.email.to_value(),
                "updated_at": self.updated_at,
                "created_at": self.created_at,
            }
        )
