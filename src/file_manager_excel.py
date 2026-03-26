import os

import pandas as pd

from src.airplane import Airplane
from src.base_file_manager import BaseFileManagerEXCEL
from src.utils import airplanes_to_dicts, ensure_directory

# from src.api import APICoordinates, APIAircraft
# from src.designer_airplane import DesignerAirplane


class FileManagerEXCEL(BaseFileManagerEXCEL):
    """Класс для работы с данными в формате xlsx.
    Основные функции:
    1. Запись переданных данных в файл (требуется передать путь для записи файла).
    2. Чтение данных файла (требуется передать путь).
    3. Добавление данных в файл (требуется передать путь до файла и данные о самолете).
    4. Удаление данных о самолете из файла (требуется передать путь до файла и
    передать словарь с критериями.)"""

    def save_to_excel_file(self, airplanes: list[Airplane], path_to_save: str | None = None) -> None:
        """Метод записи переданных данных в файл (EXCEL)."""
        if not airplanes:
            raise ValueError("Переданы пустые данные.")

        if not path_to_save:
            data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
            path_to_save = os.path.join(data_dir, self._filename)

        if os.path.isdir(path_to_save):
            path_to_save = os.path.join(path_to_save, "data.xlsx")

        ensure_directory(path_to_save)

        df = pd.DataFrame(airplanes_to_dicts(airplanes))

        try:
            df.to_excel(path_to_save, index=False)

        except OSError as e:
            raise RuntimeError(f"Ошибка записи: {e}") from e

    def read_file_excel(self, path_to_file: str) -> pd.DataFrame:
        """Метод чтения данных из файла (EXCEL)."""
        if not os.path.exists(path_to_file):
            raise FileNotFoundError(f"Файл не найден: {path_to_file}")

        return pd.read_excel(path_to_file)

    def add_info_file_excel(self, airplane: list[Airplane], path_to_file: str) -> None:
        """Метод добавления информации о самолете в файл (EXCEL)."""
        new_df = pd.DataFrame(airplanes_to_dicts(airplane))

        df = self.read_file_excel(path_to_file)

        combined_df = pd.concat([df, new_df], ignore_index=True)
        combined_df = combined_df.drop_duplicates()

        try:
            combined_df.to_excel(path_to_file, index=False)

        except OSError as e:
            raise RuntimeError(f"Ошибка записи: {e}") from e

    def delete_info_file_excel(self, callsign: str, path_to_file: str) -> None:
        """Метод удаления информации о самолете по переданному позывному (callsign)."""
        df = self.read_file_excel(path_to_file)

        df = df[df["callsign"] != callsign]

        try:
            df.to_excel(path_to_file, index=False)

        except OSError as e:
            raise RuntimeError(f"Ошибка записи: {e}") from e


# if __name__ == "__main__":
#     path = "/Users/vadimsemenov/PycharmProjects/Airplane_Tracker_App/data/data.xlsx"
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
#     report_filter_bar = designer._filtered_bar_altitude()
#     print(report)
#     print(report_filter_bar)
#
#     file_excel = FileManagerEXCEL()
#     file_excel.save_to_excel_file(report_filter_bar, path)
