from abc import ABC, abstractmethod


class BaseDesignerAirplane(ABC):
    """Базовый класс, для сбора информации о самолетах."""

    @abstractmethod
    def _get_report(self) -> list[dict]:
        """Метод для формирования отчета."""
        pass

    @abstractmethod
    def _filtered_velocity(self) -> list[dict]:
        """Метод - фильтрация самолетов по скорости."""
        pass

    @abstractmethod
    def _filtered_bar_altitude(self) -> list[dict]:
        """Метод - фильтрация самолетов по высоте."""
        pass
