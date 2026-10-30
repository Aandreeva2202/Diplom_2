import pytest
import requests
from urls import INGREDIENTS_URL
from methods.user_methods import UserMethods


@pytest.fixture(scope="function")
def user_data():
    return UserMethods.generate_user_data()

# Фикстура для создания пользователя
@pytest.fixture(scope="function")
def create_user(user_data):
    response = UserMethods.register_user(user_data)
    user = response.json()
    
    yield {
        'user': user['user'],
        'accessToken': user['accessToken'],
        'refreshToken': user['refreshToken']
    }
    
    # accessToken уже содержит префикс "Bearer "
    UserMethods.delete_user({"Authorization": user['accessToken']})

@pytest.fixture(scope="function")
def valid_ingredients():
    # Получаем список всех ингредиентов
    response = requests.get(INGREDIENTS_URL)
    
    data = response.json()
    
    ingredients_list = data['data']
    ingredient_ids = [ingredient['_id'] for ingredient in ingredients_list]
    return ingredient_ids
