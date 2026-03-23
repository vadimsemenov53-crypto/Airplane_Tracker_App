from src.airplane import Airplane


class AirplaneJSON(Airplane):
    """Подкласс Airplane, для формирования словаря JSON"""

    def get_dict_from_airplane(self) -> dict[str, str | int | float | None]:
        """Метод для формирования словаря для дальнейшего взаимодействия с данными."""
        return {
            "country": self.country,
            "callsign": self.callsign,
            "velocity": self.velocity,
            "vertical_rate": self.vertical_rate,
            "bar_altitude": self.bar_altitude,
        }
