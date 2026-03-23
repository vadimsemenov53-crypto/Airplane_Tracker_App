from abc import ABC, abstractmethod
from src.airplane import Airplane


class BaseDesignerAirplane(ABC):
    """Базовый класс, для сбора информации о самолетах."""

    @abstractmethod
    def _get_report(self) -> list[Airplane]:
        """Метод для формирования отчета."""
        pass

    @abstractmethod
    def _filtered_velocity(self) -> list[Airplane]:
        """Метод - фильтрация самолетов по скорости."""
        pass

    @abstractmethod
    def _filtered_bar_altitude(self) -> list[Airplane]:
        """Метод - фильтрация самолетов по высоте."""
        pass
