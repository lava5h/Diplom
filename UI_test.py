import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pages.UI_page import TeachersSchedule
from allure import step, title, description, feature, severity, severity_level

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
teachers_schedule = TeachersSchedule(driver)
teachers_schedule.autorization()

# Создание события через кнопку "+"
@title('Создание события через кнопку "+"')
@description('Проверка создания события с нормальным названием')
@feature('Создание событий')
@severity(severity_level.CRITICAL)

def test_create_lesson_plus():
    with step('Установка неявного ожидания'):
        teachers_schedule.driver.implicitly_wait(5)
    
    with step('Нажатие на кнопку "+"'):
        teachers_schedule.touch_botton_plus()
    
    with step('Создание урока'):
        teachers_schedule.create_lesson(event_name="Факультатив")
    
    with step('Проверка создания события'):
        created_event = teachers_schedule.driver.find_element(By.XPATH, "//*[contains(text(), 'Факультатив')]")
        assert created_event, "Созданное событие найдено в списке"


# Создание события с названием из одного символа
@title('Создание события с названием из одного символа')
@description('Проверка создания события с минимальным названием')
@feature('Создание событий')
@severity(severity_level.CRITICAL)

def test_short_eventname():
    
    with step('Нажатие на кнопку "+"'):
        teachers_schedule.touch_botton_plus()
    
    with step('Создание урока'):
        teachers_schedule.create_lesson(event_name="Ф")
    
    with step('Проверка создания события'):
        created_event = teachers_schedule.driver.find_element(By.XPATH, "//*[contains(text(), 'Ф')]")
        assert created_event, "Созданное событие найдено в списке"


# Создание события с названием длиннее 40 символов
@title('Создание события с названием длиннее 40 символов')
@description('Проверка создания события с длинным названием')
@feature('Создание событий')
@severity(severity_level.NORMAL)

def test_long_eventname():
    
    with step('Нажатие на кнопку "+"'):
        teachers_schedule.touch_botton_plus()
    
    with step('Создание урока'):
        teachers_schedule.create_lesson(event_name="уацававацауауааваццацацацацацацацацацацауцкцкцкцкцуаууакуак")
    
    with step('Проверка создания обрезанного события'):
        created_event = teachers_schedule.driver.find_element(By.XPATH, "//*[contains(text(), 'уацававацауауааваццацацацацацацацацацаца')]")
        assert created_event, "Созданное событие найдено в списке"


# Создание события с названием из 40 символов
@title('Создание события с названием из 40 символов')
@description('Проверка создания события с максимально допустимым названием')
@feature('Создание событий')
@severity(severity_level.NORMAL)

def test_max_eventname():
    
    with step('Нажатие на кнопку "+"'):
        teachers_schedule.touch_botton_plus()
    
    with step('Создание урока'):
        teachers_schedule.create_lesson(event_name="уацававацауауааваццацацацацацацацацацаца")
    
    with step('Проверка создания события'):
        created_event = teachers_schedule.driver.find_element(By.XPATH, "//*[contains(text(), 'уацававацауауааваццацацацацацацацацацаца')]")
        assert created_event, "Созданное событие найдено в списке"


# Создание события с названием из смайлика
@title('Создание события с названием из смайлика')
@description('Проверка создания события с недопустимым символом')
@feature('Создание событий')
@severity(severity_level.MINOR)

def test_emoji_eventname():
        
    with step('Нажатие на кнопку "+"'):
        teachers_schedule.touch_botton_plus()
        
    with step('Создание урока со смайликом'):
        emoji = "😀"
        teachers_schedule.create_lesson(event_name=emoji)
        
    with step('Проверка отсутствия события в списке'):
        created_event = teachers_schedule.driver.find_element(By.XPATH, "//*[contains(text(), '{emoji}')]")
        assert created_event, "Созданное событие найдено в списке"
