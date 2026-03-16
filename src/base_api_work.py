from abc import ABC, abstractmethod
from typing import Any

import requests
from requests.exceptions import HTTPError, RequestException


class BaseApiWork(ABC):
    """Базовый класс для работы с API сервисами"""

    @staticmethod
    def _make_request(url: str, params: Any, headers: dict[str, str] | None = None) -> dict | list:
        """Приватный метод подключения к API.
        Отправляет запрос, проверяет статус-код и возвращает JSON."""

        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()

        except HTTPError as e:
            raise RuntimeError(f"Ошибка HTTP: {e}") from e
        except RequestException as e:
            raise RuntimeError(f"Ошибка RequestException: {e}") from e

        try:
            data: dict | list = response.json()
            return data
        except ValueError as e:
            raise RuntimeError(f"Ошибка JSON: {e}") from e

    @abstractmethod
    def get_response_api(self, param: str | dict[str, str]) -> None:
        """Абстрактный метод, для получения ответа от API сервиса."""
        pass
