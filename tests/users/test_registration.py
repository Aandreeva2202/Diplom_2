import pytest
import allure
from methods.user_methods import UserMethods


class TestRegistaration:

    @allure.title("Регистрация")
    @allure.description("Успешная регистрация")
    def test_register_success(self, user_data):
        response = UserMethods.register_user(user_data)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title("Регистрация")
    @allure.description("Регистрация существующего пользователя")
    def test_register_existing(self, create_user, user_data):
        existing_user = {
        "email": create_user['user']['email'],
        "password": user_data['password'],  # Добавляем пароль из исходных данных
        "name": create_user['user']['name']
        }
    
        response = UserMethods.register_user(existing_user)
        assert response.status_code == 403 and response.json()['message'] == "User already exists"

    @allure.title("Регистрация")
    @allure.description("Регистрация без обязательных полей")
    def test_register_missing_fields(self, user_data):
        del user_data['password']
        response = UserMethods.register_user(user_data)
        assert response.status_code == 403 and response.json()['message'] == "Email, password and name are required fields"
