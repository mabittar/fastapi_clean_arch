from pydantic import BaseModel


class ItemDTO(BaseModel):
    item_id: int
    name: str
    email: str
