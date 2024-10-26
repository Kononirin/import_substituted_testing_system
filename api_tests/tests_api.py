import json
import pytest
import requests

URL = "http://localhost:8000/"

def test_response_body():
    response = requests.get(URL)
    data_dict = response.json()

    expected_data = {'Hello': 'World'}

    assert data_dict == expected_data


def test_create_test_case():
    data =    {
        "id": 2,
        "name": "Olga",
        "description": "first test case",
        "steps": [
            "step one",
            "step two"
        ],
        "expected_result": "success",
        "priority": "низкий"
    }

    response = requests.post("http://localhost:8000/testcases", json = data)

    assert response.json()["id"] == 2