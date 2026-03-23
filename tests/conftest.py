import pytest

from src.airplane import Airplane


@pytest.fixture()
def response_from_map():
    """Фикстура ответа от API-сервиса nominatim.openstreetmap.org"""
    return [
        {
            "place_id": 346277167,
            "licence": "Data © OpenStreetMap contributors, ODbL 1.0. http://osm.org/copyright",
            "osm_type": "relation",
            "osm_id": 1428125,
            "lat": "61.0666922",
            "lon": "-107.9917070",
            "class": "boundary",
            "type": "administrative",
            "place_rank": 4,
            "importance": 0.9082390417046676,
            "addresstype": "country",
            "name": "Canada",
            "display_name": "Canada",
            "boundingbox": ["41.6765597", "83.3362128", "-141.0027500", "-52.3237664"],
        }
    ]


@pytest.fixture()
def coordinates_from_aircraft():
    """Фикстура возвращает координаты для работы с API-сервисом https://opensky-network.org/api/states/all?"""
    return {"lamax": "83.3362128", "lamin": "41.6765597", "lomax": "-52.3237664", "lomin": "-141.0027500"}


@pytest.fixture()
def data_airplanes():
    """Фикстура возвращает ответ от API-сервиса https://opensky-network.org/api/states/all?"""
    return {
        "time": 1766142246,
        "states": [
            [
                "4b1812",
                "SWR438A ",
                "Switzerland",
                1766166618,
                1766166618,
                -0.0168,
                51.0888,
                4267.2,
                False,
                189.7,
                129.39,
                14.63,
                0,
                4282.44,
                "2061",
                False,
                0,
            ],
            [
                "4b5555",
                "SWR777A ",
                "Germany",
                1766166618,
                1766166618,
                0.0168,
                53.0888,
                5567.2,
                False,
                289.7,
                329.39,
                24.63,
                0,
                5555.44,
                "2061",
                False,
                0,
            ],
            [
                "4b1221",
                "S777A ",
                "Spain",
                1766166618,
                1766166618,
                0.0168,
                53.0888,
                None,
                False,
                None,
                329.39,
                24.63,
                0,
                5555.44,
                "2061",
                False,
                0,
            ],
        ],
    }


@pytest.fixture()
def airplane_1():
    """Фикстура экземпляра класса Airplane."""
    return Airplane("Germany", "ECA4RT", 222.98, 0.33, 13716)


@pytest.fixture()
def airplane_2():
    """Фикстура экземпляра класса Airplane."""
    return Airplane("Spain", "LVL2604", 309.77, 0, 11582.4)


@pytest.fixture()
def data_response_airplane():
    """Фикстура для тестов класса FileManager"""
    return [
        {"country": "Germany", "callsign": "222222", "velocity": 309.77, "vertical_rate": 0, "bar_altitude": 11582.4}
    ]
