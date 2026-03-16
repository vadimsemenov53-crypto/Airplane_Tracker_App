from src.base_api_work import BaseApiWork

class APICoordinates(BaseApiWork):
    """ Класс, для обращения к внешнему сервису для получения координат страны. """

    def __init__(self) -> None:
        """ Метод - конструктор, для инициализации объектов класса. """
        self.url = 'https://nominatim.openstreetmap.org/search'
        self.coordinates = None
        self.data_response = None


    def get_response_api(self, country: str) -> None:
        """ Метод обращения к внешнему API и получения координат квадрата переданной страны. """
        #Headers с user-agent - обязательный параметр при запросе к nominatim.openstreetmap.
        #Вы можете использовать любое название вместо test-app/1.0, например просто test-app.
        headers_nominatim = {
            'User-Agent': 'test-app/1.0',
        }

        #Указываем параметры: в каком формате возвращать данные и максимальную длину списка стран в ответе.
        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': 1,
        }

        self.data_response = self.make_request(self.url, params_nominatim, headers_nominatim)


    def get_coordinates(self) -> None:
        """ Метод, для получения координат из JSON-ответа от API сервиса """
        #Пример ответа от nominatim.openstreetmap можно посмотреть в задании курсовой.
        if not self.data_response:
            raise ValueError('Полученные данные пустые.')

        geo_coordinates = self.data_response[0].get('boundingbox')

        #Параметры для фильтрации самолетов по их географическим координатам.
        self.coordinates = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3],
        }


class APIAircraft(BaseApiWork):
    """ Класс, для обращения к внешнему сервису для получения информации о самолетах которые находятся
    в квадрате координат. """
    coordinates: dict[str, str]
    aeroplanes: dict | None


    def __init__(self) -> None:
        """ Метод - конструктор, для инициализации объектов класса. """
        self.url = 'https://opensky-network.org/api/states/all?'
        self.aeroplanes = None


    def get_response_api(self, coordinates: dict[str, str]) -> None:
        """ Метод обращения к внешнему API и получения информации о самолетах. """

        self.aeroplanes = self.make_request(self.url, params=coordinates)
