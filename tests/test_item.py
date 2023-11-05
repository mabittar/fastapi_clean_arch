import unittest
from random import randint

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from src.main import app

# client = TestClient(app)


class TestItem(unittest.TestCase):
    @staticmethod
    def make_valid_body():
        return {
            "item_id": randint(1, 1000), 
            "name": "Test Item", 
            "email": "test@example.com"
            }
    
    @pytest.mark.asyncio
    async def test_empty_body_must_raise_error(self):
        invalid_body = {}

        async with AsyncClient(app=app, base_url="http://test") as ac:
            result = await ac.post("/v1/items/", json=invalid_body)
        self.assertEqual(result.status_code , 422)
    
    @pytest.mark.asyncio
    async def test_body_without_name_must_raise_error(self):
        invalid_body = {
            "item_id": 0,
            "email": "test@example.com"
        }

        async with AsyncClient(app=app, base_url="http://test") as ac:
            result = await ac.post("/v1/items/", json=invalid_body)
        self.assertEqual(result.status_code , 422)
    
    @pytest.mark.asyncio
    async def test_body_invalid_email_must_raise_error(self):
        invalid_body = {
            "item_id": 0,
            "name": "test",
            "email": "test"
        }
        async with AsyncClient(app=app, base_url="http://test") as ac:
            result = await ac.post("/v1/items/", json=invalid_body)
        self.assertEqual(result.status_code , 400)

    
    @pytest.mark.asyncio
    async def test_item_post(self):
        item_data = self.make_valid_body()
        async with AsyncClient(app=app, base_url="http://test") as ac:
            result = await ac.post("/v1/items/", json=item_data)
        self.assertEqual(result.status_code , 200)
        result_response = result.json()
        self.assertEqual(result_response["item_id"] , item_data['item_id'])
        self.assertEqual(result_response["name"] , item_data['name'])
        self.assertEqual(result_response["email"] , item_data['email'])

    @pytest.mark.asyncio
    async def test_same_itemid_must_raise_error(self):
        item_data = self.make_valid_body()
        async with AsyncClient(app=app, base_url="http://test") as ac:
            await ac.post("/v1/items/", json=item_data)
            result = await ac.post("/v1/items/", json=item_data)
        self.assertEqual(result.status_code, 400)

    @pytest.mark.asyncio
    async def test_get_item(self):
        item_data = self.make_valid_body()
        async with AsyncClient(app=app, base_url="http://test") as ac:
            await ac.post("/v1/items/", json=item_data)
            result = await ac.get(f"/v1/items/{ item_data['item_id']}")
            self.assertEqual(result.status_code , 200)
            result_response = result.json()
            self.assertEqual(result_response["item_id"] , item_data['item_id'])
            self.assertEqual(result_response["name"] , item_data['name'])
            self.assertEqual(result_response["email"] , item_data['email'])

    @pytest.mark.asyncio
    async def test_get_invaid_item_must_rise_error(self):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            result = await ac.get("/v1/items/-1")
            self.assertEqual(result.status_code , 404)

    @pytest.mark.asyncio
    async def test_delete_item(self):
        item_data = self.make_valid_body()
        async with AsyncClient(app=app, base_url="http://test") as ac:
            await ac.post("/v1/items/", json=item_data)
            item_id = item_data['item_id']
            result = await ac.delete(f"/v1/items/{item_id}")
            self.assertEqual(result.status_code, 200)
            result_response = result.json()
            self.assertEqual(result_response['message'], f"Item {item_id} excluído com sucesso")

    @pytest.mark.asyncio
    async def test_delete_invaid_item_must_rise_error(self):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            result = await ac.delete("/v1/items/-1")
            self.assertEqual(result.status_code , 404)

    @pytest.mark.asyncio
    async def test_update_item(self):
        item_data = self.make_valid_body()
        async with AsyncClient(app=app, base_url="http://test") as ac:
            await ac.post("/v1/items/", json=item_data)
            item_data['name'] = 'new_name'
            result = await ac.put(f"/v1/items/{ item_data['item_id']}", json=item_data)
            self.assertEqual(result.status_code , 200)
            result_response = result.json()
            self.assertEqual(result_response['updated_item']['name'], 'new_name')

    @pytest.mark.asyncio
    async def test_update_invalid_body_must_raise_error(self):
        item_data = self.make_valid_body()
        async with AsyncClient(app=app, base_url="http://test") as ac:
            await ac.post("/v1/items/", json=item_data)
            result = await ac.put(f"/v1/items/{ item_data['item_id']}")
            self.assertEqual(result.status_code , 422)
