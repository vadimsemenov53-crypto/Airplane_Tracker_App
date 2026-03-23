import pandas as pd
import os

from src.airplane_table import AirplaneTable
from src.base_file_manager import BaseFileManagerCSV


class FileManagerCSV(BaseFileManagerCSV):
    """Класс для работы с данными в формате CSV.
    Основные функции:
    1. Запись переданных данных в файл (требуется передать путь для записи файла).
    2. Чтение данных файла (требуется передать путь).
    3. Добавление данных в файл (требуется передать путь до файла и данные о самолете).
    4. Удаление данных о самолете из файла (требуется передать путь до файла и
    передать словарь с критериями.)"""

    def save_to_csv_file(self, data: pd.DataFrame, path_to_save: str) -> None:
        """Метод записи переданных данных в файл (CSV)."""
        if not data:
            raise ValueError("Переданы пустые данные.")

        if os.path.isdir(path_to_save):
            path_to_save = os.path.join(path_to_save, "data.csv")

        os.makedirs(os.path.dirname(path_to_save), exist_ok=True)

        try:
            data.to_csv(path_to_save, index=False, encoding="utf-8", sep=",")

        except OSError as e:
            raise RuntimeError(f"Ошибка записи: {e}") from e

    def read_file_csv(self, path_to_file: str) -> list[dict[str, str | int | float | None]]:
        """Метод чтения данных из файла (CSV)."""
        pass

    def add_info_file_csv(self, airplane: AirplaneTable, path_to_file: str) -> None:
        """Метод добавления информации о самолете в файл (CSV)."""
        pass

    def delete_info_file_csv(self, callsign: str, path_to_file: str) -> None:
        """Метод удаления информации о самолете по переданному позывному (callsign)."""
        pass


if __name__ == "__main__":
    path_dir_data = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    print(path_dir_data)
    airplane = AirplaneTable('Germany', '2222', 222, 33, 5555)
    data_1 = airplane.get_table_from_airplane()

    path = "/Users/vadimsemenov/PycharmProjects/Airplane_Tracker_App/data"

    air = FileManagerCSV()


    air.save_to_csv_file(data_1, path)
