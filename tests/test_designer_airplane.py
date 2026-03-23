import pytest

from src.designer_airplane import DesignerAirplane


def test_designer_airplane_base(data_airplanes):
    air_data = DesignerAirplane(data_airplanes)

    assert air_data._data == data_airplanes


def test_designer_airplane_init_error():
    with pytest.raises(ValueError, match="Данные пустые или не переданы."):
        DesignerAirplane(_data={})


def test_designer_airplane_get_report(data_airplanes):
    air = DesignerAirplane(data_airplanes)
    report = air._get_report()

    assert len(report) == 3
    assert report[0].country == 'Switzerland'
    assert report[1].country == 'Germany'
    assert report[2].country == 'Spain'


def test_designer_airplane_get_report_error():
    response = {"test": "test", "testing": "testing"}
    air = DesignerAirplane(response)
    assert air._data == response

    with pytest.raises(ValueError, match="Некорректные данные API."):
        air._get_report()


def test_designer_airplane_save_number(data_airplanes):
    air = DesignerAirplane(data_airplanes)

    assert air._save_number(222) == 222.0
    assert air._save_number(0) == 0.0
    assert air._save_number("22") == 0.0
    assert air._save_number(None) == 0.0


def test_designer_airplane_filtered_velocity(data_airplanes):
    air = DesignerAirplane(data_airplanes)
    assert air._data == data_airplanes

    air._get_report()
    assert air._result_data[0].velocity == 189.7
    assert air._result_data[1].velocity == 289.7
    assert air._result_data[2].velocity == 0.0

    result_velocity = air._filtered_velocity()

    assert result_velocity[0].velocity == 289.7
    assert result_velocity[1].velocity == 189.7
    assert result_velocity[2].velocity == 0


def test_designer_airplane_filtered_bar(data_airplanes):
    air = DesignerAirplane(data_airplanes)
    assert air._data == data_airplanes

    air._get_report()
    assert air._result_data[0].bar_altitude == 4267.2
    assert air._result_data[1].bar_altitude == 5567.2
    assert air._result_data[2].bar_altitude == 0.0

    result_velocity = air._filtered_bar_altitude()

    assert result_velocity[0].bar_altitude == 5567.2
    assert result_velocity[1].bar_altitude == 4267.2
    assert result_velocity[2].bar_altitude == 0
