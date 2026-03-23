from src.airplane_table import AirplaneTable

def test_airplane_table_init(airplane_table_1):
    assert airplane_table_1.country == 'Spain'
    assert airplane_table_1.callsign == 'LVL2604'
    assert airplane_table_1.velocity == 309.77
    assert airplane_table_1.vertical_rate == 0
    assert airplane_table_1.bar_altitude == 11582.4


def test_airplane_table_get_table(airplane_table_1):
    result = airplane_table_1.get_table_from_airplane()

    assert result == [
        ["Country", "Callsign", "Velocity", "Vertical Rate", "Bar Altitude"],
        ['Spain', 'LVL2604', 309.77, 0, 11582.4,]
    ]