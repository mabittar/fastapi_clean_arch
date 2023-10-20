from random import randint
import unittest

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


class TestApp(unittest.TestCase):
    @staticmethod
    def make_valid_body():
        return {
            "item_id": randint(1, 1000), 
            "name": "Test Item", 
            "email": "test@example.com"
            }

    def test_app_root(self):
        result = client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json(), {"message": "Bem-vindo ao FastAPI!"})

    def test_empty_body_must_raise_error(self):
        invalid_body = {}
        result = client.post("/items/", json=invalid_body)
        self.assertEqual(result.status_code , 422)

    def test_body_without_name_must_raise_error(self):
        invalid_body = {
            "item_id": 0,
            "email": "test@example.com"
        }
        result = client.post("/items/", json=invalid_body)
        self.assertEqual(result.status_code , 422)


    def test_app_post(self):
        item_data = self.make_valid_body()
        result = client.post("/items/", json=item_data)
        self.assertEqual(result.status_code , 200)
        result_response = result.json()
        self.assertEqual(result_response["item_id"] , item_data['item_id'])
        self.assertEqual(result_response["name"] , item_data['name'])
        self.assertEqual(result_response["email"] , item_data['email'])

    def test_same_itemid_must_raise_error(self):
        item_data = self.make_valid_body()
        client.post("/items/", json=item_data)
        result = client.post("/items/", json=item_data)
        self.assertEqual(result.status_code, 400)

    def test_get_item(self):
        item_data = self.make_valid_body()
        client.post("/items/", json=item_data)
        result = client.get(f"/items/{ item_data['item_id']}")
        self.assertEqual(result.status_code , 200)
        result_response = result.json()
        self.assertEqual(result_response["item_id"] , item_data['item_id'])
        self.assertEqual(result_response["name"] , item_data['name'])
        self.assertEqual(result_response["email"] , item_data['email'])

    def test_get_invaid_item_must_rise_error(self):
        result = client.get("/items/-1")
        self.assertEqual(result.status_code , 404)

    def test_delete_item(self):
        item_data = self.make_valid_body()
        client.post("/items/", json=item_data)
        item_id = item_data['item_id']
        result = client.delete(f"/items/{item_id}")
        self.assertEqual(result.status_code, 200)
        result_response = result.json()
        self.assertEqual(result_response['message'], f"Item {item_id} excluído com sucesso")

    def test_delete_invaid_item_must_rise_error(self):
        result = client.get("/items/-1")
        self.assertEqual(result.status_code , 404)

    def test_update_item(self):
        item_data = self.make_valid_body()
        client.post("/items/", json=item_data)
        item_data['name'] = 'new_name'
        result = client.put(f"/items/{ item_data['item_id']}", json=item_data)
        self.assertEqual(result.status_code , 200)
        result_response = result.json()
        self.assertEqual(result_response['updated_item']['name'], 'new_name')

    def test_update_invalid_body_must_raise_error(self):
        item_data = self.make_valid_body()
        client.post("/items/", json=item_data)
        result = client.put(f"/items/{ item_data['item_id']}")
        self.assertEqual(result.status_code , 422)

