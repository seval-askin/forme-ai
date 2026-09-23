import os
import tempfile

import pytest

from app import create_app


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()

    os.environ["DATABASE_URL"] = db_path

    app = create_app("development")
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(db_path)


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()
    assert data["basari"] is True
    assert data["durum"] == "calisiyor"


def test_lead_ekleme(client):
    response = client.post(
        "/api/leads",
        json={
            "isim": "Test Musteri",
            "telefon": "05550000000",
            "mesaj": "Kisiye ozel FORME urunu istiyorum",
        },
    )

    assert response.status_code == 201

    data = response.get_json()
    assert data["basari"] is True


def test_lead_listeleme(client):
    client.post(
        "/api/leads",
        json={
            "isim": "Test Musteri",
            "telefon": "05550000000",
            "mesaj": "FORME test talebi",
        },
    )

    response = client.get("/api/leads")

    assert response.status_code == 200

    data = response.get_json()
    assert data["basari"] is True
    assert isinstance(data["leadler"], list)


def test_eksik_lead_bilgisi(client):
    response = client.post(
        "/api/leads",
        json={
            "isim": "",
            "telefon": "",
        },
    )

    assert response.status_code == 400