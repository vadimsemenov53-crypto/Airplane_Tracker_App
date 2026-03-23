def test_airplane_json_init(airplane_json_1):
    assert airplane_json_1.country == 'Germany'
    assert airplane_json_1.callsign == 'ECA4RT'
    assert airplane_json_1.velocity == 222.98
    assert airplane_json_1.vertical_rate == 0.33
    assert airplane_json_1.bar_altitude == 13716


def test_airplane_json_get_dict(airplane_json_1):
    result = airplane_json_1.get_dict_from_airplane()

    assert result == {
        "country": "Germany",
        "callsign": "ECA4RT",
        "velocity": 222.98,
        "vertical_rate": 0.33,
        "bar_altitude": 13716,
    }