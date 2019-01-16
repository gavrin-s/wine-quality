"""
Tests for rest_api.py
"""
import pytest
from rest_api import app


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    test_client = app.test_client()
    return test_client
