import requests
import os
def get_part_info(article):
    API_URL = " https://api.forum-auto.ru/"
    login = os.getenv("LOGIN_API")
    password = os.getenv("PASS_API")
    
    # Параметры запроса (артикул, который мы ищем)
    params = {
        'login': login,
        'pass': password,
        'art': article
    }
    
    print(f"--- Ищу информацию по артикулу: {article} ---")
    
    try:
        response = requests.get(API_URL, params=params)
        # Если склад ответил 200 (ОК)
        if response.status_code == 200:
            data = response.json() # Превращаем ответ в список запчастей
            return data
        else:
            print(f"Ошибка API: {response.status_code}")
            return None
    except Exception as e:
        print(f"Не удалось подключиться к складу: {e}")
        return None


info = get_part_info("OC90")

if info:
    for item in info:
        print(f"Название: {item.get('name')}")
        print(f"Бренд: {item.get('brand')}")
        print(f"Цена склада: {item.get('price')} руб.")
        print(f"Наличие: {item.get('num')} шт.")
        print("-" * 30)
else:
    print("Запчасть не найдена или API еще не активно.")