import json
import os
from json import JSONDecodeError
from src.airplane import Airplane

from src.base_file_manager import BaseFileManagerJSON

class FileManagerJson(BaseFileManagerJSON):
    """ Класс для работы с данными в формате JSON.
     Основные функции:
     1. Запись переданных данных в файл (требуется передать путь для записи файла).
     2. Чтение данных файла (требуется передать путь).
     3. Добавление данных в файл (требуется передать путь до файла и данные о самолете).
     4. Удаление данных о самолете из файла (требуется передать путь до файла и
     передать словарь с критериями.)"""

    def save_to_json_file(self, data: dict | list, path_to_save: str) -> None:
        """ Метод записи переданных данных в файл (JSON). """
        if not data:
            raise ValueError('Переданы пустые данные.')

        os.makedirs(os.path.dirname(path_to_save), exist_ok=True)

        try:
            with open(path_to_save, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False, default=str)

        except OSError as e:
            raise RuntimeError(f'Ошибка записи: {e}') from e

    def read_file_json(self, path_to_file: str) -> str:
        """ Метод чтения данных из файла (JSON). """
        try:
            with open(path_to_file, 'r', encoding='utf-8') as file:
                return json.load(file)

        except FileNotFoundError as e:
            raise FileNotFoundError(f'Файл не найден: {e}')

        except JSONDecodeError as e:
            raise RuntimeError(f'Ошибка JSON: {e}') from e


    def add_info_file_json(self, data: dict[str, str | int | float | None], path_to_file: str) -> None:
        """ Метод добавления информации о самолете в файл (JSON). """
        try:
            with open(path_to_file, 'r', encoding='utf-8') as file:
                data_file = json.load(file)

        except FileNotFoundError as e:
            raise FileNotFoundError(f'Файл не найден: {e}')

        data_file.append(data)

        try:
            with open(path_to_file, 'w', encoding='utf-8') as file:
                json.dump(data_file, file, indent=2, ensure_ascii=False, default=str)

        except OSError as e:
            raise RuntimeError(f'Ошибка записи: {e}') from e



if __name__ == '__main__':
    path_base = os.path.dirname(os.path.dirname(__file__))
    path_save = os.path.join(path_base, 'data/example_1.json')
    print(path_save)

    ex_1 = FileManagerJson()
    data = [{
                        "country": "Germany",
                        "callsign": "ECA4RT",
                        "velocity": 123,
                        "vertical_rate": 455,
                        "bar_altitude": 346346,
                    }]
    print(ex_1.read_file_json('/Users/vadimsemenov/PycharmProjects/Airplane_Tracker_App/data/example_1.json'))