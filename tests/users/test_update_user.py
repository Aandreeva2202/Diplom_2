import allure
from methods.user_methods import UserMethods
from messages import UNAUTHORISED


class TestUpdateUser:

    @allure.title("Обновление данных")
    @allure.description("Обновление email с авторизацией")
    def test_update_email_authorized(self, create_user):
        token = create_user['accessToken']
        original_email = create_user['user']['email']
        new_email = f"updated_{original_email}"
        headers = {"Authorization": token}
        response = UserMethods.update_user(
                    headers, 
                    {"email": new_email}
                )
        assert response.status_code == 200 and response.json()['success'] is True and response.json()['user']['email'] == new_email

    @allure.title("Обновление данных")
    @allure.description("Обновление name с авторизацией")
    def test_update_name_authorized(self, create_user):
        token = create_user['accessToken']
        new_name = "НовоеИмя"
        headers = {"Authorization": token}
        response = UserMethods.update_user(
            headers, 
            {"name": new_name}
        )
        assert response.status_code == 200 and response.json()['success'] is True and response.json()['user']['name'] == new_name

    @allure.title("Обновление данных")
    @allure.description("Попытка обновления email без авторизации")
    def test_update_email_unauthorized(self):
        response = UserMethods.update_user({}, {"email": "test@test.com"})
        assert response.json()['message'] == UNAUTHORISED and response.status_code == 401

    @allure.title("Обновление данных")
    @allure.description("Попытка обновления name без авторизации")
    def test_update_name_unauthorized(self):
        response = UserMethods.update_user({}, {"name": "NewName"})
        assert response.json()['message'] == UNAUTHORISED and response.status_code == 401
