from fastapi import FastAPI

# Crie uma instância do FastAPI
app = FastAPI()

# Crie uma rota simples
@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao FastAPI!"}

# Crie uma rota com parâmetros
@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

# Rota de criação de itens
@app.post("/items/")
def create_item(item: dict):
    return item

# Rota de atualização de itens
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: dict):
    return {"item_id": item_id, "updated_item": updated_item}

# Rota de exclusão de itens
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} excluído com sucesso"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
