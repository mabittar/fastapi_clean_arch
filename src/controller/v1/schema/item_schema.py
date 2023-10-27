from pydantic import BaseModel, ConfigDict


class ItemSchema(BaseModel):
    item_id: int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)
