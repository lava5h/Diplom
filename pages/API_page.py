import requests

# Создание проектов
class CreateEvent:

    """
    Класс для создания личных событий в кабинете учителя.
    
    Этот класс предоставляет методы для создания личных событий в расписании учителя.
    """

    def __init__(self, url, Cookie):
        self.url = url
        self.Cookie = Cookie
        self.event_id = None

        """
        Инициализация страницы.

        url: ссылка на страницу сайта.
        Cookie: токен для авторизации на сайте.
        """

    project_data_positive = {
        "backgroundColor": "#F4F5F6",
        "color": "#81888D",
        "description": "",
        "endAt": "2025-04-23T03:00:00+07:00",
        "startAt": "2025-04-23T02:30:00+07:00",
        "title": "Факультатив"
    }

    project_data_negative_color = {
        "backgroundColor": "#171E83",
        "color": "#000000",
        "description": "",
        "endAt": "2025-04-23T03:00:00+07:00",
        "startAt": "2025-04-23T02:30:00+07:00",
        "title": "Факультатив"
    }

    project_data_negative_name = {
        "backgroundColor": "#F4F5F6",
        "color": "#81888D",
        "description": "",
        "endAt": "2025-04-23T03:00:00+07:00",
        "startAt": "2025-04-23T02:30:00+07:00",
        "title": ""
    }

    # Функция создания события (позитивный)
    def create_event_positive(self, url):

        """
        Создание события (позитивный).

        Метод создаёт личное событие через ввод валидных значений.
        """

        headers = {
            "Cookie": self.Cookie,
            "Content-Type": "application/json"
        }
        
        response = requests.post(url + "createPersonal", headers=headers, json=self.project_data_positive)
        self.event_id = response.json()["data"]["payload"]["id"]
        return response

    # Функция создания проекта (негативный)
    def create_event_negative_color(self, url):

        """
        Создание события (негативный).

        Метод создаёт личное событие через ввод невалидных значений (непредставленный цвет).
        """

        headers = {
            "Cookie": self.Cookie,
            "Content-Type": "application/json"
        }
        
        response = requests.post(url + "createPersonal", headers=headers, json=self.project_data_negative_color)
        return response

    # Функция создания проекта (негативный)
    def create_event_negative_name(self, url):

        """
        Создание события (негативный).

        Метод создаёт личное событие через ввод невалидных значений (пустое название).
        """

        headers = {
            "Cookie": self.Cookie,
            "Content-Type": "application/json"
        }
        
        response = requests.post(url + "createPersonal", headers=headers, json=self.project_data_negative_name)
        return response

class ChangeEvent:

    """
    Класс для редактирования личных событий в кабинете учителя.
    
    Этот класс предоставляет методы для редактирования личных событий в расписании учителя.
    """

    def __init__(self, url, Cookie, event_id):
        self.url = url
        self.Cookie = Cookie
        self.event_id = event_id

        """
        Инициализация страницы.

        url: ссылка на страницу сайта.
        Cookie: токен для авторизации на сайте.
        """

    def project_data_positive(self):
        project_data_positive = {
            "backgroundColor": "#F4F5F6",
            "color": "#81888D",
            "description": "",
            "title": "Математика",
            "endAt": "2025-04-23T03:00:00+07:00",
            "id": f"{self.event_id}",
            "oldStartAt": "2025-04-23T02:30:00+07:00",
            "startAt": "2025-04-23T02:30:00+07:00"
        }
        return project_data_positive

    # Функция редактирования события (позитивный)
    def change_event_positive(self, url):

        """
        Редактирование события (позитивный).

        Метод редактирует личное событие изменяя название.
        """

        headers = {
            "Cookie": self.Cookie,
            "Content-Type": "application/json"
        }
        
        response = requests.post(url + "updatePersonal", headers=headers, json=self.project_data_positive())
        return response

class DeleteEvent:

    """
    Класс для удаления личных событий в кабинете учителя.
    
    Этот класс предоставляет методы для удаления личных событий в расписании учителя.
    """

    def __init__(self, url, Cookie, event_id):
        self.url = url
        self.Cookie = Cookie
        self.event_id = event_id

        """
        Инициализация страницы.

        url: ссылка на страницу сайта.
        Cookie: токен для авторизации на сайте.
        """

    def project_data_positive(self):
        project_data_positive = {
            "id": f"{self.event_id}",
            "startAt": "2025-04-23T02:30:00+07:00"
        }
        return project_data_positive

    # Функция удаления события (позитивный)
    def delete_event_positive(self, url):

        """
        Удаление события (позитивный).

        Метод удаляет личное событие.
        """

        headers = {
            "Cookie": self.Cookie,
            "Content-Type": "application/json"
        }
        
        response = requests.post(url + "removePersonal", headers=headers, json=self.project_data_positive())
        return response
