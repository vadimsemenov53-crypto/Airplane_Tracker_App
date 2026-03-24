from abc import ABC, abstractmethod

import pandas as pd

from src.airplane import Airplane


class BaseFileManagerJSON(ABC):
    """Базовый класс для работы с данными о самолетах в формате JSON."""

    @abstractmethod
    def save_to_json_file(self, airplanes: list[Airplane], path_to_save: str) -> None:
        """Метод записи переданных данных в файл (JSON)."""
        pass

    @abstractmethod
    def read_file_json(self, path_to_file: str) -> list[dict[str, str | int | float | None]]:
        """Метод чтения данных из файла (JSON)."""
        pass

    @abstractmethod
    def add_info_file_json(self, airplanes: list[Airplane], path_to_file: str) -> None:
        """Метод добавления информации о самолете в файл (JSON)."""
        pass

    @abstractmethod
    def delete_info_file_json(self, callsign: str, path_to_file: str) -> None:
        """Метод удаления информации о самолете по переданному позывному (callsign)."""
        pass


class BaseFileManagerCSV(ABC):
    """Базовый класс для работы с данными о самолетах в формате CSV."""

    @abstractmethod
    def save_to_csv_file(self, airplanes: list[Airplane], path_to_save: str) -> None:
        """Метод записи переданных данных в файл (CSV)."""
        pass

    @abstractmethod
    def read_file_csv(self, path_to_file: str) -> pd.DataFrame:
        """Метод чтения данных из файла (CSV)."""
        pass

    @abstractmethod
    def add_info_file_csv(self, airplane: list[Airplane], path_to_file: str) -> None:
        """Метод добавления информации о самолете в файл (CSV)."""
        pass

    @abstractmethod
    def delete_info_file_csv(self, callsign: str, path_to_file: str) -> None:
        """Метод удаления информации о самолете по переданному позывному (callsign)."""
        pass

class BaseFileManagerEXECL(ABC):
        """Базовый класс для работы с данными о самолетах в формате EXECL."""

        @abstractmethod
        def save_to_execl_file(self, airplanes: list[Airplane], path_to_save: str) -> None:
            """Метод записи переданных данных в файл (EXECL)."""
            pass

        @abstractmethod
        def read_file_execl(self, path_to_file: str) -> pd.DataFrame:
            """Метод чтения данных из файла (EXECL)."""
            pass

        @abstractmethod
        def add_info_file_execl(self, airplane: list[Airplane], path_to_file: str) -> None:
            """Метод добавления информации о самолете в файл (EXECL)."""
            pass

        @abstractmethod
        def delete_info_file_execl(self, callsign: str, path_to_file: str) -> None:
            """Метод удаления информации о самолете по переданному позывному (callsign)."""
            pass
