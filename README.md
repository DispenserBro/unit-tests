Тест на покрытие от Coveralls:

[![Coverage Status](https://coveralls.io/repos/github/DispenserBro/unit-tests/badge.svg)](https://coveralls.io/github/DispenserBro/unit-tests)

[Покрытие от pytest-cov](./coverage.json),
тут 98.9% покрытия.

[Отчет pylint](./pylint_report.json),
тут pylint ругается только на файлы тестов

[Зависимости окружения](./requirements.txt)

### Объяснение сценариев тестов

В файле [test_main.py](./final_hw/tests/test_main.py) находится только один тест, который проверяет правильность вывода в консоль.
Он нужен для поднятия уровня покрытия.

В файле [test_average_value.py](./final_hw/tests/test_average_value.py) находится основная масс тестов.
Проверяется нахождение среднего значения, сравнения средних значений и вывод результатов сравнений в понятном формате.
Это буквально весь функционал класса `AverageValue`