import unittest

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


class TestHealthCheck(unittest.TestCase):

    def test_item_root(self):
        result = client.get("/health")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json(), {"status": "OK"})
