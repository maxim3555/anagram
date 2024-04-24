import vk_api
import random
import openpyxl
import requests
from pyautogui import *
from multiprocessing import Pool
class Vk_prosto_like:
    def __init__(self,group_id, post_id,group_full, access_token):
        self.group_id=group_id
        self.post_id=post_id
        self.group_full=group_full
        self.access_token=access_token

    def like(self):

        url = f'https://api.vk.com/method/likes.add?type=post&owner_id=-{self.group_id}&item_id={self.post_id}&access_token={self.access_token}&v=5.131'
        response = requests.get(url)
        if response.status_code == 200:
            print('Post liked successfully!')
        else:
            print('Error liking post:', response.text)

