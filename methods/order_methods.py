import requests
import allure
from urls import ORDERS_URL

class OrderMethods:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(headers=None, ingredients=None):
        url = ORDERS_URL
        payload = {}
        if ingredients:
            payload['ingredients'] = ingredients
        if headers:
            return requests.post(url, json=payload, headers=headers)
        return requests.post(url, json=payload)
    
    @staticmethod
    @allure.step("Получение заказов пользователя")
    def get_user_orders(headers):
        return requests.get(ORDERS_URL, headers=headers)
    