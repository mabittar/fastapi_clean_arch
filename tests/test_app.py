import unittest

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


class TestApp(unittest.TestCase):
    def test_app_get(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        # item_data = {"item_id": 1, "name": "Test Item", "email": "test@example.com"}
        # response = client.post("/items/", json=item_data)
        # assert response.status_code == 200
        # response_data = response.json()
        # assert response_data["item"]["item_id"] == 1
        # assert response_data["item"]["name"] == "Test Item"
        # assert response_data["item"]["email"] == "test@example.com"


if __name__ == "__main__":
    unittest.main()
