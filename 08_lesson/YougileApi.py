import requests
from config import login, password, company_id, key_token, project_id
import config


class YougileApi:

    def __init__(self, url):
        self.url = url

    def get_company_list(self):
        authorization = {
            "login": login,
            "password": password
        }
        resp = requests.post(self.url + "/auth/companies", json=authorization)
        json_data = resp.json()
        company_id = json_data['content'][0]['id']
        config.company_id = company_id
        return resp

    def create_key(self):
        making = {
            "login": login,
            "password": password,
            "companyId": company_id
        }
        resp = requests.post(self.url + "/auth/keys", json=making)
        json_data = resp.json()
        key_token = json_data['key']
        config.key_token = key_token
        return resp

    def get_create_project_positive(self):
        project = {
            "title": "Крутое название"
        }
        my_headers = {}
        my_headers['Authorization'] = "Bearer" + key_token
        my_headers['Content-type'] = "application/json"
        resp = requests.post(self.url + "/projects", json=project, headers=my_headers)
        json_data = resp.json()
        project_id = json_data['id']
        config.project_id = project_id
        return resp

    def get_create_project_negative(self):  # В теле запроса отутствует наименование проекта
        project = {
            "title": ""
        }
        my_headers = {}
        my_headers['Authorization'] = "Bearer" + key_token
        my_headers['Content-type'] = "application/json"
        resp = requests.post(self.url + "/projects", json=project, headers=my_headers)
        json_data = resp.json()
        project_id = json_data['id']
        config.project_id = project_id
        return resp

    def get_put_project_positive(self):
        project = {
            "title": "Крутое название"
        }
        my_headers = {}
        my_headers['Authorization'] = "Bearer" + key_token
        my_headers['Content-type'] = "application/json"
        resp = requests.post(self.url + "/projects"/project_id, json=project, headers=my_headers)
        return resp

    def get_put_project_negative(self):  # В запросе неверно указан id
        project = {
            "title": "Крутое название"
        }
        my_headers = {}
        my_headers['Authorization'] = "Bearer" + key_token
        my_headers['Content-type'] = "application/json"
        resp = requests.post(self.url + "/projects", json=project, headers=my_headers)
        return resp

    def get_search_project_id_positive(self):
        my_headers = {}
        my_headers['Authorization'] = "Bearer" + key_token
        my_headers['Content-type'] = "application/json"
        resp = requests.post(self.url + "/projects"/project_id, headers=my_headers)
        return resp

    def get_search_project_id_negative(self):  # Неверный указан токен
        my_headers = {}
        my_headers['Authorization'] = "Bearer"
        my_headers['Content-type'] = "application/json"
        resp = requests.post(self.url + "/projects"/project_id, headers=my_headers)
        return resp
