import requests
from requests.exceptions import HTTPError, RequestException
from abc import ABC, abstractmethod

class BaseApiWork(ABC):
    """ Базовый класс для работы с API сервисами """

    @staticmethod
    def _make_request(url, params, headers=None) -> dict | list:
        """ Приватный метод подключения к API.
        Отправляет запрос, проверяет статус-код и возвращает JSON. """

        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()

        except HTTPError as e:
            raise RuntimeError(f'Ошибка HTTP: {e}') from e
        except RequestException as e:
            raise RuntimeError(f'Ошибка запроса к API: {e}') from e

        try:
            return response.json()
        except ValueError as e:
            raise RuntimeError(f'Ошибка JSON: {e}') from e

    @abstractmethod
    def get_response_api(self, param: str | dict) -> None:
        """ Абстрактный метод, для получения ответа от API сервиса. """
        pass