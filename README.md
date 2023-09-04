### 1. Описание тестов
Тестируется страница https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

Реализованные тест-кейсы:

1.1. Запись с ContactName равной 'Giovanni Rovelli' имеет Address = 'Via Ludovico il Moro 22'.

1.2. Вывод только те строки таблицы Customers, где city='London'. Количество такиз строк равно 6.

1.3. Добавление новой записи в таблицу Customers и проверка, что эта запись добавилась.

1.4. Обновление всех полей (кроме CustomerID) для выбранной записи таблицы Customers и проверка, что изменения записались в базу.

1.5. Проверка наличия кнопки 'Get your own SQL server' и того, что кнопка имеет соответствующий текст

### 2. Особенности:
2.1. Язык Python, подключен allure

2.2. Тесты реализованы только для Chrome. Используя https://pypi.org/project/webdriver-manager/ можно добавить запуск тестов на других браузерах.

2.3. В случае добавления тестов для Firefox, необходимо использовать другие селекторы, т.к. для Firefox данные в таблице вставляются в iframe. Кроме этого в Firefox не работают INSERT запросы (ограничение сервиса w3schools)

### 3. Запуск тестов
3.1. На машину необходимо установить docker

3.2. Собрать образ из Dockerfile
```
#> docker build . --no-cache -t w3schools_pytest_demo_runner
```

3.3. Запустить контейнер
```
#> docker run --rm w3schools_pytest_demo_runner 
```