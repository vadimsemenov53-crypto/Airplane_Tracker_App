from abc import ABC, abstractmethod

class BaseDesignerAirplane(ABC):
    """ Базовый класс, для сбора информации о самолетах. """

    @abstractmethod
    def _get_report(self):
        """ Метод для формирования отчета. """
        pass


    @abstractmethod
    def _filtered_velocity(self):
        """ Метод - фильтрация самолетов по скорости. """
        pass


    @abstractmethod
    def _filtered_bar_altitude(self):
        """ Метод - фильтрация самолетов по высоте. """
        pass
