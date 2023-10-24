from fastapi import HTTPException, status

from ...controller.v1.schema.item_schema import ItemSchema
from ...infra.data.entities.item_entity import ItemEntity
from ...infra.data.repository.item_repository import ItemRepositoryDatabase
from ...infra.database.pg_adapter import AsyncSessionDI
from .base_usecase import BaseUsecase


class DeleteItemUsecase(BaseUsecase):
    def __init__(self, session: AsyncSessionDI) -> None:
        self.session = session

    async def execute(self, input: int) -> ItemSchema:
        async with self.session.begin() as db:
            item_repository = ItemRepositoryDatabase(ItemEntity)
            db_item = await item_repository.get(db=db, item_id=input)
            if not db_item:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Item not found",
                )
            await item_repository.delete(db_item)
            return ItemSchema.model_validate(db_item)
