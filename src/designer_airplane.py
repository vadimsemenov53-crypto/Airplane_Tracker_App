from src.base_designer_airplane import BaseDesignerAirplane

class DesignerAirplane(BaseDesignerAirplane):
    """ Класс для работы с информацией о самолетах и формирования структуры отчета. """

    def __init__(self, _data: dict | list = None):
        """Метод - конструктор, для инициализации объектов класса."""
        if _data is None or not _data:
            raise ValueError('Данные пустые или не переданы.')

        self._data = _data


    def _get_report(self) -> list[dict]:
        """ Метод для формирования отчета. """
        if not self._data or "states" not in self._data:
            raise ValueError("Некорректные данные API.")

        self._result_data: list[dict] = []

        for airline in self._data["states"]:
            if airline:
                self._result_data.append({
                    'country' : airline[2],
                    'callsign' : airline[1],
                    'velocity' : self._save_number(airline[9]),
                    'vertical_rate' : self._save_number(airline[11]),
                    'bar_altitude' : self._save_number(airline[7])
                })
        return self._result_data

    @staticmethod
    def _save_number(value: int | float | None) -> float:
        """ Приватный метод, для фильтрации значений скорости и высоты. """
        return float(value) if isinstance(value, (int, float)) else 0.0


    def _filtered_velocity(self) -> list[dict]:
        """ Метод - фильтрация самолетов по скорости(убывание). """
        return sorted(
            self._result_data,
            key=lambda x: x['velocity'],
            reverse=True
        )


    def _filtered_bar_altitude(self):
        """ Метод - фильтрация самолетов по высоте. """
        return sorted(
            self._result_data,
            key=lambda x: x['bar_altitude'],
            reverse=True
        )
