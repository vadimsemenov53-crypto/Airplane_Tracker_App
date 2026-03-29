from src.api import APICoordinates, APIAircraft
from src.designer_airplane import DesignerAirplane
from src.airplane import Airplane
from src.file_manager_json import FileManagerJson
from src.file_manager_csv import FileManagerCSV
from src.file_manager_excel import FileManagerEXCEL

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


def get_file_format_user() -> int | None:
    """ Вспомогательная функция для выбора форма файлов для работы (JSON, CSV, EXCEL) """
    while True:
        show_message("""
        Выберите формат в котором вы собираетесь работать:
        1 - JSON
        2 - CSV
        3 - EXCEL
        4 - Выход
        """)
        format_file = int(ask_user())

        if format_file == 4:
            show_message("Завершение работы с файлами.")
            break

        elif format_file not in (1, 2 ,3, 4):
            show_message("Неверный выбор (1, 2, 3, 4)")

        else:
            return format_file


def get_file_manager(file_name: str | None = None):
    """ Вспомогательная функция для передачи имени файла
     и создание объекта класса FileManagerJSON / CSV / EXCEL."""
    format_file = get_file_format_user()

    if format_file == 1:
        if file_name:
            return FileManagerJson(file_name)

        return FileManagerJson()

    elif format_file == 2:
        if file_name:
            return FileManagerCSV(file_name)

        return FileManagerCSV()

    else:
        if file_name:
            return FileManagerEXCEL(file_name)
        return FileManagerEXCEL()


def handle_save(report: list[Airplane] | None = None) -> None:
    """Вспомогательная функция для сохранения переданных данных в файл."""
    if report:
        show_message("Передайте имя для файла"
                     "Пример: 'report_api.json' "
                     "Или попустите файл сохранить со стандартным именем (data.json)")
        file_name = str(ask_user()).strip()

        if file_name:
            file = get_file_manager(file_name)

            show_message("Передайте путь для сохранения файла")
            path_to_save = str(ask_user()).strip()

            file.save_to_file(report, path_to_save)
        else:
            file = get_file_manager()

            show_message("Передайте путь для сохранения файла")
            path_to_save = str(ask_user()).strip()

            file.save_to_file(report, path_to_save)

    else:
        handle_file_operations()

def handle_file_operations() -> None:
    """ Вспомогательная функция для работы с уже существующими файлами """
    file = get_file_manager()

    while True:
        show_message("""
        Вам доступно: 
        1- Чтение данных 
        2- Добавление данных 
        3- Удаление данных
        """)
        choice_work = int(ask_user())

        if choice_work == 1:
            show_message("Передайте путь до файла.")
            path_to_file = str(ask_user()).strip()

            print(file.read_file(path_to_file))

        elif choice_work == 2:
            show_message("Передайте путь до файла.")
            path_to_file = str(ask_user()).strip()

            obj_air = get_airplane_object()

            if obj_air:
                file.add_info_file([obj_air], path_to_file)

        elif choice_work == 3:
            show_message("Передайте путь до файла.")
            path_to_file = str(ask_user()).strip()

            show_message("Передайте позывной для удаления самолета")
            callsign = str(ask_user()).strip().upper()

            file.delete_info_file(callsign, path_to_file)


def get_airplane_object():
    """ Вспомогательная функция конструктор объектов самолетов """
    show_message("Заполните параметры самолета (Страна, Позывной, Скорость, Вертикальная скорость, Высота полета.)"
                 "Напишите параметры через запятую"
                 "Пример: Germany, DLH123, 250.5, 5.2, 11000")

    user_input = ask_user().strip()
    params = [p.strip() for p in user_input.split(",")]

    if len(params) != 5:
        show_message("Ошибка: нужно ввести ровно 5 параметров.")
        return None

    country, callsign, velocity, vertical_rate, bar_altitude = params

    try:
        velocity = float(velocity)
        vertical_rate = float(vertical_rate)
        bar_altitude = float(bar_altitude)
    except ValueError:
        show_message("Ошибка: скорость и высота должны быть числами.")
        return None

    return Airplane(
        country=country,
        callsign=callsign,
        velocity=velocity,
        vertical_rate=vertical_rate,
        bar_altitude=bar_altitude
    )



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
            result_api = get_api_data()

            show_message("Сохранить полученные данные? (Y-да, Enter-нет)")
            choice_api = str(ask_user()).strip().upper()

            if choice_api == "Y":
                handle_save(result_api)

        elif choice_menu == 2:
            handle_file_operations()

        elif choice_menu == 3:
            show_message("Завершение работы.")
            break


def get_api_data() -> list[Airplane] | None:
    """ Функция для реализации работы пользователя с API - сервисом. """
    show_message("Введите страну на английском языке (Spain, Germany...)")
    choice_country = str(ask_user()).strip().capitalize()

    api_1 = APICoordinates()
    api_1.get_response_api(choice_country)
    api_1.get_coordinates()

    api_2 = APIAircraft()
    api_2.get_response_api(api_1.coordinates)

    data_air = api_2.aeroplanes

    designer = DesignerAirplane(data_air)
    report = designer.get_report()

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
            filter_report = designer.filtered_velocity()

            show_message("Вывести результат в консоль? (Y-да, N-нет)")
            choice_filter = str(ask_user()).strip().upper()

            show_message("Сделать топ? (1, 2, 3 ... или Enter для пропуска.)")
            choice_filter_top = ask_user().strip()

            if choice_filter == "Y":
                if choice_filter_top.isdigit():
                    show_report(filter_report, int(choice_filter_top))
                else:
                    show_report(filter_report)

        elif choice_report_filter == 2:
            filter_report = designer.filtered_bar_altitude()

            show_message("Вывести результат в консоль? (Y-да, N-нет)")
            choice_filter = str(ask_user()).strip().upper()

            show_message("Сделать топ? (1, 2, 3 ... или Enter для пропуска.)")
            choice_filter_top = ask_user().strip()

            if choice_filter == "Y":
                if choice_filter_top.isdigit():
                    show_report(filter_report, int(choice_filter_top))
                else:
                    show_report(filter_report)

        elif choice_report_filter == 3:
            break
        else:
            show_message("Неверное значение.")

        return report





if __name__ == "__main__":
    run_app()