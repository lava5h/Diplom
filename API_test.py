import pytest
from allure import step, title, description, feature, severity, severity_level
from pages.API_page import CreateEvent
from pages.API_page import ChangeEvent
from pages.API_page import DeleteEvent

# Данные для авторизации
Cookie = "token_global=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjE0ODk0MjUwLCJpZGVudGl0eSI6InRlc3QudHN0MzQ1QHNreWVuZy5ydSIsImlkZW50aXR5TG9naW4iOm51bGwsImlkZW50aXR5RW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJpZGVudGl0eVBob25lIjoiKzc5MTY1MDAyMjU1IiwibmFtZSI6Ilx1MDQxMFx1MDQzYlx1MDQzNVx1MDQzYVx1MDQ0MVx1MDQzNVx1MDQzOSIsInN1cm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJ1aUxhbmd1YWdlIjoicnUiLCJsb2NhbGUiOiJydSIsInNlcnZpY2VMb2NhbGUiOm51bGwsInVhcyI6MzAsImp3dFR5cGUiOjEsImp0aSI6InliVjV0MkxjcVhTQTFNMDFmdGhsR3Z1WFd0RWVPZFNoIiwiYnJhbmQiOm51bGwsImV4cCI6MTc0NTc4MTA4NywiYmlydGhkYXkiOiIyMDA2LTEwLTEwIiwiYUlzU3Ryb25nIjp0cnVlLCJhVHlwZSI6IlVTRVJOQU1FX1BBU1NXT1JEIiwiYVRpbWUiOjE3NDU2OTQ2ODYsInJvbGVzIjpbIlJPTEVfVEVBQ0hFUl9DQU5ESURBVEUiLCJST0xFX1RFQUNIRVJfQ0FORElEQVRFX0JBU0VfQUNDRVNTIiwiUk9MRV9UUk1fVVBMT0FEX0ZJTEUiLCJST0xFX1RUQ19VU0FHRSIsIlJPTEVfVklNQk9YX1RFQUNIRVJfVVNBR0UiLCJST0xFX1RFQUNIRVIiLCJST0xFX0NSTTJfVEVBQ0hFUl9BQ0NFU1MiLCJST0xFX1RFQUNIRVJTX0NBQklORVRfQkFTRV9BQ0NFU1MiLCJST0xFX01BVEhfVEVBQ0hFUiIsIlJPTEVfTUFUSF9DT05URU5UX1RIRU1FX1ZJRVciXX0.0AFZ0pUOs9r7ZW6A5RKLn2ItWdodpCyuOWLg_X6WaduksyN6TFa68Rm5wH5le4ID4dtTx4EBg3MKJZ5cYC-Y3L2Z2WdpRhVkPA78qCEf-fBiOTfSpWViZ0zE66O_MUaQgqNvn8CwDj7MxhDEIesyIqsmObLuXkThpzHwDc46hc1gIQmX-a2EqPlvA8VUqfdp-prbQKbg5DxmCNVjkzeuUvo31SGuY2iTgVn3HB3OpHrguT70ZqILg8Www_RC01jVhl5q_OF3nL1Fyin7rLOHZvUfwrSWoQTCMSQb-ki5f34n1phjSr1iDFrSB6Qk_nT5DBj_g70zivkAfOSg3YDwcsXmkKkXb_zOI68mCBrUxGhVOMTpVd5n-hmHoGh9tFZ_OrPXSk6HbzcEaIyd89CrLGcL4l3HmNxDj0ZPJdPtH51vQ7CYfcb0XG079cWR3LgwpbKYb2rZobfSNpdMCcFf-axgLWEUT3GJ4jGD8PUpi2AyF4XRF6fOp9GOR0NQWar5ScOV9T67NqiMqEmma3zm92cPAsCShEEzDfJMbM7oH3jOVVNql6VN9ZVRHr_U7-lTgaAT0a6ay8G7IZYhe09agEsclMhBUlIa5cwYa71JBQZ0HZ245tuW4z3XzXCJVd_4DPrY6bNNPlI1sh3urziKbeNB2gVPY0wjV1P4pCBWx0Q"

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
