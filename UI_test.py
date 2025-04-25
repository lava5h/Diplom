import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pages.UI_page import TeachersSchedule

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

teachers_schedule = TeachersSchedule(driver)

teachers_schedule.autorization()

# Создание события через кнопку "+"
def test_create_lesson_plus():
    
    # Устанавливаем неявное ожидание на 5 секунд
    teachers_schedule.driver.implicitly_wait(5)
    teachers_schedule.touch_botton_plus()
    teachers_schedule.create_lesson(event_name="Факультатив") 

    # Проверяем, что событие появилось в списке
    created_event = teachers_schedule.driver.find_element(By.XPATH, "//*[contains(text(), 'Факультатив')]")
    assert created_event, "Созданное событие найдено в списке"

# Создание события с названием из одного символа
def test_short_eventname():
    
    # Устанавливаем неявное ожидание на 5 секунд
    teachers_schedule.driver.implicitly_wait(5)
    teachers_schedule.touch_botton_plus()
    teachers_schedule.create_lesson(event_name="Ф")

    # Проверяем, что событие появилось в списке
    created_event = teachers_schedule.driver.find_element(By.XPATH, "//*[contains(text(), 'Ф')]")
    assert created_event, "Созданное событие найдено в списке" 

# Создание события с названием из > 40 символов
def test_long_eventname():

    # Устанавливаем неявное ожидание на 5 секунд
    teachers_schedule.driver.implicitly_wait(5)
    teachers_schedule.touch_botton_plus()
    teachers_schedule.create_lesson(event_name="уацававацауауааваццацацацацацацацацацацауцкцкцкцкцуаууакуак")

    # Проверяем, что событие появилось в списке обрезанное до 40 символов
    created_event = teachers_schedule.driver.find_element(By.XPATH, "//*[contains(text(), 'уацававацауауааваццацацацацацацацацацаца')]")
    assert created_event, "Созданное событие найдено в списке" 

# Создание события с названием из 40 символов
def test_max_eventname():

    # Устанавливаем неявное ожидание на 5 секунд
    teachers_schedule.driver.implicitly_wait(5)
    teachers_schedule.touch_botton_plus()
    teachers_schedule.create_lesson(event_name="уацававацауауааваццацацацацацацацацацаца")
    
    # Проверяем, что событие появилось в списке
    created_event = teachers_schedule.driver.find_element(By.XPATH, "//*[contains(text(), 'уацававацауауааваццацацацацацацацацацаца')]")
    assert created_event, "Созданное событие найдено в списке" 

# Создание события с названием из смайлика (негативный)
def test_emoji_eventname():

    # Устанавливаем неявное ожидание на 5 секунд
    teachers_schedule.driver.implicitly_wait(5)
    teachers_schedule.touch_botton_plus()
    teachers_schedule.create_lesson(event_name="😀")

    # Проверяем, что событие появилось в списке
    created_event = teachers_schedule.driver.find_element(By.XPATH, "//*[contains(text(), '😀')]")
    assert created_event, "Созданное событие не найдено в списке" 
