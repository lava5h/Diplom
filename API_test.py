import pytest
from pages.API_page import CreateEvent
from pages.API_page import ChangeEvent
from pages.API_page import DeleteEvent

# Данные для авторизации
Cookie = "..."

# URL для создания проекта
url = "https://api-teachers.skyeng.ru/v2/schedule/"

# Создание проекта
def test_create_positive():
    
    create_event = CreateEvent(url, Cookie)
    response = create_event.create_event_positive(url)

    # Проверка статуса ответа
    assert response.status_code == 200
    return create_event

def test_create_negative_color():
    
    create_event = CreateEvent(url, Cookie)
    response = create_event.create_event_negative_color(url)

    # Проверка статуса ответа
    assert response.status_code == 400
    
def test_create_negative_name():
    
    create_event = CreateEvent(url, Cookie)
    response = create_event.create_event_negative_name(url)

    # Проверка статуса ответа
    assert response.status_code == 400       

def test_change_positive():

    create_event = test_create_positive()
    event_id = create_event.event_id
    
    change_event = ChangeEvent(url, Cookie, event_id)
    response = change_event.change_event_positive(url)

    # Проверка статуса ответа
    assert response.status_code == 200

def test_delete_positive():

    create_event = test_create_positive()
    event_id = create_event.event_id
    
    delete_event = DeleteEvent(url, Cookie, event_id)
    response = delete_event.delete_event_positive(url)

    # Проверка статуса ответа
    assert response.status_code == 200
