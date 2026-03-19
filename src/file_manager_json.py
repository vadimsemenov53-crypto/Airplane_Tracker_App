import json
import os
from src.base_file_manager import BaseFileManagerJSON

class FileManagerJson(BaseFileManagerJSON):
    """ Класс для работы с данными в формате JSON.
     Основные функции:
     1. Запись переданных данных в файл (требуется передать путь для записи файла).
     2. Чтение данных файла (требуется передать путь).
     3. Добавление данных в файл (требуется передать путь до файла и данные о самолете).
     4. Удаление данных о самолете из файла (требуется передать путь до файла и
     передать словарь с критериями.)"""

    def _save_to_json_file(self, data, path_to_save: str):
        """ Приватный метод записи переданных данных в файл. """
        if not data:
            raise ValueError('Переданы пустые данные.')

        with open(path_to_save, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False, default=str)

if __name__ == '__main__':
    path_base = os.path.dirname(os.path.dirname(__file__))
    path_save = os.path.join(path_base, 'data')
    print(path_save)

    ex_1 = FileManagerJson()
    data = {
        "time": 1766142246,
        "states": [
            [
                "4b1812",
                "SWR438A ",
                "Switzerland",
                1766166618,
                1766166618,
                -0.0168,
                51.0888,
                4267.2,
                False,
                189.7,
                129.39,
                14.63,
                0,
                4282.44,
                "2061",
                False,
                0,
            ],
        ],
    }
    ex_1._save_to_json_file(data, '/Users/vadimsemenov/PycharmProjects/Airplane_Tracker_App/data')