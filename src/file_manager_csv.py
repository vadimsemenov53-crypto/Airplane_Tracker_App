import csv
import os

from src.airplane import Airplane
from src.base_file_manager import BaseFileManagerCSV


class FileManagerCSV(BaseFileManagerCSV):
    """Класс для работы с данными в формате CSV.
    Основные функции:
    1. Запись переданных данных в файл (требуется передать путь для записи файла).
    2. Чтение данных файла (требуется передать путь).
    3. Добавление данных в файл (требуется передать путь до файла и данные о самолете).
    4. Удаление данных о самолете из файла (требуется передать путь до файла и
    передать словарь с критериями.)"""

    def save_to_csv_file(self, data: list[dict[str, str | int | float | None]], path_to_save: str) -> None:
        """Метод записи переданных данных в файл (CSV)."""

    def read_file_csv(self, path_to_file: str) -> list[dict[str, str | int | float | None]]:
        """Метод чтения данных из файла (CSV)."""
        pass

    def add_info_file_csv(self, airplane: Airplane, path_to_file: str) -> None:
        """Метод добавления информации о самолете в файл (CSV)."""
        pass

    def delete_info_file_csv(self, callsign: str, path_to_file: str) -> None:
        """Метод удаления информации о самолете по переданному позывному (callsign)."""
        pass


if __name__ == "__main__":
    path_dir_data = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    print(path_dir_data)

    # /Users/vadimsemenov/PycharmProjects/Airplane_Tracker_App/data

    air = FileManagerCSV()
