from abc import ABC, abstractmethod
from typing import Any, Dict, Type, TypeVar, Union

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseRepository(ABC):
    def __init__(self, model: Type[ModelType]) -> None:
        self._model = model

    @abstractmethod
    async def create(
            self, 
            db: AsyncSession,
            object: CreateSchemaType
    ) -> ModelType:
        raise NotImplementedError

    @abstractmethod
    async def get(self, db: AsyncSession, **kwargs) -> ModelType | None:
        raise NotImplementedError

    @abstractmethod
    async def update(
            self,
            db: AsyncSession,
            object: Union[UpdateSchemaType, Dict[str, Any]],
            db_object: ModelType | None = None,
            **kwargs
    ) -> ModelType | None:
        raise NotImplementedError
