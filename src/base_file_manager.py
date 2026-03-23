from abc import ABC, abstractmethod

from src.airplane import Airplane
from src.airplane_json import AirplaneJSON


class BaseFileManagerJSON(ABC):
    """Базовый класс для работы с данными о самолетах в формате JSON."""

    @abstractmethod
    def save_to_json_file(self, data: list[dict[str, str | int | float | None]], path_to_save: str) -> None:
        """Метод записи переданных данных в файл (JSON)."""
        pass

    @abstractmethod
    def read_file_json(self, path_to_file: str) -> list[dict[str, str | int | float | None]]:
        """Метод чтения данных из файла (JSON)."""
        pass

    @abstractmethod
    def add_info_file_json(self, airplane: AirplaneJSON, path_to_file: str) -> None:
        """Метод добавления информации о самолете в файл (JSON)."""
        pass

    @abstractmethod
    def delete_info_file_json(self, callsign: str, path_to_file: str) -> None:
        """Метод удаления информации о самолете по переданному позывному (callsign)."""
        pass


class BaseFileManagerCSV(ABC):
    """Базовый класс для работы с данными о самолетах в формате CSV."""

    @abstractmethod
    def save_to_csv_file(self, data: list[dict[str, str | int | float | None]], path_to_save: str) -> None:
        """Метод записи переданных данных в файл (CSV)."""
        pass

    @abstractmethod
    def read_file_csv(self, path_to_file: str) -> list[dict[str, str | int | float | None]]:
        """Метод чтения данных из файла (CSV)."""
        pass

    @abstractmethod
    def add_info_file_csv(self, airplane: Airplane, path_to_file: str) -> None:
        """Метод добавления информации о самолете в файл (CSV)."""
        pass

    @abstractmethod
    def delete_info_file_csv(self, callsign: str, path_to_file: str) -> None:
        """Метод удаления информации о самолете по переданному позывному (callsign)."""
        pass

    # @abstractmethod
    # def save_to_csv_file(self):
    #     pass
    #
    # @abstractmethod
    # def save_to_execl_file(self):
    #     pass
