from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TeachersSchedule:

    """
    Класс для работы с расписанием в кабинете учителя.
    
    Этот класс предоставляет методы для работы с элементами в расписании учителя.
    """


    def __init__(self, driver):

        """
        Инициализация страницы.

        driver: объект веб-драйвера
        """

        self.driver = driver
        self.driver.get("https://teachers.skyeng.ru/schedule")

    # Функция авторизации 
    def autorization(self):

        username = self.driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        username.send_keys("test.tst345@skyeng.ru")

        password = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password.send_keys("2DbhAAPG6q")

        button = self.driver.find_element(By.CSS_SELECTOR, "button[class='button button--primary']")
        button.click() 

    # Функция нажатия на кнопку "+"
    def touch_botton_plus(self):

        button = self.driver.find_element(By.CSS_SELECTOR, "ds-icon[name='add']")
        button.click()

    # Функция создания личного события
    def create_lesson(self, event_name):

        element = self.driver.find_element(By.XPATH, "//div[contains(.//span, 'Личное событие')]")
        element.click()

        eventname = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Например: посмотреть вебинар']")
        eventname.send_keys(event_name)

        description = self.driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Например: ссылка на вебинар']")
        description.send_keys("Описание")

        color = self.driver.find_element(By.CSS_SELECTOR, "path[style='fill: rgb(250, 198, 65);']")
        color.click()

        button = self.driver.find_element(By.CSS_SELECTOR, "button[class='root -type-primary -color-brand -size-m -active']")
        button.click()

    def slot_selection(self):

        slot = self.driver.find_element(By.CSS_SELECTOR, "div[class='box-hover hover-enabled']")
        slot.click()
