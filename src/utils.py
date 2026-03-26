import os

from src.airplane import Airplane

def airplanes_to_dicts(airplanes: list[Airplane]) -> list[dict]:
    """ Вспомогательная функция для преобразования объектов Airplane в список словарей. """
    return [air.get_dict_from_airplane() for air in airplanes]


def ensure_directory(path: str) -> None:
    """ Вспомогательная функция, создает директорию для файла если она еще не существует. """
    os.makedirs(os.path.dirname(path), exist_ok=True)