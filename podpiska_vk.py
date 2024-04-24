import vk_api
import random
import openpyxl
import requests
from pyautogui import *
from multiprocessing import Pool
class Vk_prosto_podpiska:
    def __init__(self,group_id, post_id,group_full, access_token):
        self.group_id=group_id
        self.post_id=post_id
        self.group_full=group_full
        self.access_token=access_token
    def podpiska(self):
        url = 'https://api.vk.com/method/'
        params = {
            'group_id': self.group_id,
            'v': 5.131,
            'access_token': self.access_token
        }
        response = requests.post(url + "groups.isMember", params=params)
        if response.status_code == 200:
            data = response.json()
            print(data)
            if data['response'] == 1:
                print("Вы уже подписаны на эту группу.")
            else:
                response = requests.post(url + "groups.join", params=params)
                if response.status_code == 200:
                    print("Вы успешно подписались на группу!")
                else:
                    error_msg = response.json()['error']['error_msg']
                    print(f"Ошибка при выполнении запроса: {error_msg}")
        else:
            print("Ошибка при выполнении запроса.")