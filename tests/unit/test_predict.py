import json
import os


def test_missed_fields_with_FILL(client):
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
    # set autocomplete
    os.environ["FILL"] = "1"
    response = client.post("/predict", data=json.dumps(data), content_type='application/json')
    response_json = response.json
    assert response.status_code == 200
    assert type(response_json) == list
    assert len(response_json) == 1


def test_predic_missed_fields_without_FILL(client):
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
    # set autocomplete
    os.environ["FILL"] = "0"
    response = client.post("/predict", data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert "Incorrect properties order" in str(response.get_data())


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
    response = client.post("/predict", data=json.dumps(data), content_type='application/json')
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
    response = client.post("/predict", data=json.dumps(data), content_type='application/json')
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
    response = client.post("/predict", data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert 'Invalid Type' in str(response.get_data())


def test_invalid_query(client):
    data = {
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
        "color": "red"
    }
    response = client.post("/predict", data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert 'Invalid Query' in str(response.get_data())


def test_arbitrary_order(client):
    data = [{
        "alcohol": 9.8,
        "citric acid": 0.4,
        "pH": 3.26,
        "volatile acidity": 0.760,
        "color": "red",
        "residual sugar": 2.30,
        "total sulfur dioxide": 54,
        "density": 0.997,
        "sulphates": 0.65,
        "chlorides": 0.092,
        "free sulfur dioxide": 15,
        "fixed acidity": 6.6,
    }]
    response = client.post("/predict", data=json.dumps(data), content_type='application/json')
    response_json = response.json
    assert response.status_code == 200
    assert type(response_json) == list
    assert len(response_json) == 1
