from fastapi import HTTPException, status

from ...controller.v1.schema.item_schema import ItemSchema
from ...infra.data.entities.item_entity import ItemEntity
from ...infra.data.repository.item_repository import ItemRepositoryDatabase
from ...infra.database.pg_adapter import AsyncSessionDI
from ..domain.item import Item
from .base_usecase import BaseUsecase


class UpdateItemUsecase(BaseUsecase):
    def __init__(self, session: AsyncSessionDI) -> None:
        self.session = session

    async def execute(self, input: dict) -> ItemSchema:
        async with self.session.begin() as db:
            item_repository = ItemRepositoryDatabase(ItemEntity)
            item_id = input["item_id"]
            db_item = await item_repository.get(db=db, item_id=item_id)
            if not db_item:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Item not found",
                )
            updated_item = input["updated_item"]
            item: Item = Item(**updated_item.model_dump())
            db_object = await item_repository.update(
                db=db, object=item.to_model(), db_object=db_item
            )
            return ItemSchema.model_validate(db_object)
