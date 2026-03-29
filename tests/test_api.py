from unittest.mock import patch

import pytest
from requests import RequestException

from src.api import APIAircraft, APICoordinates


def test_api_coord_base():
    api = APICoordinates()

    assert api.url == "https://nominatim.openstreetmap.org/search"
    assert api.coordinates is None
    assert api._data_response is None


@patch("src.base_api_work.BaseApiWork._make_request")
def test_api_coord_response(mock_get, response_from_map):
    mock_get.return_value = response_from_map

    api = APICoordinates()
    api.get_response_api("Canada")

    assert api._data_response == response_from_map
    assert api._data_response[0]["name"] == "Canada"
    assert api._data_response[0]["boundingbox"] == ["41.6765597", "83.3362128", "-141.0027500", "-52.3237664"]

    mock_get.assert_called_once()


@patch("src.base_api_work.BaseApiWork._make_request")
def test_api_coord_response_error_api(mock_get):
    mock_get.side_effect = RequestException("Api error")

    api = APICoordinates()

    with pytest.raises(RequestException, match="Api error"):
        api.get_response_api("Canada")

    mock_get.assert_called_once()


@patch("src.base_api_work.BaseApiWork._make_request")
def test_api_coord_get_coordinates(mock_get, response_from_map):
    mock_get.return_value = response_from_map

    api = APICoordinates()
    api.get_response_api("Canada")
    api.get_coordinates()

    assert api.coordinates == {
        "lamax": "83.3362128",
        "lamin": "41.6765597",
        "lomax": "-52.3237664",
        "lomin": "-141.0027500",
    }

    mock_get.assert_called_once()


@patch("src.base_api_work.BaseApiWork._make_request")
def test_api_coord_get_coordinates_error(mock_get, response_from_map):
    mock_get.return_value = []

    api = APICoordinates()
    api.get_response_api("Canada")

    with pytest.raises(ValueError, match="Полученные данные пустые."):
        api.get_coordinates()

    mock_get.assert_called_once()


def test_api_air_base():
    api = APIAircraft()

    assert api.url == "https://opensky-network.org/api/states/all?"
    assert api.aeroplanes is None


@patch("src.base_api_work.BaseApiWork._make_request")
def test_api_air_response(mock_get, coordinates_from_aircraft, data_airplanes):
    mock_get.return_value = data_airplanes

    api = APIAircraft()
    api.get_response_api(coordinates_from_aircraft)

    assert api.aeroplanes == data_airplanes
    assert api.aeroplanes["states"][0][2] == "Switzerland"
    mock_get.assert_called_once()
