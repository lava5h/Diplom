import pytest
from allure import step, title, description, feature, severity, severity_level
from pages.API_page import CreateEvent
from pages.API_page import ChangeEvent
from pages.API_page import DeleteEvent

# Данные для авторизации
Cookie = "..."

# URL для создания проекта
url = "https://api-teachers.skyeng.ru/v2/schedule/"

# Создание события (позитивный)
@title("Создание события (позитивный)")
@description("Проверка успешного создания события через API")
@feature("Создание события")
@severity(severity_level.CRITICAL)
def test_create_positive():
    with step("Отправка запроса на создание события"):
        create_event = CreateEvent(url, Cookie)
        response = create_event.create_event_positive(url)

    with step("Проверка статуса ответа"):
        assert response.status_code == 200

    return create_event


# Создание события с непредставленным цветом (негативный)
@title("Создание события с непредставленным цветом")
@description("Цвет не передан — сервер должен вернуть #000000")
@feature("Создание события")
@severity(severity_level.NORMAL)
def test_create_negative_color():
    with step("Отправка запроса с некорректным цветом"):
        create_event = CreateEvent(url, Cookie)
        response = create_event.create_event_negative_color(url)
        data = response.json()

    with step("Проверка, что цвет по умолчанию #000000"):
        assert response.status_code == 200
        assert data["data"]["payload"]["payload"]["color"] == "#000000"


# Создание события без названия (негативный)
@title("Создание события без названия")
@description("Проверка, что событие не создается без имени")
@feature("Создание события")
@severity(severity_level.NORMAL)
def test_create_negative_name():
    with step("Попытка создать событие без имени"):
        create_event = CreateEvent(url, Cookie)
        response = create_event.create_event_negative_name(url)
        data = response.json()

    with step("Проверка, что данные не вернулись и статус 200"):
        assert data["data"] is None
        assert response.status_code == 200       


# Редактирование события (позитивный)
@title("Редактирование события")
@description("Редактирование ранее созданного события")
@feature("Редактирование события")
@severity(severity_level.CRITICAL)
def test_change_positive():
    with step("Создание события перед редактированием"):
        create_event = test_create_positive()
        event_id = create_event.event_id

    with step("Отправка запроса на редактирование"):
        change_event = ChangeEvent(url, Cookie, event_id)
        response = change_event.change_event_positive(url)

    with step("Проверка, что редактирование прошло успешно"):
        assert response.status_code == 200


# Удаление события (позитивный)
@title("Удаление события")
@description("Удаление события, созданного ранее")
@feature("Удаление события")
@severity(severity_level.CRITICAL)
def test_delete_positive():
    with step("Создание события перед удалением"):
        create_event = test_create_positive()
        event_id = create_event.event_id

    with step("Отправка запроса на удаление"):
        delete_event = DeleteEvent(url, Cookie, event_id)
        response = delete_event.delete_event_positive(url)

    with step("Проверка, что удаление прошло успешно"):
        assert response.status_code == 200
