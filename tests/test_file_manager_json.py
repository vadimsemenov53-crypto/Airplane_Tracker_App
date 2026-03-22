import json
from json import JSONDecodeError
from unittest.mock import patch

import pytest

from src.file_manager_json import FileManagerJson


def test_manager_json_save(tmp_path, data_response_airplane):
    path_to_file = tmp_path / "data.json"

    ex_1 = FileManagerJson()
    ex_1.save_to_json_file(data_response_airplane, str(path_to_file))

    assert path_to_file.exists()

    with open(path_to_file, "r", encoding="utf-8") as f:
        save_data = json.load(f)

    assert save_data == data_response_airplane


def test_manager_json_save_error(tmp_path):
    path_to_file = tmp_path / "data.json"

    ex_1 = FileManagerJson()

    with pytest.raises(ValueError, match="Переданы пустые данные."):
        ex_1.save_to_json_file([], str(path_to_file))


def test_manager_json_save_is_dir(tmp_path, data_response_airplane):
    ex_1 = FileManagerJson()
    ex_1.save_to_json_file(data_response_airplane, str(tmp_path))

    path_to_file = tmp_path / "data.json"
    assert path_to_file.exists()

    with open(path_to_file, "r", encoding="utf-8") as f:
        data_file = json.load(f)

    assert data_file == data_response_airplane


@patch("builtins.open")
def test_manager_json_save_os_error(mock_open, tmp_path):
    mock_open.side_effect = OSError("Test error")

    ex_1 = FileManagerJson()

    with pytest.raises(RuntimeError, match="Ошибка записи: Test error"):
        ex_1.save_to_json_file([{"test": "test"}], str(tmp_path))

    mock_open.assert_called_once()


def test_manager_json_read(tmp_path, data_response_airplane):
    path = tmp_path / "data.json"

    with open(str(path), "w", encoding="utf-8") as f:
        json.dump(data_response_airplane, f)

    ex_1 = FileManagerJson()
    response = ex_1.read_file_json(str(path))

    assert response == data_response_airplane


def test_manager_json_read_not_file():
    ex_1 = FileManagerJson()
    with pytest.raises(FileNotFoundError, match="Файл не найден: test/test.json"):
        ex_1.read_file_json("test/test.json")


@patch("src.file_manager_json.json.load")
def test_manager_json_read_error_decod(mock_load, tmp_path):
    mock_load.side_effect = JSONDecodeError("Декодирование", doc="", pos=0)

    path = tmp_path / "data.json"

    with open(str(path), "w", encoding="utf-8") as f:
        json.dump([{"test": "test"}], f)

    ex_1 = FileManagerJson()
    with pytest.raises(RuntimeError, match="Ошибка JSON: Декодирование"):
        ex_1.read_file_json(str(path))

    mock_load.assert_called_once()


def test_manager_json__ensure_list():
    ex_1 = FileManagerJson()
    result = ex_1._ensure_list([{"test": "test"}])
    assert result == [{"test": "test"}]


def test_manager_json__ensure_list_error():
    ex_1 = FileManagerJson()
    with pytest.raises(ValueError, match="Файл должен содержать список объектов."):
        ex_1._ensure_list(12333)


def test_manager_json_add(tmp_path, airplane_2, data_response_airplane):
    path = tmp_path / "data.json"

    ex_1 = FileManagerJson()
    ex_1.save_to_json_file(data_response_airplane, str(path))
    report = ex_1.read_file_json(str(path))
    assert len(report) == 1

    ex_1.add_info_file_json(airplane_2, str(path))
    report = ex_1.read_file_json(str(path))
    assert len(report) == 2

    ex_1.add_info_file_json(airplane_2, str(path))
    report = ex_1.read_file_json(str(path))
    assert len(report) == 2


def test_manager_json_delete(tmp_path, airplane_2, data_response_airplane):
    path = tmp_path / "data.json"

    ex_1 = FileManagerJson()
    ex_1.save_to_json_file(data_response_airplane, str(path))
    ex_1.add_info_file_json(airplane_2, str(path))
    report = ex_1.read_file_json(str(path))
    assert len(report) == 2
    assert report[1]["callsign"] == "LVL2604"

    ex_1.delete_info_file_json("2312", str(path))
    report = ex_1.read_file_json(str(path))
    assert len(report) == 2
    assert report[1]["callsign"] == "LVL2604"

    ex_1.delete_info_file_json("LVL2604", str(path))
    report = ex_1.read_file_json(str(path))
    assert len(report) == 1
