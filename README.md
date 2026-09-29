# ✈️ Airplane Tracker App
Консольное приложение на Python для получения, 
обработки и сохранения данных о самолётах в реальном времени.

## 🚀 Возможности
- Получение данных о самолётах через API (по стране)
- Фильтрация:
- - по скорости
- - по высоте
- Вывод результатов в консоль
- Сохранение данных в файлы:
- - JSON
- - CSV
- - Excel (XLSX)
 - Работа с уже существующими файлами:
- - чтение
- - добавление записей
- - удаление по callsign

## ⚙️ Установка
- git clone <https://github.com/vadimsemenov53-crypto/Airplane_Tracker_App>
- poetry install

## ▶️ Запуск
```bash
python3 main.py
```

## 🧠 Используемые технологии
- Python 3.14
- pandas
- pytest
- unittest.mock
- requests

## 📌 Особенности
- Разделение логики и интерфейса
- Использование абстрактных классов для работы с файлами
- Поддержка нескольких форматов данных
- Тестирование CLI через моки

## 👨‍💻 Автор
### Vadim Semenov

Запуск тестов:

```bash
pytest --cov=src tests/ --cov-report=html
pytest --cov
````
````
Name                               Stmts   Miss  Cover
------------------------------------------------------
interface/__init__.py                  0      0   100%
interface/utils_run_app.py           140     64    54%
src/__init__.py                        0      0   100%
src/airplane.py                       38      0   100%
src/api.py                            29      0   100%
src/base_api_work.py                  22      1    95%
src/base_designer_airplane.py         12      3    75%
src/base_file_manager.py              60     12    80%
src/designer_airplane.py              23      0   100%
src/file_manager_csv.py               39      0   100%
src/file_manager_excel.py             39      0   100%
src/file_manager_json.py              51      0   100%
src/utils.py                           9      0   100%
tests/__init__.py                      0      0   100%
tests/conftest.py                     40      0   100%
tests/test_airplane.py                32      0   100%
tests/test_api.py                     53      0   100%
tests/test_base_api_work.py           30      0   100%
tests/test_designer_airplane.py       49      0   100%
tests/test_file_manager_csv.py        95      0   100%
tests/test_file_manager_excel.py      95      0   100%
tests/test_file_manager_json.py      112      0   100%
tests/test_utils.py                   15      0   100%
tests/test_utils_run_app.py           95      0   100%
------------------------------------------------------
TOTAL                               1078     80    93%
```