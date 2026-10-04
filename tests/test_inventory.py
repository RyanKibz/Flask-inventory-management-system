from app import app
from data import inventory


def test_get_inventory():
    client = app.test_client()
    response = client.get("/inventory")
    assert response.status_code == 200


def test_get_item():
    client = app.test_client()
    response = client.get("/inventory/1")
    assert response.status_code == 200


def test_add_item():
    client = app.test_client()
    response = client.post("/inventory", json={
        "product_name": "Test Product",
        "brand": "Test Brand",
        "price": 5,
        "stock": 10
    })
    assert response.status_code == 201


def test_update_item():
    client = app.test_client()
    response = client.patch("/inventory/1", json={"stock": 25})
    assert response.status_code == 200
    assert response.json["stock"] == 25


def test_delete_item():
    client = app.test_client()

    inventory.append({
        "id": 99,
        "product_name": "Delete Me",
        "brand": "Test",
        "price": 1,
        "stock": 1
    })

    response = client.delete("/inventory/99")
    assert response.status_code == 200

def test_item_not_found():
    client = app.test_client()
    response = client.get("/inventory/999")
    assert response.status_code == 404
    