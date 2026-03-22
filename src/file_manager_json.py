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

    def save_to_json_file(self, data: list[dict[str, str | int | float | None]], path_to_save: str) -> None:
        """ Метод записи переданных данных в файл (JSON). """
        if not data:
            raise ValueError('Переданы пустые данные.')

        if os.path.isdir(path_to_save):
            path_to_save = os.path.join(path_to_save, "data.json")

        os.makedirs(os.path.dirname(path_to_save), exist_ok=True)

        try:
            with open(path_to_save, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False, default=str)

        except OSError as e:
            raise RuntimeError(f'Ошибка записи: {e}') from e

    def read_file_json(self, path_to_file: str) -> list[dict[str, str | int | float | None]]:
        """ Метод чтения данных из файла (JSON). """
        try:
            with open(path_to_file, 'r', encoding='utf-8') as file:
                return json.load(file)

        except FileNotFoundError as e:
            raise FileNotFoundError(f'Файл не найден: {path_to_file}') from e

        except JSONDecodeError as e:
            raise RuntimeError(f'Ошибка JSON: {e}') from e


    def add_info_file_json(self, airplane: Airplane, path_to_file: str) -> None:
        """ Метод добавления информации о самолете в файл (JSON). """
        data = airplane.get_dict_from_airplane()

        data_file = self.read_file_json(path_to_file)

        if not isinstance(data_file, list):
            raise TypeError("Файл должен содержать список объектов")

        if data not in data_file:
            data_file.append(data)

        self.save_to_json_file(data_file, path_to_file)


    def delete_info_file_json(self, callsign: str, path_to_file: str) -> None:
        """ Метод удаления информации о самолете по переданному позывному (callsign). """
        data_file = self.read_file_json(path_to_file)

        if not isinstance(data_file, list):
            raise TypeError("Файл должен содержать список объектов")

        data_file = [air for air in data_file if air.get('callsign') != callsign]

        self.save_to_json_file(data_file, path_to_file)


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
    # print(ex_1.save_to_json_file(data, '/Users/vadimsemenov/PycharmProjects/Airplane_Tracker_App/data/example_1.json'))

    air_1 = Airplane("Spain1111", "LVL2604", 309.77, 0, 11582.4)
    ex_1.delete_info_file_json("LVL2604",
                            '/Users/vadimsemenov/PycharmProjects/Airplane_Tracker_App/data/example_1.json')
