from src.airplane import Airplane

def airplanes_to_dicts(airplanes: list[Airplane]) -> list[dict]:
    """ Вспомогательная функция для преобразования объектов Airplane в список словарей. """
    return [air.get_dict_from_airplane() for air in airplanes]