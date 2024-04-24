import random
import time

import openpyxl
#import pyautogui
import requests
#from pyautogui import *
from multiprocessing import Pool
class Vk_prosto_koment_odin:
    def __init__(self,group_id, post_id,group_full, access_token):
        self.group_id=group_id
        self.post_id=post_id
        self.group_full=group_full
        self.access_token=str(access_token)
    def coment(self,coment):
        url = f"https://api.vk.com/method/wall.get?owner_id=-{self.group_id}&count=10&access_token={self.access_token}&v=5.131"
        response = requests.get(url)
        data = response.json()
        print(coment)
        comment_text = coment

        # API endpoint for creating a wall comment
        url = f'https://api.vk.com/method/wall.createComment?owner_id=-{self.group_id}&post_id={self.post_id}&message={comment_text}&access_token={self.access_token}&v=5.131'
        #url = f'https://api.vk.com/method/wall.createComment?owner_id=154085847&post_id=30437531&message={comment_text}&access_token=vk1.a.gC3Zg11bZIT36LBC3hsMSo06ETrcioKxn9aQogvx2eBqxKPTpf_yJhrqxD6IN5SEXYDeR_RhgCuiB8ok5LFr69HZdRyJpBXG5kTJum2mlcWPWCo_sRgLKRXPfpY1-u3MePlrm233qMxAVVWAwfNxHDXdFXyiaH4R6mA4ItOL1zaMNYs4dsdK3mNhER1trFLtCNmA_XcWbmCRH7CYWroRxA&v=5.131'


        response = requests.get(url)

        print(response)
        if response.status_code == 200:
            print('Comment posted successfully!')
            return comment_text
        else:
            print('Error posting comment:', response.text)

    def coment_one(self, com):
        url = f"https://api.vk.com/method/wall.createComment?owner_id=-{int(self.group_id)}&post_id={int(self.post_id)}&message={com}&access_token={self.access_token}&v=5.131"
        response = requests.get(url)
        if response.status_code == 200:
            print('Comment posted successfully!')
        else:
            print('Error posting comment:', response.text)

