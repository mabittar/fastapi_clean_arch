from fastapi import APIRouter, Depends, HTTPException

from src.application.usecase import (CreateItemUsecase, ReadItemUsecase,
                                     UpdateItemUsecase)

from .schema.item_schema import ItemSchema

item_router = APIRouter(tags=["item"], prefix="/v1")

items = {}


def find_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return None


# Crie uma rota com parâmetros
@item_router.get("/items/{item_id}")
async def read_item(
    item_id: int,
    query_param: str = None,
    use_case: ReadItemUsecase = Depends(ReadItemUsecase),
) -> ItemSchema:
    item = await use_case.execute(item_id)
    return item


# Rota de criação de itens
@item_router.post("/items/")
async def create_item(
    item: ItemSchema, use_case: CreateItemUsecase = Depends(CreateItemUsecase)
) -> ItemSchema:
    item = await use_case.execute(item)
    return item


# Rota de atualização de itens
@item_router.put("/items/{item_id}")
async def update_item(
    item_id: int,
    updated_item: ItemSchema,
    use_case: UpdateItemUsecase = Depends(UpdateItemUsecase),
) -> ItemSchema:
    item = await use_case.execute({"item_id": item_id, "updated_item": updated_item})
    return item


# Rota de exclusão de itens DeleteItemUsecase
@item_router.delete("/items/{item_id}")
async def delete_item(
    item_id: int, 
    use_case: UpdateItemUsecase = Depends(UpdateItemUsecase),
    ) -> dict[str, str]:
    await use_case.execute(item_id)
    return {"message": f"Item {item_id} excluído com sucesso"}
