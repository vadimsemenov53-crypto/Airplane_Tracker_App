from abc import ABC, abstractmethod

class BaseFileManagerJSON(ABC):
    """ Базовый класс для работы с данными о самолетах в формате JSON. """

    @abstractmethod
    def _save_to_json_file(self, data, path_to_save: str):
        pass

    # @abstractmethod
    # def _read_file_json(self):
    #     pass
    #
    # @abstractmethod
    # def _add_info_file_json(self):
    #     pass
    #
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
