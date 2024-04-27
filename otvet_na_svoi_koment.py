import random
import os
import openpyxl
import requests



class Vk_prosto_otvet_na_svoi_koment:

    def __init__(self,group_id, post_id,group_full, access_token,schet):
        self.group_id=group_id
        self.post_id=post_id
        self.group_full=group_full
        self.access_token=access_token
        self.schet=schet

        #self.id_user=Vk_prosto_anagram.list1['G'][schet].value

    def leave_reply(self,parent_comment_id,text):#функция отправляет комент на свой коментарий
        url = 'https://api.vk.com/method/wall.createComment'
        params = {
            'owner_id': self.group_id,
            'post_id': self.post_id,
            'reply_to_comment': parent_comment_id,  # ID родительского комментария
            'message': text,
            'access_token': self.access_token,
            'v': '5.131'
        }
        response = requests.post(url, params=params)

        if response.status_code == 200:
            print("Комментарий успешно оставлен!")
        else:
            print("Произошла ошибка при оставлении комментария.")