import pytest
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client


def test_home(client):
    """Home route returns welcome message"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Welcome to the Flask app!'}

def test_add_valid(client):
    """Adding two valid numbers"""
    response = client.post('/add', json={'a':3, 'b':4})
    assert response.status_code == 200
    assert response.get_json()['result'] == 7

def test_add_missing_field(client):
    """Missing one field should return 400"""
    response = client.post('/add', json={'a':4})
    assert response.status_code == 400
    assert 'error' in response.get_json()