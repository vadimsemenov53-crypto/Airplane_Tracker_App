import pytest

from unittest.mock import patch
from src.base_api_work import BaseApiWork
from requests.exceptions import HTTPError, RequestException


@patch("src.base_api_work.requests.get")
def test_base_api_make_request(mock_get):
    mock_response = mock_get.return_value

    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {'test' : 'tests'}

    result = BaseApiWork._make_request('http:test', params={'params': 1})
    assert result == {'test' : 'tests'}


@patch("src.base_api_work.requests.get")
def test_base_api_make_request_http_error(mock_get):
    mock_response = mock_get.return_value

    mock_response.raise_for_status.side_effect = HTTPError("404 Not Found")

    with pytest.raises(RuntimeError, match='Ошибка HTTP: 404 Not Found'):
        BaseApiWork._make_request('http:test', params={'params': 1})


@patch("src.base_api_work.requests.get")
def test_base_api_make_request_exception(mock_get):
    mock_response = mock_get.return_value

    mock_response.raise_for_status.side_effect = RequestException("Ошибка доступа.")

    with pytest.raises(RuntimeError, match='Ошибка RequestException: Ошибка доступа.'):
        BaseApiWork._make_request('http:test', params={'params': 1})


@patch("src.base_api_work.requests.get")
def test_base_api_make_request_json_error(mock_get):
    mock_response = mock_get.return_value

    mock_response.raise_for_status.return_value = None
    mock_response.json.side_effect = ValueError("Invalid JSON")

    with pytest.raises(RuntimeError, match='Ошибка JSON: Invalid JSON'):
        BaseApiWork._make_request('http:test', params={'params': 1})