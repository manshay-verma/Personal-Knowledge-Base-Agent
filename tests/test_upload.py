from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_upload_valid_pdf():

    pdf_path = Path("tests/sample.pdf")

    with open(pdf_path, "rb") as pdf:

        response = client.post(
            "/documents/upload",
            files={
                "file": (
                    "sample.pdf",
                    pdf,
                    "application/pdf"
                )
            }
        )

    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "Document uploaded successfully"
    assert data["filename"] == "sample.pdf"
    assert data["chunks"] > 0
    assert "document_id" in data


def test_upload_invalid_file():

    response = client.post(
        "/documents/upload",
        files={
            "file": (
                "sample.txt",
                b"hello world",
                "text/plain"
            )
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Only PDF files are supported."


def test_upload_without_file():

    response = client.post("/documents/upload")

    assert response.status_code == 422

from app.main import app

def test_routes():
    for route in app.routes:
        print(route.path)