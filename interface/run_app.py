from interface.utils_run_app import ask_user, get_api_data, handle_file_operations, handle_save, show_message


def run_app() -> None:
    """Функция для реализации общего функционала и работы с пользователем."""
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
