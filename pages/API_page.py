import requests

# Создание проектов
class CreateEvent:

    def __init__(self, url, Cookie):
        self.url = url
        self.Cookie = Cookie
        self.event_id = None

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
        headers = {
            "Cookie": self.Cookie,
            "Content-Type": "application/json"
        }
        
        response = requests.post(url + "createPersonal", headers=headers, json=self.project_data_positive)
        self.event_id = response.json()["data"]["payload"]["id"]
        return response

    # Функция создания проекта (негативный)
    def create_event_negative_color(self, url):
        headers = {
            "Cookie": self.Cookie,
            "Content-Type": "application/json"
        }
        
        response = requests.post(url + "createPersonal", headers=headers, json=self.project_data_negative_color)
        return response

    # Функция создания проекта (негативный)
    def create_event_negative_name(self, url):
        headers = {
            "Cookie": self.Cookie,
            "Content-Type": "application/json"
        }
        
        response = requests.post(url + "createPersonal", headers=headers, json=self.project_data_negative_name)
        return response

class ChangeEvent:

    def __init__(self, url, Cookie, event_id):
        self.url = url
        self.Cookie = Cookie
        self.event_id = event_id

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
        headers = {
            "Cookie": self.Cookie,
            "Content-Type": "application/json"
        }
        
        response = requests.post(url + "updatePersonal", headers=headers, json=self.project_data_positive())
        return response

class DeleteEvent:

    def __init__(self, url, Cookie, event_id):
        self.url = url
        self.Cookie = Cookie
        self.event_id = event_id

    def project_data_positive(self):
        project_data_positive = {
            "id": f"{self.event_id}",
            "startAt": "2025-04-23T02:30:00+07:00"
        }
        return project_data_positive

    # Функция удаления события (позитивный)
    def delete_event_positive(self, url):
        headers = {
            "Cookie": self.Cookie,
            "Content-Type": "application/json"
        }
        
        response = requests.post(url + "removePersonal", headers=headers, json=self.project_data_positive())
        return response
