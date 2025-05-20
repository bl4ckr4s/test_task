# Проект автоматизации API для сервиса бронирования

## Инструменты и технологии

- Python 3.12
- PyTest с расширением xdist для параллельного выполнения тестов
- Библиотека Requests для взаимодействия с API
- Pydantic для валидации ответов
- Allure для расширенной отчетности по тестам
- GitHub Actions для CI/CD

## Установка и запуск

1. Создайте и активируйте виртуальное окружение.
    ```bash
    python -m venv venv
    source venv/bin/activate
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
3. Запустите тесты с формированием Allure-отчёта:
      ```bash
      pytest -v -n auto --alluredir=allure-results
4. Сгенерируйте и откройте отчет локально:
   ```bash
   allure serve allure-results

## Отчёты Allure

Отчёты о результатах автоматических тестов также доступны онлайн по ссылке: https://bl4ckr4s.github.io/test_task
