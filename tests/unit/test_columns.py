""" """


def test_get_columns(client):
    response = client.get("/columns")
    assert response.status_code == 200
