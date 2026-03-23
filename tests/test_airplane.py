from src.airplane import Airplane


def test_airplane_base(airplane_1):
    assert airplane_1.country == "Germany"
    assert airplane_1.callsign == "ECA4RT"
    assert airplane_1.velocity == 222.98
    assert airplane_1.vertical_rate == 0.33
    assert airplane_1.bar_altitude == 13716


def test_airplane_repr_(airplane_1):
    assert airplane_1.__repr__() == "Airplane: ECA4RT, GermanyVelocity: 222.98, Bar_A: 13716"


def test_airplane__validate():
    air_1 = Airplane("air_1", "123", 222, 333, 444)
    air_2 = Airplane("air_2", "456", None, 333, "234")

    assert air_1._validate_velocity(air_1.velocity) == 222
    assert air_1._validate_bar_altitude(air_1.bar_altitude) == 444

    assert air_2._validate_velocity(air_2.velocity) == 0
    assert air_2._validate_bar_altitude(air_2.bar_altitude) == 0


def test_airplane_all_magic(airplane_1, airplane_2):
    assert airplane_1.bar_altitude == 13716
    assert airplane_2.bar_altitude == 11582.4

    assert not airplane_1.__lt__(airplane_2)
    assert airplane_1.__gt__(airplane_2)
    assert not airplane_1.__le__(airplane_2)
    assert airplane_1.__ge__(airplane_2)
    assert not airplane_1.__eq__(airplane_2)
    assert airplane_1.__ne__(airplane_2)


def test_airplane_magic_error(airplane_1):
    assert airplane_1.__eq__("222") == NotImplemented
    assert airplane_1.__eq__({"Bar": 2222}) == NotImplemented

    assert airplane_1.__ne__("222") == NotImplemented
    assert airplane_1.__ne__({"Bar": 2222}) == NotImplemented


def test_airplane_get_dict(airplane_1):
    assert airplane_1.get_dict_from_airplane() == {
        "country": "Germany",
        "callsign": "ECA4RT",
        "velocity": 222.98,
        "vertical_rate": 0.33,
        "bar_altitude": 13716,
    }
