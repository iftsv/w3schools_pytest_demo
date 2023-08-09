### 1. Описание тестов
Тестируется страница https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

Реализованные тест-кейсы:

1.1. Запись с ContactName равной 'Giovanni Rovelli' имеет Address = 'Via Ludovico il Moro 22'.

1.2. Вывод только те строки таблицы Customers, где city='London'. Количество такиз строк равно 6.

1.3. Добавление новой записи в таблицу Customers и проверка, что эта запись добавилась.

1.4. Обновление всех полей (кроме CustomerID) для выбранной записи таблицы Customers и проверка, что изменения записались в базу.

1.5. Проверка наличия и видимости на странице кнопки 'Get your own SQL server'

### 2. Особенности:
2.1. Язык Python, подключен allure

2.2. Тесты реализованы только для WebDriver for Chrome.

2.3. В случае добавления тестов для браузера Firefox, необходимо использовать другие селекторы, т.к. данные в таблице вставляются в iframe для Firefox. Так же в браузере Firefox не работают INSERT запросы

### 3. Запуск тестов
3.1. На машину необходимо установить docker и контейнер с Chrome 
```
#> docker pull selenium/standalone-chrome
```

3.2. Запуск контейнера 
```
#> docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest
```

3.3. Запуск тестов из каталога репозитория
```
#> python -m pytest --alluredir=test_results/  .\tests\
```

3.4. Для просмотра отчетов 
```
#> allure serve test_results/
```

 ### 4. Запуск полностью в docker-контейнере (TODO)
4.1. файл draft_Dockerfile

4.2. исправить webdriver.Remote на webdriver.Chrome

4.3. Получение/Сборка
```
docker pull selenium/standalone-chrome && docker buildx b w3schools_pytest_runner .
```