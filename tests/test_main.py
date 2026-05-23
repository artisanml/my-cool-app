"""Lightweight API checks for the demo server."""

from fastapi.testclient import TestClient

from main import PUBLIC, app

client = TestClient(app)


def test_health_returns_ok_json() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_index_serves_pomodoro_html() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "")
    body = response.text
    assert "Pomodoro" in body
    assert (PUBLIC / "index.html").read_text(encoding="utf-8") == body
