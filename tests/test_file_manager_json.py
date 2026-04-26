import json
from json import JSONDecodeError
from unittest.mock import patch

import pytest

from src.file_manager_json import FileManagerJson


def test_manager_json_init():
    file_1 = FileManagerJson()
    file_2 = FileManagerJson("report.json")

    assert file_1._filename == "data.json"
    assert file_2._filename == "report.json"


def test_manager_json_save_path(tmp_path, data_response_airplane):
    path_to_file_1 = tmp_path / "data.json"
    file_1 = FileManagerJson()
    file_1.save_to_file(data_response_airplane, str(path_to_file_1))

    assert path_to_file_1.exists()


@patch("os.makedirs")
@patch("src.file_manager_json.get_default_path_save")
@patch("builtins.open")
def test_manager_json_save_base_path(mock_open, mock_get_path, mock_dir, data_response_airplane):
    mock_get_path.return_value = "test_path/data.json"

    file = FileManagerJson()
    file.save_to_file(data_response_airplane, path_to_save=None)

    mock_get_path.assert_called_once()
    mock_dir.assert_called_once()

    args, kwargs = mock_open.call_args
    assert "test_path/data.json" in args[0]


def test_manager_json_save(tmp_path, data_response_airplane):
    path_to_file = tmp_path / "data.json"

    ex_1 = FileManagerJson()
    ex_1.save_to_file(data_response_airplane, str(path_to_file))

    assert path_to_file.exists()

    expected_data = [air.get_dict_from_airplane() for air in data_response_airplane]

    with open(path_to_file, "r", encoding="utf-8") as f:
        save_data = json.load(f)

    assert save_data == expected_data


def test_manager_json_save_error(tmp_path):
    path_to_file = tmp_path / "data.json"

    ex_1 = FileManagerJson()

    with pytest.raises(ValueError, match="Переданы пустые данные."):
        ex_1.save_to_file([], str(path_to_file))


def test_manager_json_save_is_dir(tmp_path, data_response_airplane):
    ex_1 = FileManagerJson()
    ex_1.save_to_file(data_response_airplane, str(tmp_path))

    path_to_file = tmp_path / "data.json"
    assert path_to_file.exists()

    expected_data = [air.get_dict_from_airplane() for air in data_response_airplane]

    with open(path_to_file, "r", encoding="utf-8") as f:
        data_file = json.load(f)

    assert data_file == expected_data


@patch("builtins.open")
def test_manager_json_save_os_error(mock_open, tmp_path, data_response_airplane):
    mock_open.side_effect = OSError("Test error")

    ex_1 = FileManagerJson()

    with pytest.raises(RuntimeError, match="Ошибка записи: Test error"):
        ex_1.save_to_file(data_response_airplane, str(tmp_path))

    mock_open.assert_called_once()


def test_manager_json_read(tmp_path, data_airplane_for_read):
    path = tmp_path / "data.json"

    with open(str(path), "w", encoding="utf-8") as f:
        json.dump(data_airplane_for_read, f)

    ex_1 = FileManagerJson()
    response = ex_1.read_file(str(path))

    assert response == data_airplane_for_read


def test_manager_json_read_not_file():
    ex_1 = FileManagerJson()
    with pytest.raises(FileNotFoundError, match="Файл не найден: test/test.json"):
        ex_1.read_file("test/test.json")


@patch("src.file_manager_json.json.load")
def test_manager_json_read_error_decod(mock_load, tmp_path):
    mock_load.side_effect = JSONDecodeError("Декодирование", doc="", pos=0)

    path = tmp_path / "data.json"

    with open(str(path), "w", encoding="utf-8") as f:
        json.dump([{"test": "test"}], f)

    ex_1 = FileManagerJson()
    with pytest.raises(RuntimeError, match="Ошибка JSON: Декодирование"):
        ex_1.read_file(str(path))

    mock_load.assert_called_once()


def test_manager_json__ensure_list():
    ex_1 = FileManagerJson()
    result = ex_1._ensure_list([{"test": "test"}])
    assert result == [{"test": "test"}]


def test_manager_json__ensure_list_error():
    ex_1 = FileManagerJson()
    with pytest.raises(ValueError, match="Файл должен содержать список объектов."):
        ex_1._ensure_list(12333)


def test_manager_json_add(tmp_path, airplane_3, data_response_airplane):
    path = tmp_path / "data.json"

    ex_1 = FileManagerJson()
    ex_1.save_to_file(data_response_airplane, str(path))
    report = ex_1.read_file(str(path))
    assert len(report) == 2

    ex_1.add_info_file([airplane_3], str(path))
    report = ex_1.read_file(str(path))
    assert len(report) == 3

    ex_1.add_info_file([airplane_3], str(path))
    report = ex_1.read_file(str(path))
    assert len(report) == 3


def test_manager_json_delete(tmp_path, airplane_3, data_response_airplane):
    path = tmp_path / "data.json"

    ex_1 = FileManagerJson()
    ex_1.save_to_file(data_response_airplane, str(path))
    ex_1.add_info_file([airplane_3], str(path))
    report = ex_1.read_file(str(path))
    assert len(report) == 3
    assert report[2]["callsign"] == "LVL2517"

    ex_1.delete_info_file("2312", str(path))
    report = ex_1.read_file(str(path))
    assert len(report) == 3
    assert report[2]["callsign"] == "LVL2517"

    ex_1.delete_info_file("LVL2517", str(path))
    report = ex_1.read_file(str(path))
    assert len(report) == 2
