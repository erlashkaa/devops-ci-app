"""Tests for the Flask application."""

from app.app import app


def test_index():
    """The root endpoint identifies the service."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["service"] == "devops-ci-app"
    assert response.get_json()["version"] == "1.0.0"


def test_health():
    """The health endpoint reports a healthy state."""
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
