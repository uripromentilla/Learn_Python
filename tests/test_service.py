import pytest
import source.service as service
import unittest.mock as mock
import requests


@mock.patch("source.service.get_user_from_db")
# We are patching this function. We are creating an object where we can control its return values.
# mock.patch returns an object connected to the function we are patching.
def test_get_user_from_db(mock_get_user_from_db):
    # We are setting the return value of the function to a user object.
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)
    assert user_name == "Mocked Alice"


@mock.patch("requests.get")
def test_get_users(mock_get):
    mock.response = mock.Mock()
    mock.response.status_code = 200
    mock.response.json.return_value = {"name": "John", "age": 30, "job": "cook"}
    mock_get.return_value = mock.response
    data = service.get_users()
    assert data == {"name": "John", "age": 30, "job": "cook"}


@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock.response = mock.Mock()
    mock.response.status_code = 404
    mock_get.return_value = mock.response
    with pytest.raises(requests.HTTPError):
        service.get_users()
