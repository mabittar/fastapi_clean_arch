from fastapi import HTTPException, status

from ...controller.v1.schema.item_schema import ItemSchema
from ...infra.data.entities.item_entity import ItemEntity
from ...infra.data.repository.item_repository import ItemRepositoryDatabase
from ...infra.database.pg_adapter import AsyncSessionDI
from ..domain.item import Item
from .base_usecase import BaseUsecase


class CreateItemUsecase(BaseUsecase):
    def __init__(self, session: AsyncSessionDI) -> None:
        self.session = session

    async def execute(self, input: ItemSchema) -> ItemSchema:
        async with self.session.begin() as db:
            item_repository = ItemRepositoryDatabase(ItemEntity)
            db_item = await item_repository.get(db=db, item_id=input.item_id)
            if db_item:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Item already exists",
                )
            item: Item = Item(**input.model_dump())
            db_object = await item_repository.create(db=db, object=item.to_model())
            return ItemSchema.model_validate(db_object)
