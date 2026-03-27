from src.api import APICoordinates, APIAircraft
from src.designer_airplane import DesignerAirplane
from src.airplane import Airplane

def ask_user() -> str:
    """ Вспомогательная функция для взаимодействия с пользователем. """
    return input(f"Пользователь: ")


def show_message(message: str) -> None:
    """ Вспомогательная функция вывода в консоль сообщения от программы. """
    print(f"\nПрограмма:\n{message}")


def show_report(airplanes: list[Airplane], limit: int | None = None) -> None:
    """ Вспомогательная функция вывода в консоль результатов отчета. """
    for i, air in enumerate(airplanes, start=1):
        if limit and i > limit:
            break

        print(f"{i}. Позывной: {air.callsign} | Скорость: {air.velocity} | Высота: {air.bar_altitude}")


def run_app():
    """ Функция для реализации общего функционала и работы с пользователем. """
    while True:
        show_message("""
                Добро пожаловать в приложение Airplane Tracker.
                Выберите режим работы:
                1 - Получение данных о самолетах в реальном времени.
                2 - Работа с файлами (JSON, CSV, EXCEL) (если данные уже существуют.)
                3 - Выход.
                """)
        choice_menu = int(ask_user())

        if choice_menu == 1:
            get_api_data()

        elif choice_menu == 2:
            break

        elif choice_menu == 3:
            show_message("Завершение работы.")
            break


def get_api_data():
    """ Функция для реализации работы пользователя с API - сервисом. """
    show_message("Введите страну на английском языке (Spain, Germany...)")
    choice_country = str(ask_user()).strip().capitalize()

    api_1 = APICoordinates()
    api_1.get_response_api(choice_country)
    api_1.get_coordinates()

    api_2 = APIAircraft()
    api_2.get_response_api(api_1._coordinates)

    data_air = api_2._aeroplanes

    designer = DesignerAirplane(data_air)
    report = designer._get_report()

    show_message("Вывести результат в консоль? (Y-да, N-нет)")
    choice_report = str(ask_user()).strip().upper()

    if choice_report == "Y":
        show_report(report)

    while True:
        show_message("""
        Отфильтровать полученные данные по скорости или высоте?
        1 - Скорость.
        2 - Высота.
        3 - Нет.""")
        choice_report_filter = int(ask_user())

        if choice_report_filter == 1:
            filter_report = designer._filtered_velocity()

            show_message("Вывести результат в консоль? (Y-да, N-нет)")
            choice_filter = str(ask_user()).strip().upper()

            show_message("Сделать топ? (1, 2, 3 ... или Enter для пропуска.)")
            choice_filter_top = int(ask_user())

            if choice_filter == "Y":
                if isinstance(choice_filter_top, int):
                    show_report(filter_report, choice_filter_top)
                else:
                    show_report(filter_report)

        elif choice_report_filter == 2:
            filter_report = designer._filtered_bar_altitude()

            show_message("Вывести результат в консоль? (Y-да, N-нет)")
            choice_filter = str(ask_user()).strip().upper()

            show_message("Сделать топ? (1, 2, 3 ... или Enter для пропуска.)")
            choice_filter_top = int(ask_user())

            if choice_filter == "Y":
                if isinstance(choice_filter_top, int):
                    show_report(filter_report, choice_filter_top)
                else:
                    show_report(filter_report)

        elif choice_report_filter == 3:
            break
        else:
            show_message("Неверное значение.")





if __name__ == "__main__":
    run_app()