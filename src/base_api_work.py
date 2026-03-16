from abc import ABC, abstractmethod

class BaseApiWork(ABC):
    """ Базовый класс для работы с API сервисами """
    param: str | dict[str, str]

    @abstractmethod
    def get_response_api(self, param: str | dict) -> None:
        """ Абстрактный метод, для получения ответа от API сервиса. """
        pass