from datetime import datetime
from typing import Any, Dict

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base_repository import (
    BaseRepository,
    CreateSchemaType,
    ModelType,
    UpdateSchemaType,
)


class ItemRepositoryDatabase(BaseRepository):
    async def get(self, db: AsyncSession, **kwargs) -> ModelType | None:
        query = select(self._model).filter_by(**kwargs)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    async def create(self, db: AsyncSession, object: CreateSchemaType) -> ModelType:
        object_dict = object.model_dump()
        db_object = self._model(**object_dict)
        db.add(db_object)
        await db.commit()
        return db_object

    async def update(
        self,
        db: AsyncSession,
        object: Dict[str, Any],
        db_object: ModelType | None = None,
    ) -> ModelType | None:
        if db_object:
            if isinstance(object, dict):
                update_data = object
            else:
                update_data = object.model_dump(exclude_unset=True)

            update_data.update({"updated_at": datetime.utcnow()})
            for field in object.__dict__:
                if field in update_data:
                    setattr(db_object, field, update_data[field])
            db.add(db_object)
            await db.commit()
            return db_object

    async def delete(
        self,
        session: AsyncSession,
    ) -> None:
        await session.delete(self._model)
        await session.flush()
