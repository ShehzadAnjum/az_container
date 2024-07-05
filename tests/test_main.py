import pytest
from fastapi.testclient import TestClient
from az_container.main import app

client  = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Welcome to the Azure container world !"}

def test_name():
    response = client.get("/name")
    assert response.status_code == 200
    assert response.json() == {"name":"ShehzadAnjum"}

def test_batch():
    response = client.get("/batch")
    assert response.status_code ==200
    assert response.json() == {"batch":"36-37 Cloud computing and GenAI "}