import allure
from methods.order_methods import OrderMethods


class TestCreateOrder:

    @allure.title("Создание заказа")
    @allure.description("Успешное создание заказа с авторизацией")
    def test_create_order_authorized(self, create_user, valid_ingredients):
        token = create_user['accessToken']
        headers = {"Authorization": token}
        response = OrderMethods.create_order(
            headers=headers,
            ingredients=[valid_ingredients[0]]
        )
        assert response.status_code == 200 and response.json()['success'] is True and 'order' in response.json()

    @allure.title("Создание заказа")
    @allure.description("Попытка создания заказа без авторизации")
    def test_create_order_unauthorized(self, valid_ingredients):
        response = OrderMethods.create_order(ingredients=[valid_ingredients[0]])
        # скорее всего баг, по документации ожидается другое.
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title("Создание заказа")
    @allure.description("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, create_user, valid_ingredients):
        token = create_user['accessToken']
        headers = {"Authorization": token}
        response = OrderMethods.create_order(
            headers=headers,
            ingredients=valid_ingredients[:2]
        )
        assert response.json()['success'] is True and len(response.json()['order']['ingredients']) == 2

    @allure.title("Создание заказа")
    @allure.description("Попытка создания заказа без ингредиентов")
    def test_create_order_no_ingredients(self, create_user):
        token = create_user['accessToken']
        headers = {"Authorization": token}
        response = OrderMethods.create_order(headers=headers)
        assert response.status_code == 400 and response.json()['message'] == "Ingredient ids must be provided"

    @allure.title("Создание заказа")
    @allure.description("Создание заказа с неверным хешем ингредиента")
    def test_create_order_invalid_ingredient(self, create_user):
        token = create_user['accessToken']
        headers = {"Authorization": token}
        response = OrderMethods.create_order(
            headers=headers,
            ingredients=["invalid_id"]
        )
        assert response.status_code == 500
