# QIWI Хакатон 25.07.2023

**Задание:** _Реализовать консольную утилиту, которая выводит курсы валют ЦБ РФ за определенную дату. Для получения курсов необходимо использовать официальный API ЦБ РФ_

**Установка зависимостей**

`pip install -r .\requirements.txt`

**Примеры запуска утилиты**

`py .\main.py currency_rates --code=USD --date=2021-10-08`

`py .\main.py currency_rates --code=BYN --date=2022-06-30`

**Запуск тестов**

`py -m unittest`