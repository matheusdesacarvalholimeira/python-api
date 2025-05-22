from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_itens_vazio():
    response = client.get("/itens")
    assert response.status_code == 200
    assert response.json() == []

def test_post_item():
    data = {
        "id": 1,
        "nome": "Teste",
        "descricao": "Descrição do teste"
    }
    response = client.post("/itens", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_itens_apos_post():
    response = client.get("/itens")
    assert response.status_code == 200
    json_resp = response.json()
    assert len(json_resp) == 1
    assert json_resp[0]["id"] == 1
    assert json_resp[0]["nome"] == "Teste"

def test_post_item_com_id_duplicado():
    data = {
        "id": 1,
        "nome": "Outro",
        "descricao": "Outro item"
    }
    response = client.post("/itens", json=data)
    assert response.status_code == 400
    assert response.json()["detail"] == "ID já existe."
