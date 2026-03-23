import json
import os
from json import JSONDecodeError
from typing import cast

from src.airplane import Airplane
from src.base_file_manager import BaseFileManagerJSON

# from src.api import APICoordinates, APIAircraft
# from src.designer_airplane import DesignerAirplane


class FileManagerJson(BaseFileManagerJSON):
    """Класс для работы с данными в формате JSON.
    Основные функции:
    1. Запись переданных данных в файл (требуется передать путь для записи файла).
    2. Чтение данных файла (требуется передать путь).
    3. Добавление данных в файл (требуется передать путь до файла и данные о самолете).
    4. Удаление данных о самолете из файла (требуется передать путь до файла и
    передать словарь с критериями.)"""

    def save_to_json_file(self, airplanes: list[Airplane], path_to_save: str) -> None:
        """Метод записи переданных данных в файл (JSON)."""
        if not airplanes:
            raise ValueError("Переданы пустые данные.")

        if os.path.isdir(path_to_save):
            path_to_save = os.path.join(path_to_save, "data.json")

        os.makedirs(os.path.dirname(path_to_save), exist_ok=True)

        data = [air.get_dict_from_airplane() for air in airplanes]

        try:
            with open(path_to_save, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2, ensure_ascii=False, default=str)

        except OSError as e:
            raise RuntimeError(f"Ошибка записи: {e}") from e

    def read_file_json(self, path_to_file: str) -> list[dict[str, str | int | float | None]]:
        """Метод чтения данных из файла (JSON)."""
        try:
            with open(path_to_file, "r", encoding="utf-8") as file:
                data_list = json.load(file)

            return cast(list[dict[str, str | int | float | None]], data_list)

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Файл не найден: {path_to_file}") from e

        except JSONDecodeError as e:
            raise RuntimeError(f"Ошибка JSON: {e}") from e

    @staticmethod
    def _ensure_list(data: list[dict]) -> list[dict]:
        """Приветный метод валидации данных.
        Если передан список словарей -> возвращаем.
        Иначе -> ошибка."""
        if not isinstance(data, list):
            raise ValueError("Файл должен содержать список объектов.")
        return data

    def add_info_file_json(self, airplanes: list[Airplane], path_to_file: str) -> None:
        """Метод добавления информации о самолете в файл (JSON)."""
        new_data = [air.get_dict_from_airplane() for air in airplanes]

        data_file = self.read_file_json(path_to_file)

        self._ensure_list(data_file)

        for item in new_data:
            if item not in data_file:
                data_file.append(item)

        save_data = [Airplane(**item) for item in data_file]

        self.save_to_json_file(save_data, path_to_file)

    def delete_info_file_json(self, callsign: str, path_to_file: str) -> None:
        """Метод удаления информации о самолете по переданному позывному (callsign)."""
        data_file = self.read_file_json(path_to_file)

        self._ensure_list(data_file)

        data_file = [Airplane(**air) for air in data_file if air.get("callsign") != callsign]

        self.save_to_json_file(data_file, path_to_file)

# if __name__ == "__main__":
#     path = "/Users/vadimsemenov/PycharmProjects/Airplane_Tracker_App/data/data.json"
#
#     api_1 = APICoordinates()
#     api_1.get_response_api('Spain')
#     api_1.get_coordinates()
#
#     api_2 = APIAircraft()
#     api_2.get_response_api(api_1._coordinates)
#     print(api_2._aeroplanes)
#
#     data_air = api_2._aeroplanes
#
#     designer = DesignerAirplane(data_air)
#     report = designer._get_report()
#     print(report)
#
#     file_csv = FileManagerJson()
#     file_csv.save_to_json_file(report, path)