from unittest.mock import patch

import pandas as pd
import pytest

from src.file_manager_excel import FileManagerEXCEL


def test_file_manager_excel_init():
    file_1 = FileManagerEXCEL()
    file_2 = FileManagerEXCEL("report.xlsx")

    assert file_1._filename == "data.xlsx"
    assert file_2._filename == "report.xlsx"


def test_file_manager_csv_save_path(tmp_path, data_response_airplane):
    path_to_file_1 = tmp_path / "data.xlsx"
    file_1 = FileManagerEXCEL()
    file_1.save_to_file(data_response_airplane, str(path_to_file_1))

    assert path_to_file_1.exists()


@patch("os.makedirs")
@patch("pandas.DataFrame.to_excel")
def test_manager_json_save_base_path(mock_csv, mock_dir, data_response_airplane):
    file = FileManagerEXCEL()
    file.save_to_file(data_response_airplane, path_to_save=None)

    mock_dir.assert_called_once()

    args, kwargs = mock_csv.call_args
    assert "Airplane_Tracker_App/data/data.xlsx" in args[0]


def test_file_manager_exec_save(tmp_path, data_response_airplane):
    path = tmp_path / "data.xlsx"

    file = FileManagerEXCEL()
    file.save_to_file(data_response_airplane, str(path))

    assert path.exists()

    df = file.read_file(str(path))

    assert df["country"][0] == "Germany"
    assert df["country"][1] == "Spain"


def test_file_manager_excel_save_error(tmp_path):
    path = tmp_path / "data.xlsx"

    file = FileManagerEXCEL()
    with pytest.raises(ValueError, match="Переданы пустые данные."):
        file.save_to_file([], str(path))


def test_file_manager_excel_save_is_dir(tmp_path, data_response_airplane):
    file = FileManagerEXCEL()
    file.save_to_file(data_response_airplane, str(tmp_path))

    path = tmp_path / "data.xlsx"
    assert path.exists()

    df = file.read_file(str(path))

    assert df["country"][0] == "Germany"
    assert df["country"][1] == "Spain"


@patch("builtins.open")
def test_file_manager_excel_save_os_error(mock_open, tmp_path, data_response_airplane):
    mock_open.side_effect = OSError("Test error")

    file = FileManagerEXCEL()
    with pytest.raises(RuntimeError, match="Ошибка записи: Test error"):
        file.save_to_file(data_response_airplane, str(tmp_path))


def test_file_manager_excel_read(tmp_path, data_response_airplane):
    file = FileManagerEXCEL()
    file.save_to_file(data_response_airplane, str(tmp_path))

    path = tmp_path / "data.xlsx"

    df_data = file.read_file(str(path))

    df_save = pd.DataFrame([air.get_dict_from_airplane() for air in data_response_airplane])

    assert df_data.equals(df_save)


def test_file_manager_excel_read_error():
    file = FileManagerEXCEL()

    with pytest.raises(FileNotFoundError, match="Файл не найден: fake_path/data.xlsx"):
        file.read_file("fake_path/data.xlsx")


def test_file_manager_excel_add(tmp_path, data_response_airplane, airplane_3):
    path = tmp_path / "data.xlsx"

    file = FileManagerEXCEL()
    file.save_to_file(data_response_airplane, str(path))

    df_read = file.read_file(str(path))

    df_save = pd.DataFrame([air.get_dict_from_airplane() for air in data_response_airplane])
    assert df_read.equals(df_save)
    assert df_read["country"][1] == "Spain"

    file.add_info_file([airplane_3], str(path))
    df_read = file.read_file(str(path))

    assert df_read["country"][2] == "Turkey"


@patch("pandas.DataFrame.to_excel")
def test_file_manager_excel_add_error(mock_excel, tmp_path, file_excel_saves, airplane_3):
    mock_excel.side_effect = OSError("Test error")
    path = tmp_path / "data.xlsx"

    assert path.exists()

    with pytest.raises(RuntimeError, match="Ошибка записи: Test error"):
        file_excel_saves.add_info_file([airplane_3], path)


def test_file_manager_excel_delete(tmp_path, file_excel_saves):
    path = tmp_path / "data.xlsx"

    read_file = file_excel_saves.read_file(str(path))
    assert read_file["callsign"][0] == "ECA4RT"
    assert read_file["callsign"][1] == "LVL2604"

    file_excel_saves.delete_info_file("ECA4RT", str(path))
    read_file = file_excel_saves.read_file(str(path))

    assert read_file["callsign"][0] == "LVL2604"

    with pytest.raises(KeyError):
        assert read_file["callsign"][1] == "LVL2604"


@patch("pandas.DataFrame.to_excel")
def test_file_manager_excel_delete_error(mock_excel, tmp_path, file_excel_saves):
    mock_excel.side_effect = OSError("Test error")
    path = tmp_path / "data.xlsx"

    assert path.exists()

    with pytest.raises(RuntimeError, match="Ошибка записи: Test error"):
        file_excel_saves.delete_info_file("LVL2604", str(path))
