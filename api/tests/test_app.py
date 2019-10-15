from app.app import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_the_app_is_up_and_running():
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, world!'}
