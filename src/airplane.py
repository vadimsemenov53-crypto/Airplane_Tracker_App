class Airplane:
    """Класс отдельного самолета с атрибутами и методами валидации."""

    __slots__ = ("country", "callsign", "velocity", "vertical_rate", "bar_altitude")

    def __init__(self, country: str, callsign: str, velocity: float, vertical_rate: float, bar_altitude: float):
        """Метод - конструктор, для инициализации объектов класса."""
        self.country = country
        self.callsign = callsign
        self.velocity = velocity
        self.vertical_rate = vertical_rate
        self.bar_altitude = bar_altitude

    @staticmethod
    def _validate_velocity(velocity: float) -> float:
        """Приватный метод валидации данных (скорость)."""
        if velocity is None or not isinstance(velocity, int | float):
            return 0
        return velocity

    @staticmethod
    def _validate_bar_altitude(bar_altitude: float) -> float:
        """Приватный метод валидации данных (скорость)."""
        if bar_altitude is None or not isinstance(bar_altitude, int | float):
            return 0
        return bar_altitude

    def __repr__(self) -> str:
        """Метод отладки, для разработчика"""
        return f"Airplane: {self.callsign}, {self.country}" f"Velocity: {self.velocity}, Bar_A: {self.bar_altitude}"

    def __lt__(self, other: "Airplane") -> bool:
        """Метод сравнения высот двух самолетов (Air_1 < Air_2)."""
        return self.bar_altitude < other.bar_altitude

    def __gt__(self, other: "Airplane") -> bool:
        """Метод сравнения высот двух самолетов (Air_1 > Air_2)."""
        return self.bar_altitude > other.bar_altitude

    def __le__(self, other: "Airplane") -> bool:
        """Метод сравнения высот двух самолетов (Air_1 <= Air_2)."""
        return self.bar_altitude <= other.bar_altitude

    def __ge__(self, other: "Airplane") -> bool:
        """Метод сравнения высот двух самолетов (Air_1 >= Air_2)."""
        return self.bar_altitude >= other.bar_altitude

    def __eq__(self, other: object) -> bool:
        """Метод сравнения высот двух самолетов (Air_1 == Air_2)."""
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.bar_altitude == other.bar_altitude

    def __ne__(self, other: object) -> bool:
        """Метод сравнения высот двух самолетов (Air_1 != Air_2)."""
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.bar_altitude != other.bar_altitude
