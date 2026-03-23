import pandas as pd
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

    def save_to_csv_file(self, airplanes: list[Airplane], path_to_save: str) -> None:
        """Метод записи переданных данных в файл (CSV)."""
        if not airplanes:
            raise ValueError("Переданы пустые данные.")

        if os.path.isdir(path_to_save):
            path_to_save = os.path.join(path_to_save, "data.csv")

        os.makedirs(os.path.dirname(path_to_save), exist_ok=True)

        df = pd.DataFrame([air.get_dict_from_airplane() for air in airplanes])

        try:
            df.to_csv(path_to_save, index=False)

        except OSError as e:
            raise RuntimeError(f"Ошибка записи: {e}") from e

    def read_file_csv(self, path_to_file: str) -> list[dict[str, str | int | float | None]]:
        """Метод чтения данных из файла (CSV)."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Файл не найден: {path}")

        df = pd.read_csv(path_to_file)
        return df.to_dict(orient='records')

    def add_info_file_csv(self, airplane: Airplane, path_to_file: str) -> None:
        """Метод добавления информации о самолете в файл (CSV)."""
        pass

    def delete_info_file_csv(self, callsign: str, path_to_file: str) -> None:
        """Метод удаления информации о самолете по переданному позывному (callsign)."""
        pass


if __name__ == "__main__":
    path_dir_data = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    print(path_dir_data)
    airplane1 = Airplane('Germany', '2222', 222, 33, 5555)
    airplane2 = Airplane('Germany', '2222', 222, 33, 5555)
    data_1 = [airplane1, airplane2]

    path = "/Users/vadimsemenov/PycharmProjects/Airplane_Tracker_App/data/data.csv"

    air11 = FileManagerCSV()

    print(air11.read_file_csv(path))
