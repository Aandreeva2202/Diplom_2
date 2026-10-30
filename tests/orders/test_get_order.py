import allure
from methods.order_methods import OrderMethods
from messages import UNAUTHORISED


class TestGetOrder:

    @allure.title("Получение заказов")
    @allure.description("Получение заказов авторизованным пользователем")
    def test_get_user_orders_authorized(self, create_user):
        token = create_user['accessToken']
        headers = {"Authorization": token}
        
        response = OrderMethods.get_user_orders(headers)
        response_data = response.json()
            
        assert response.status_code == 200 and response_data['success'] is True and 'orders' in response_data

    @allure.title("Получение заказов")
    @allure.description("Попытка получения заказов неавторизованным пользователем")
    def test_get_user_orders_unauthorized(self):
        response = OrderMethods.get_user_orders({})
        response_data = response.json()

        assert response.status_code == 401 and response_data['success'] is False and response_data['message'] == UNAUTHORISED
