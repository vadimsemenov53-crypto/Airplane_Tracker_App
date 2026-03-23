from src.base_designer_airplane import BaseDesignerAirplane
from src.airplane import Airplane


class DesignerAirplane(BaseDesignerAirplane):
    """Класс для работы с информацией о самолетах и формирования структуры отчета."""

    def __init__(self, _data: dict[str, list] | None = None):
        """Метод - конструктор, для инициализации объектов класса."""
        if _data is None or not _data:
            raise ValueError("Данные пустые или не переданы.")

        self._data = _data

    def _get_report(self) -> list[Airplane]:
        """Метод для формирования отчета."""
        if not self._data or "states" not in self._data:
            raise ValueError("Некорректные данные API.")

        self._result_data: list[Airplane] = []

        for airline in self._data["states"]:
            if airline:
                airline = Airplane(
                    airline[2],
                    airline[1],
                    self._save_number(airline[9]),
                    self._save_number(airline[11]),
                    self._save_number(airline[7]),
                )
                self._result_data.append(airline)
        return self._result_data

    @staticmethod
    def _save_number(value: int | float | None) -> float:
        """Приватный метод, для фильтрации значений скорости и высоты."""
        return float(value) if isinstance(value, (int, float)) else 0.0

    def _filtered_velocity(self) -> list[Airplane]:
        """Метод - фильтрация самолетов по скорости(убывание)."""
        return sorted(self._result_data, key=lambda x: x.velocity, reverse=True)

    def _filtered_bar_altitude(self) -> list[Airplane]:
        """Метод - фильтрация самолетов по высоте."""
        return sorted(self._result_data, key=lambda x: x.bar_altitude, reverse=True)
