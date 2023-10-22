from fastapi import FastAPI, HTTPException

# Crie uma instância do FastAPI
app = FastAPI()

items = {}

def find_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return None

# Crie uma rota simples
@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao FastAPI!"}

# Crie uma rota com parâmetros
@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    memory_item = find_item(item_id)
    if not memory_item:
        raise HTTPException(status_code=404, detail="Item not exists")
    return memory_item

# Rota de criação de itens
@app.post("/items/")
def create_item(item: dict):
    memory_item = find_item(item['item_id'])
    if memory_item:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item['item_id']] = item
    return item

# Rota de atualização de itens
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: dict):
    memory_item = find_item(item_id)
    if not memory_item:
        raise HTTPException(status_code=404, detail="Item not exists")
    items[item_id] = updated_item
    
    return {"item_id": item_id, "updated_item": items[item_id] }

# Rota de exclusão de itens
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    memory_item = find_item(item_id)
    if not memory_item:
        raise HTTPException(status_code=404, detail="Item not exists")
    items.pop(item_id)
    return {"message": f"Item {item_id} excluído com sucesso"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
