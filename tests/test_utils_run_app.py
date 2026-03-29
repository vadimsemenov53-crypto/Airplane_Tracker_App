from unittest.mock import MagicMock, patch

from interface.utils_run_app import (ask_user, get_airplane_object, get_file_format_user, get_file_manager,
                                     handle_file_operations, handle_save, show_message, show_report)


@patch("builtins.input", return_value="test input")
def test_ask_user(mock_input):
    result = ask_user()

    assert result == "test input"
    mock_input.assert_called_once_with("Пользователь: ")


def test_show_message(capsys):
    show_message("test")

    message = capsys.readouterr()

    assert message.out.strip() == "Программа:\ntest"


def test_show_report(capsys, airplane_3, airplane_2):
    show_report([airplane_2, airplane_3], 1)

    message = capsys.readouterr()

    assert message.out.strip() == "1. Позывной: LVL2604 | Скорость: 309.77 | Высота: 11582.4"


@patch("builtins.input", return_value=1)
def test_get_file_format_base(mock_input):
    result = get_file_format_user()

    assert result == 1
    mock_input.assert_called_once_with("Пользователь: ")


@patch("builtins.input", return_value=4)
def test_get_file_format_exit(mock_input, capsys):
    result = get_file_format_user()
    message = capsys.readouterr()

    assert not result
    assert message.out.strip().split("\n")[-1] == "Завершение работы с файлами."
    mock_input.assert_called_once_with("Пользователь: ")


@patch("builtins.input", side_effect=[5, 4])
def test_get_file_format(mock_input, capsys):
    result = get_file_format_user()

    message = capsys.readouterr()

    assert not result
    assert message.out.strip().split("\n")[-1] == "Завершение работы с файлами."
    assert "Неверный выбор (1, 2, 3, 4)" in message.out.strip().split("\n")

    mock_input.assert_called_with("Пользователь: ")


@patch("interface.utils_run_app.get_file_format_user", return_value=1)
def test_get_file_manager_base_1(mock_manager):
    file = get_file_manager("test")
    assert file._filename == "test.json"

    mock_manager.assert_called_once()


@patch("interface.utils_run_app.get_file_format_user", return_value=2)
def test_get_file_manager_base_2(mock_manager):
    file = get_file_manager("test")
    assert file._filename == "test.csv"

    mock_manager.assert_called_once()


@patch("interface.utils_run_app.get_file_format_user", return_value=3)
def test_get_file_manager_base_3(mock_manager):
    file = get_file_manager("test")
    assert file._filename == "test.xlsx"

    mock_manager.assert_called_once()


@patch("interface.utils_run_app.get_file_format_user", return_value=1)
def test_get_file_manager_base_4(mock_manager):
    file = get_file_manager()
    assert file._filename == "data.json"

    mock_manager.assert_called_once()


@patch("interface.utils_run_app.get_file_format_user", return_value=2)
def test_get_file_manager_base_5(mock_manager):
    file = get_file_manager()
    assert file._filename == "data.csv"

    mock_manager.assert_called_once()


@patch("interface.utils_run_app.get_file_format_user", return_value=3)
def test_get_file_manager_base_6(mock_manager):
    file = get_file_manager()
    assert file._filename == "data.xlsx"

    mock_manager.assert_called_once()


@patch("builtins.input", return_value="Germany, DLH777, 777, 7, 10000")
def test_get_airplane_object(mock_input):
    result = get_airplane_object()

    assert result.country == "Germany"
    assert result.velocity == 777

    mock_input.assert_called_once_with("Пользователь: ")


@patch("builtins.input", return_value="Germany, DLH777, AAA, 7, 10000")
def test_get_airplane_object_invalid_element(mock_input, capsys):
    result = get_airplane_object()

    message = capsys.readouterr()

    assert result is None
    assert "Ошибка: скорость и высота должны быть числами." in message.out

    mock_input.assert_called_once_with("Пользователь: ")


@patch("interface.utils_run_app.get_file_manager")
@patch("builtins.input", side_effect=["file", "/tmp"])
def test_handle_save_with_filename(mock_input, mock_get_file_manager):
    mock_file = MagicMock()
    mock_get_file_manager.return_value = mock_file

    report = [MagicMock()]

    handle_save(report)

    mock_get_file_manager.assert_called_with("file")
    mock_file.save_to_file.assert_called_once_with(report, "/tmp")


@patch("interface.utils_run_app.get_file_manager")
@patch("builtins.input", side_effect=["1", "/path", "4"])
def test_handle_file_read(mock_input, mock_get_file_manager):
    mock_file = MagicMock()
    mock_get_file_manager.return_value = mock_file
    mock_file.read_file.return_value = ["data"]

    handle_file_operations()

    mock_file.read_file.assert_called_once_with("/path")
