import random
import string
import requests
import allure
from urls import REGISTER_URL, LOGIN_URL, USER_URL

class UserMethods:

    @staticmethod
    @allure.step("Генерация данных пользователя")
    def generate_user_data():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
    
        # генерируем логин, пароль и имя курьера
        email = f"test_{generate_random_string(5)}@test.com"
        password = generate_random_string(10)
        name = generate_random_string(10)
    
        # собираем словарь
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        # возвращаем словарь
        return payload 
    
    @staticmethod
    @allure.step("Регистрация пользователя")
    def register_user(user_data):
        return requests.post(REGISTER_URL, json=user_data)
    
    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(credentials):
        return requests.post(LOGIN_URL, json=credentials)
    
    @staticmethod
    @allure.step("Обновление данных пользователя")
    def update_user(headers, data):
        return requests.patch(USER_URL, headers=headers, json=data)
    
    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(headers):
        return requests.delete(USER_URL, headers=headers)
