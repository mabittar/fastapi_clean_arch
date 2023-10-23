from fastapi import APIRouter, HTTPException,status
from .dto.item_dto import ItemDTO

item_router = APIRouter(tags=["item"], prefix="/v1")

items = {}

def find_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return None
    
# Crie uma rota com parâmetros
@item_router.get("/items/{item_id}")
async def read_item(item_id: int, query_param: str = None):
    memory_item = find_item(item_id)
    if not memory_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not exists")
    return memory_item

# Rota de criação de itens
@item_router.post("/items/")
async def create_item(item: ItemDTO):
    memory_item = find_item(item.item_id)
    if memory_item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item already exists")
    items[item.item_id] = item.model_dump()
    return item

# Rota de atualização de itens
@item_router.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: ItemDTO):
    memory_item = find_item(item_id)
    if not memory_item:
        raise HTTPException(status_code=404, detail="Item not exists")
    items[item_id] = updated_item.model_dump()    
    return {"item_id": item_id, "updated_item": items[item_id] }

# Rota de exclusão de itens
@item_router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    memory_item = find_item(item_id)
    if not memory_item:
        raise HTTPException(status_code=404, detail="Item not exists")
    items.pop(item_id)
    return {"message": f"Item {item_id} excluído com sucesso"}
