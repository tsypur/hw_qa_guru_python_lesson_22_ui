# UI tests automation для проекта Swag Labs

> web-сайт [SauceDemo](https://www.saucedemo.com/)

---

## Содержание проекта

Фреймворк для автоматизации тестирования включающий:

- **Page Object Model (POM)** для поддерживаемой структуры тестов
- **Отчетность Allure** со скриншотами, видео и подробными шагами
- **Облако Selenoid** для масштабируемого выполнения в браузере
- **Jenkins CI/CD** с ручным выполнением заданий
- **Уведомления Telegram** для получения результатов в режиме реального времени
- **Интеграция с Allure TestOps** для управления тестированием

---

## Используемый стек

<p align="center">
<a href="https://www.jetbrains.com/pycharm/"><img src="media/logo/pycharm.svg" width="50" height="50"  alt="PyCharm"/></a>
<a href="https://www.python.com/"><img src="media/logo/python.svg" width="50" height="50"  alt="Python"/></a>
<a href="https://github.com/"><img src="media/logo/github.svg" width="50" height="50"  alt="GitHub"/></a>
<a href="https://docs.pytest.org/"><img src="media/logo/pytest.svg" width="50" height="50"  alt="Pytest 5"/></a>
<a href="https://aerokube.com/selenoid/"><img src="media/logo/selenoid.svg" width="50" height="50"  alt="Selenoid"/></a>
<a href="https://github.com/allure-framework/allure2"><img src="media/logo/allure.svg" width="50" height="50"  alt="Allure"/></a>
<a href="https://www.jenkins.io/"><img src="media/logo/jenkins.svg" width="50" height="50"  alt="Jenkins"/></a>
<a href="https://qameta.io/"><img src="media/logo/allure_TO.svg" width="50" height="50"  alt="Allure TestOps"/></a>
</p> 

---

## Запуск теста

### Установка
```bash
# 1. Склонировать репозиторий
git clone https://github.com/tsypur/hw_qa_guru_python_lesson_22_ui
cd hw_qa_guru_python_lesson_22_ui

# 2. Создание виртуального окружения
python -m venv venv

# 3. Активация виртуального окружения
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

# 4. Установка зависимостей
pip install -r requirements.txt
```
### Настройка окружения

```bash
Создание файла `.env` в корне проекта
Файл .env включить в .gitignore
```

### Запуск тестов
```bash
# Запуск всех тестов
pytest tests/ --alluredir=allure-results -v

# Запуск конкретных тестов
pytest tests/test_login.py::TestLogin::test_successful_login -v

# Просмотр Allure report
allure serve allure-results
```

---

#### <img src="media/logo/selenoid.svg" width="25" height="25"  alt="Allure"/></a> Демонстрация выполнения теста:

![Text Example](media/test_ex.gif)

---

### Примеры отчётов

#### <img src="media/logo/allure.svg" width="25" height="25"  alt="Allure"/></a> <a target="_blank" href="https://jenkins.autotests.cloud/job/C11-voronirina-diploma-UI/46/allure/">Allure Report</a> [Jenkins](https://jenkins.autotests.cloud/job/tsypur_hw_qa_guru_python_lesson_22_ui/) Build

![Jenkins Build](media/jenkins_build.png)

#### Allure Overview  
![Allure Report](media/allure_overview.png)

#### Детали тестового прогона
![Test Details](media/test_details.png)

#### <img src="media/logo/allure_TO.svg" width="25" height="25"  alt="Allure"/></a> <a target="_blank" href="https://allure.autotests.cloud/launch/38541/">TestOps</a> [TestOps](https://allure.autotests.cloud/project/5055/dashboards) Runs
![TestOps Runs](media/testops_runs.png)

#### Тест-кейсы TestOps
![TestOps Test Cases](media/testops_details.png)


#### <img src="media/logo/telegram.svg" width="25" height="25"  alt="Allure"/></a> Telegram Notification
![Telegram](media/telegram_notification.png)


