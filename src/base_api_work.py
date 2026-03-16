import requests
from abc import ABC, abstractmethod

class BaseApiWork(ABC):
    """ Базовый класс для работы с API сервисами """

    def make_request(self, url, params, headers=None) -> str:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        return response.json()

    @abstractmethod
    def get_response_api(self, param: str | dict) -> None:
        """ Абстрактный метод, для получения ответа от API сервиса. """
        pass