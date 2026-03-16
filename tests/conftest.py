import pytest

@pytest.fixture()
def response_from_map():
    """ Фикстура ответа от API-сервиса nominatim.openstreetmap.org """
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
        "boundingbox": [
            "41.6765597",
            "83.3362128",
            "-141.0027500",
            "-52.3237664"
        ]
    }
]