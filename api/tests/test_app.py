from app.app import app
from starlette.testclient import TestClient

from tests.helpers import test_deeds

client = TestClient(app)


def test_the_app_is_up_and_running():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}


def test_the_app_gets_deeds(mocker):
    mock = mocker.patch("app.app.get_deeds")
    mock.return_value = test_deeds
    response = client.get("/deeds")

    assert response.status_code == 200
    assert response.json() == test_deeds
