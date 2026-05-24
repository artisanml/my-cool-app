"""Lightweight API checks for the demo server."""

from fastapi.testclient import TestClient

from main import PREMIUM_THANK_YOU, PUBLIC, UNLIMITED_THANK_YOU, app

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
    assert "Prestige-tier access" in body
    assert (PUBLIC / "index.html").read_text(encoding="utf-8") == body


def test_subscribe_premium_message() -> None:
    response = client.post("/subscribe", json={"tier": "premium"})
    assert response.status_code == 201
    assert response.json() == {"message": PREMIUM_THANK_YOU}


def test_subscribe_unlimited_message() -> None:
    response = client.post("/subscribe", json={"tier": "unlimited"})
    assert response.status_code == 201
    assert response.json() == {"message": UNLIMITED_THANK_YOU}


def test_subscribe_rejects_unknown_tier() -> None:
    response = client.post("/subscribe", json={"tier": "student"})
    assert response.status_code == 422
