import hashlib
import os
import pytest
import struct
from io import BytesIO

from app import app as flask_app


def sha256sum(file):
    sha256_hash = hashlib.sha256()
    buffer_size = 8192

    while chunk := file.read(buffer_size):
    	sha256_hash.update(chunk)

    return sha256_hash.hexdigest()


@pytest.fixture()
def app():
    flask_app.config.update({
        "TESTING": True,
    })

    yield flask_app


@pytest.fixture()
def client(app):
    return app.test_client()

# Used to test the testing framework
def test_false(client):
    if os.getenv("DEBUG_RETURN_FALSE"):
	    assert False
    else:
	    assert True

def test_show_image_has_content(client):
    response = client.get("/image/show")
    file = BytesIO(response.data)
    digest = "880e2b44ef39c1eb7cd7fac66efbe826c6611b560e0b03264f76879059cbcc92"
    assert response.status_code == 200
    assert sha256sum(file) == digest
    assert response.content_type == "image/png"


def test_tiff_version_returns_string(client):
    response = client.get("/tiff_version")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "LIBTIFF, Version 4.7.1"

