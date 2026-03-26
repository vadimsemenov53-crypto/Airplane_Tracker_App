from src.utils import airplanes_to_dicts, ensure_directory, get_default_path_save
from unittest.mock import patch

def test_airplanes_to_dicts(airplane_3):
    result = airplanes_to_dicts([airplane_3])

    assert result[0]['country'] == 'Turkey'
    assert result[0]['callsign'] == 'LVL2517'
    assert result[0]['velocity'] == 809.77
    assert result[0]['vertical_rate'] == 0
    assert result[0]['bar_altitude'] == 11582.4


def test_ensure_directory(tmp_path):
    path = tmp_path
    ensure_directory(str(tmp_path))

    assert path.exists()


def test_get_default_path_save():
    result = get_default_path_save('report.json')

    assert "Airplane_Tracker_App/data/report.json" in result