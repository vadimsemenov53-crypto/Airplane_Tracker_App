from abc import ABC, abstractmethod

class BaseDesignerAirplane(ABC):
    """ Базовый класс, для сбора информации о самолетах. """

    @abstractmethod
    def get_report_json(self):
        """ Метод для формирования отчета JSON. """
        pass


    # @abstractmethod
    # def filtered_json_velocity(self):
    #     """ Метод - фильтрация самолетов по скорости. """
    #     pass
    #
    #
    # @abstractmethod
    # def filtered_json_bar_altitude(self):
    #     """ Метод - фильтрация самолетов по высоте. """
    #     pass
