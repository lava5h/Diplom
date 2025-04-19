from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.UI_page import TeachersSchedule

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

teachers_schedule = TeachersSchedule(driver)

teachers_schedule.autorization()

# Создание события через кнопку "+"
def test_create_lesson_plus():
    
    # Устанавливаем неявное ожидание на 10 секунд
    teachers_schedule.driver.implicitly_wait(15)
    
    teachers_schedule.touch_botton_plus()

    teachers_schedule.create_lesson(event_name="Факультатив") 

def test_short_eventname():
    
    # Устанавливаем неявное ожидание на 10 секунд
    teachers_schedule.driver.implicitly_wait(15)
    
    teachers_schedule.touch_botton_plus()

    teachers_schedule.create_lesson(event_name="Ф") 

def test_long_eventname():

    # Устанавливаем неявное ожидание на 10 секунд
    teachers_schedule.driver.implicitly_wait(15)
    
    teachers_schedule.touch_botton_plus()

    teachers_schedule.create_lesson(event_name="уацававацауауааваццацацацацацацацацацацауцкцкцкцкцуаууакуак")

def test_create_lesson_slot():
    
    # Устанавливаем неявное ожидание на 10 секунд
    teachers_schedule.driver.implicitly_wait(15)
    
    teachers_schedule.slot_selection()

    teachers_schedule.create_lesson(event_name="Математика") 

def test_null_eventname():

    # Устанавливаем неявное ожидание на 10 секунд
    teachers_schedule.driver.implicitly_wait(15)
    
    teachers_schedule.touch_botton_plus()

    teachers_schedule.create_lesson(event_name="")
