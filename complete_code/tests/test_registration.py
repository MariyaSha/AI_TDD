import importlib


def test_registration_page():
    app = importlib.import_module('app').app
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'Create Account' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert b'Register' in response.data


import pytest


@pytest.mark.parametrize('username', ['', 'a b', 'a_b', 'é', '用户', 'abc\n', '<script>'])
def test_reject_invalid_username(username):
    response = importlib.import_module('app').app.test_client().post(
        '/', data={'username': username, 'password': 'Abcd1!'})
    assert response.status_code == 400
    assert b'Username must contain only ASCII letters and digits.' in response.data


def test_successful_registration():
    response = importlib.import_module('app').app.test_client().post(
        '/', data={'username': 'User123', 'password': 'Abcd1!'})
    assert response.status_code == 200
    assert b'Registration successful' in response.data
    assert b'Abcd1!' not in response.data


@pytest.mark.parametrize('password', ['', 'Aa1!', 'abcd1!', 'ABCD1!', 'Abcde!', 'Abcde1', 'Abcd1 ', 'Abcd1\t', 'Abcd1é', 'Abcd1💡', 'Abcd١!'])
def test_reject_invalid_password(password):
    response = importlib.import_module('app').app.test_client().post(
        '/', data={'username': 'User123', 'password': password})
    assert response.status_code == 400
    assert b'Password must meet all requirements.' in response.data
    assert b'Registration successful' not in response.data


@pytest.mark.parametrize('password', ['Aa1!xy', 'Abcd1_', 'Abcd1~', 'Ab1! é'])
def test_valid_password(password):
    response = importlib.import_module('app').app.test_client().post(
        '/', data={'username': 'User123', 'password': password})
    assert response.status_code == 200
    assert b'Registration successful' in response.data


def test_missing_fields_rejected():
    assert importlib.import_module('app').app.test_client().post('/').status_code == 400
