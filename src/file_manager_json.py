import json
import os
from json import JSONDecodeError
from typing import cast

from src.airplane import Airplane
from src.base_file_manager import BaseFileManagerJSON


class FileManagerJson(BaseFileManagerJSON):
    """Класс для работы с данными в формате JSON.
    Основные функции:
    1. Запись переданных данных в файл (требуется передать путь для записи файла).
    2. Чтение данных файла (требуется передать путь).
    3. Добавление данных в файл (требуется передать путь до файла и данные о самолете).
    4. Удаление данных о самолете из файла (требуется передать путь до файла и
    передать словарь с критериями.)"""

    def save_to_json_file(self, data: list[dict[str, str | int | float | None]], path_to_save: str) -> None:
        """Метод записи переданных данных в файл (JSON)."""
        if not data:
            raise ValueError("Переданы пустые данные.")

        if os.path.isdir(path_to_save):
            path_to_save = os.path.join(path_to_save, "data.json")

        os.makedirs(os.path.dirname(path_to_save), exist_ok=True)

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

    def add_info_file_json(self, airplane: Airplane, path_to_file: str) -> None:
        """Метод добавления информации о самолете в файл (JSON)."""
        data = airplane.get_dict_from_airplane()

        data_file = self.read_file_json(path_to_file)

        self._ensure_list(data_file)

        if data not in data_file:
            data_file.append(data)

        self.save_to_json_file(data_file, path_to_file)

    def delete_info_file_json(self, callsign: str, path_to_file: str) -> None:
        """Метод удаления информации о самолете по переданному позывному (callsign)."""
        data_file = self.read_file_json(path_to_file)

        self._ensure_list(data_file)

        data_file = [air for air in data_file if air.get("callsign") != callsign]

        self.save_to_json_file(data_file, path_to_file)
