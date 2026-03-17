from src.base_designer_airplane import BaseDesignerAirplane
from src.api import APICoordinates, APIAircraft

class DesignerAirplane(BaseDesignerAirplane):
    """ Класс для работы с информацией о самолетах. """

    def __init__(self, _data: dict | list = None):
        """Метод - конструктор, для инициализации объектов класса."""
        if _data is None:
            raise ValueError('Данные пустые или не переданы.')

        self._data = _data
        self._result_data: list[dict] = []

    def get_report_json(self) -> list[dict]:
        """ Метод для формирования отчета JSON. """
        for airline in self._data["states"]:
            if airline:
                self._result_data.append({
                    'country' : airline[2],
                    'callsign' : airline[1],
                    'velocity' : airline[9],
                    'vertical_rate' : airline[11],
                    'bar_altitude' : airline[7]
                })
        return self._result_data


if __name__ == '__main__':
    api = APICoordinates()
    api.get_response_api('Spain')
    api.get_coordinates()

    api_2 = APIAircraft()
    api_2.get_response_api(api._coordinates)
    print(api_2._aeroplanes)
    data = api_2._aeroplanes

    ex_1 = DesignerAirplane(data)
    result = ex_1.get_report_json()
    print(result)
