import vk_api
import random
import openpyxl
import requests
from pyautogui import *
from multiprocessing import Pool
class Vk_prosto_repost:
    def __init__(self,group_id, post_id,group_full, access_token):
        self.group_id=group_id
        self.post_id=post_id
        self.group_full=group_full
        self.access_token=access_token
    def repost(self):  # полный post_id 32129227_117356
        # Выполняем GET-запрос к API ВКонтакте
        response = requests.get(f"https://api.vk.com/method/users.get?access_token={self.access_token}&v=5.131")
    # Проверяем успешность запроса
        if response.status_code == 200:
            print(response.json())
            user_id = response.json()["response"][0]["id"]
            print(f"Ваш ID пользователя: {user_id}")
        else:
            print("Не удалось получить ID пользователя.")

        # Выполняем GET-запрос к API ВКонтакте
        response = requests.get(
            f"https://api.vk.com/method/wall.get?owner_id={user_id}&access_token={self.access_token}&v=5.131&filter=copy")
    # Проверяем успешность запроса
        spisok_id_repost = []
        if response.status_code == 200:
            posts = response.json()["response"]["items"]
            for post in posts:
                if "copy_history" in post:
                    repost = post["copy_history"][0]
                    repost_id = repost["id"]
                    spisok_id_repost.append(repost_id)
            #print(spisok_id_repost, repost_id)
        else:
            print("Не удалось получить записи.")
    # Выполняем репост, если его нет в списке репостов
        if self.post_id not in spisok_id_repost:
            url = 'https://api.vk.com/method/wall.repost'
            params = {
                'object': f'wall-{self.group_full}',  # сюда надо 32129227_117356 в таком формате
                'access_token': self.access_token,
                'v': '5.131'
            }
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()  # Проверяем код ответа

                data = response.json()
                if 'response' in data:
                    print('Запись успешно репостнута на вашу страницу!')
                elif 'error' in data:
                    error_code = data['error']['error_code']
                    error_msg = data['error']['error_msg']
                    print(f'Ошибка при репосте. Код ошибки: {error_code}. Сообщение об ошибке: {error_msg}')
                else:
                    print('Произошла неизвестная ошибка.')
            except requests.exceptions.RequestException as e:
                print('Произошла ошибка во время запроса:', str(e))
        else:
            print('Повторный репост, репост не выполнен')