"""
Tests for rest_api.py
"""
import json
import pytest
from rest_api import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    test_client = app.test_client()
    return test_client


def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')


def test_lack_parameters(client):
    data = [{
        "fixed acidity": 6.6,
        "volatile acidity": 0.760,
        "citric acid": 0.4,
        "residual sugar": 2.30,
        "chlorides": 0.092,
        # "free sulfur dioxide": 15,
        "total sulfur dioxide": 54,
        "density": 0.997,
        "pH": 3.26,
        "sulphates": 0.65,
         # "alcohol": 9.8,
        "color": "red"
    }]
    response = post_json(client, "/predict", data)
    response_json = response.json
    assert response.status_code == 200
    assert type(response_json) == list
    assert len(response_json) == 1


def test_excess_parameters(client):
    data = [{
        "fixed acidity": 6.6,
        "volatile acidity": 0.760,
        "citric acid": 0.4,
        "residual sugar": 2.30,
        "chlorides": 0.092,
        "free sulfur dioxide": 15,
        "total sulfur dioxide": 54,
        "density": 0.997,
        "pH": 3.26,
        "sulphates": 0.65,
        "alcohol": 9.8,
        "color": "red",
        "privetiki": "privet"  # excess!
    }]
    response = post_json(client, "/predict", data)
    response_json = response.json
    assert response.status_code == 200
    assert type(response_json) == list
    assert len(response_json) == 1


def test_invalid_value(client):
    data = [{
        "fixed acidity": 6.6,
        "volatile acidity": 0.760,
        "citric acid": 0.4,
        "residual sugar": 2.30,
        "chlorides": 0.092,
        "free sulfur dioxide": 15,
        "total sulfur dioxide": 54,
        "density": 0.997,
        "pH": 3.26,
        "sulphates": 0.65,
        "alcohol": 9.8,
        "color": "BLACK!"
    }]
    response = post_json(client, "/predict", data)
    assert response.status_code == 400
    assert 'Invalid Value' in str(response.get_data())


def test_invalid_type(client):
    data = [{
        "fixed acidity": 6.6,
        "volatile acidity": 0.760,
        "citric acid": "0.4",
        "residual sugar": 2.30,
        "chlorides": 0.092,
        "free sulfur dioxide": 15,
        "total sulfur dioxide": 54,
        "density": 0.997,
        "pH": 3.26,
        "sulphates": 0.65,
        "alcohol": 9.8,
        "color": "red"
    }]
    response = post_json(client, "/predict", data)
    assert response.status_code == 400
    assert 'Invalid Type' in str(response.get_data())
