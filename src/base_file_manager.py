from abc import ABC, abstractmethod

import pandas as pd

from src.airplane import Airplane


class BaseFileManagerJSON(ABC):
    """Базовый класс для работы с данными о самолетах в формате JSON."""

    def __init__(self, filename: str = "data.json") -> None:
        """Метод инициализации с приватным атрибутом __filename"""
        self._filename = filename

    @abstractmethod
    def save_to_file(self, airplanes: list[Airplane], path_to_save: str | None = None) -> None:
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

    def __init__(self, filename: str = "data.csv") -> None:
        """Метод инициализации с приватным атрибутом _filename"""
        self._filename = filename

    @abstractmethod
    def save_to_file(self, airplanes: list[Airplane], path_to_save: str | None = None) -> None:
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


class BaseFileManagerEXCEL(ABC):
    """Базовый класс для работы с данными о самолетах в формате EXCEL."""

    def __init__(self, filename: str = "data.xlsx") -> None:
        """Метод инициализации с приватным атрибутом _filename"""
        self._filename = filename

    @abstractmethod
    def save_to_file(self, airplanes: list[Airplane], path_to_save: str | None = None) -> None:
        """Метод записи переданных данных в файл (EXCEL)."""
        pass

    @abstractmethod
    def read_file_excel(self, path_to_file: str) -> pd.DataFrame:
        """Метод чтения данных из файла (EXCEL)."""
        pass

    @abstractmethod
    def add_info_file_excel(self, airplane: list[Airplane], path_to_file: str) -> None:
        """Метод добавления информации о самолете в файл (EXCEL)."""
        pass

    @abstractmethod
    def delete_info_file_excel(self, callsign: str, path_to_file: str) -> None:
        """Метод удаления информации о самолете по переданному позывному (callsign)."""
        pass
