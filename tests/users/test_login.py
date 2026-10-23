import allure
from methods.user_methods import UserMethods


class TestLogin:

    @allure.title("Авторизация")
    @allure.description("Успешный логин")
    def test_login_success(self, user_data, create_user):
        credentials = {
            "email": create_user['user']['email'],
            "password": user_data['password']
        }
        response = UserMethods.login_user(credentials)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title("Авторизация")
    @allure.description("Неверный логин/пароль")
    def test_login_invalid(self, create_user):
        credentials = {
            "email": create_user['user']['email'],
            "password": "wrong_password"
        }
        response = UserMethods.login_user(credentials)
        assert response.status_code == 401 and response.json()['message'] == "email or password are incorrect"
