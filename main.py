from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    nome: str
    descricao: str

itens_db: List[Item] = []

@app.get("/itens", response_model=List[Item])
def listar_itens():
    return itens_db

@app.post("/itens", response_model=Item)
def adicionar_item(item: Item):
    for existente in itens_db:
        if existente.id == item.id:
            raise HTTPException(status_code=400, detail="ID já existe.")
    itens_db.append(item)
    return item
