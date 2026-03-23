from src.airplane import Airplane

class AirplaneTable(Airplane):
    """ Подкласс Airplane, для подготовки таблиц и дальнейшей работы с CSV & EXECL форматами. """

    def get_dict_from_airplane(self) -> list[list[str | float]]:
        """ Метод для сбора данных и формирования таблицы """
        headers = ["Country", "Callsign", "Velocity", "Vertical Rate", "Bar Altitude"]
        row = [self.country, self.callsign, self.velocity, self.vertical_rate, self.bar_altitude]

        return [headers, row]