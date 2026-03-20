from abc import ABC, abstractmethod

class BaseFileManagerJSON(ABC):
    """ Базовый класс для работы с данными о самолетах в формате JSON. """

    @abstractmethod
    def save_to_json_file(self, data: dict[str, str | int | float | None], path_to_save: str) -> None:
        """ Метод записи переданных данных в файл (JSON). """
        pass

    @abstractmethod
    def read_file_json(self, path_to_file: str) -> list[dict[str, str | int | float | None]]:
        """ Метод чтения данных из файла (JSON). """
        pass

    @abstractmethod
    def add_info_file_json(self, data: dict[str, str | int | float | None], path_to_file: str) -> None:
        """ Метод добавления информации о самолете в файл (JSON). """
        pass

    # @abstractmethod
    # def _delete_info_file_json(self):
    #     pass

    # @abstractmethod
    # def save_to_csv_file(self):
    #     pass
    #
    # @abstractmethod
    # def save_to_execl_file(self):
    #     pass
