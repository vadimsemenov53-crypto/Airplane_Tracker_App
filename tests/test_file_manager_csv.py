from unittest.mock import patch

import pandas as pd
import pytest

from src.file_manager_csv import FileManagerCSV


def test_file_manager_csv_init():
    file_1 = FileManagerCSV()
    file_2 = FileManagerCSV("report.csv")

    assert file_1._filename == "data.csv"
    assert file_2._filename == "report.csv"


def test_file_manager_csv_save_path(tmp_path, data_response_airplane):
    path_to_file_1 = tmp_path / "data.json"
    file_1 = FileManagerCSV()
    file_1.save_to_file(data_response_airplane, str(path_to_file_1))

    assert path_to_file_1.exists()


@patch("os.makedirs")
@patch("pandas.DataFrame.to_csv")
def test_manager_json_save_base_path(mock_csv, mock_dir, data_response_airplane):
    file = FileManagerCSV()
    file.save_to_file(data_response_airplane, path_to_save=None)

    mock_dir.assert_called_once()

    args, kwargs = mock_csv.call_args
    assert "Airplane_Tracker_App/data/data.csv" in args[0]


def test_file_manager_csv_save(tmp_path, data_response_airplane):
    path = tmp_path / "data.csv"

    file = FileManagerCSV()
    file.save_to_file(data_response_airplane, str(path))

    assert path.exists()

    df = file.read_file(str(path))

    assert df["country"][0] == "Germany"
    assert df["country"][1] == "Spain"


def test_file_manager_csv_save_error(tmp_path):
    path = tmp_path / "data.csv"

    file = FileManagerCSV()
    with pytest.raises(ValueError, match="Переданы пустые данные."):
        file.save_to_file([], str(path))


def test_file_manager_csv_save_is_dir(tmp_path, data_response_airplane):
    file = FileManagerCSV()
    file.save_to_file(data_response_airplane, str(tmp_path))

    path = tmp_path / "data.csv"
    assert path.exists()

    df = file.read_file(str(path))

    assert df["country"][0] == "Germany"
    assert df["country"][1] == "Spain"


@patch("builtins.open")
def test_file_manager_csv_save_os_error(mock_open, tmp_path, data_response_airplane):
    mock_open.side_effect = OSError("Test error")

    file = FileManagerCSV()
    with pytest.raises(RuntimeError, match="Ошибка записи: Test error"):
        file.save_to_file(data_response_airplane, str(tmp_path))


def test_file_manager_csv_read(tmp_path, data_response_airplane):
    file = FileManagerCSV()
    file.save_to_file(data_response_airplane, str(tmp_path))

    path = tmp_path / "data.csv"

    df_data = file.read_file(str(path))

    df_save = pd.DataFrame([air.get_dict_from_airplane() for air in data_response_airplane])

    assert df_data.equals(df_save)


def test_file_manager_csv_read_error():
    file = FileManagerCSV()

    with pytest.raises(FileNotFoundError, match="Файл не найден: fake_path/data.csv"):
        file.read_file("fake_path/data.csv")


def test_file_manager_csv_add(tmp_path, data_response_airplane, airplane_3):
    path = tmp_path / "data.csv"

    file = FileManagerCSV()
    file.save_to_file(data_response_airplane, str(path))

    df_read = file.read_file(str(path))

    df_save = pd.DataFrame([air.get_dict_from_airplane() for air in data_response_airplane])
    assert df_read.equals(df_save)
    assert df_read["country"][1] == "Spain"

    file.add_info_file([airplane_3], str(path))
    df_read = file.read_file(str(path))

    assert df_read["country"][2] == "Turkey"


@patch("pandas.DataFrame.to_csv")
def test_file_manager_csv_add_error(mock_csv, tmp_path, file_csv_saves, airplane_3):
    mock_csv.side_effect = OSError("Test error")
    path = tmp_path / "data.csv"

    assert path.exists()

    with pytest.raises(RuntimeError, match="Ошибка записи: Test error"):
        file_csv_saves.add_info_file([airplane_3], path)


def test_file_manager_csv_delete(tmp_path, file_csv_saves):
    path = tmp_path / "data.csv"

    read_file = file_csv_saves.read_file(str(path))
    assert read_file["callsign"][0] == "ECA4RT"
    assert read_file["callsign"][1] == "LVL2604"

    file_csv_saves.delete_info_file("ECA4RT", str(path))
    read_file = file_csv_saves.read_file(str(path))

    assert read_file["callsign"][0] == "LVL2604"

    with pytest.raises(KeyError):
        assert read_file["callsign"][1] == "LVL2604"


@patch("pandas.DataFrame.to_csv")
def test_file_manager_csv_delete_error(mock_csv, tmp_path, file_csv_saves):
    mock_csv.side_effect = OSError("Test error")
    path = tmp_path / "data.csv"

    assert path.exists()

    with pytest.raises(RuntimeError, match="Ошибка записи: Test error"):
        file_csv_saves.delete_info_file("LVL2604", str(path))
