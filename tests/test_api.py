import pytest

from unittest.mock import Mock, patch
from requests import RequestException
from src.api import APICoordinates, APIAircraft

def test_api_coord_base():
    api = APICoordinates()

    assert api.url == 'https://nominatim.openstreetmap.org/search'
    assert not api.coordinates
    assert not api.data_response


@patch("src.api.get")
def test_api_coord_response(mock_get, capsys, response_from_map):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = response_from_map

    api = APICoordinates()
    api.get_response_api('Canada')

    assert api.data_response[0]['name'] == 'Canada'
    assert api.data_response[0]['boundingbox'] == [
        "41.6765597",
        "83.3362128",
        "-141.0027500",
        "-52.3237664"
    ]

    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == 'Успешный ответ API'


@patch("src.api.get")
def test_api_coord_response_error_api(mock_get, capsys, response_from_map):
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = response_from_map

    api = APICoordinates()
    api.get_response_api('Canada')

    message = capsys.readouterr()
    assert message.out.strip().split('\n') == 'Ошибка API:'