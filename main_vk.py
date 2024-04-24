import random
import os
import openpyxl
import requests
from multiprocessing import Pool
import time
from koment_odin import Vk_prosto_koment_odin
from anagram import Vk_prosto_anagram
from podpiska_vk import Vk_prosto_podpiska
from like import Vk_prosto_like
from repost_vk import Vk_prosto_repost


schet = int(input())
schet2 = 1
schet3 =0

block_pod_like_rep =0 #1 лайк репост и подписка
nabor_coment=0 #1 записываем в базовый тхт
osnovnoi_cikl=1 #1 запусаем цикл

book = openpyxl.open('telegramm.xlsx')
list1 = book.active
group_full='144958594_29622494'#магнит
group_id, post_id = map(int, group_full.split("_"))
group_id_str, post_id_str = group_full.split("_")


#инициализация лайк,подписка,репост
#основной цикл
while True:
    vk_coment_odin=Vk_prosto_koment_odin(group_id=group_id_str, post_id=post_id_str, group_full=group_full,
                                 access_token=list1['J'][schet].value)
    vk_anagram=Vk_prosto_anagram(group_id=group_id_str, post_id=post_id_str, group_full=group_full,
                                 access_token=list1['J'][schet].value,schet=schet)
    vk_podpiska = Vk_prosto_podpiska(group_id=group_id, post_id=post_id, group_full=group_full,
                                     access_token=list1['J'][schet].value)
    vk_like = Vk_prosto_like(group_id=group_id, post_id=post_id, group_full=group_full,
                             access_token=list1['J'][schet].value)
    vk_repost = Vk_prosto_repost(group_id=group_id, post_id=post_id, group_full=group_full,
                                 access_token=list1['J'][schet].value)
    if block_pod_like_rep==1:
        #если нужен подписка
            vk_podpiska.podpiska()
        #если нужно репост
            vk_repost.repost()
        #если нужен лайк
            vk_like.like()
    if nabor_coment==1:
    #нужно записать колличество коментов в podkoment_spis_baza.txt
        vk_anagram.podkoment()
    if osnovnoi_cikl==1:
    #получить слово для отправки,тут записывается это слово в тхт нужного аккаунта
        slovo=vk_anagram.compare_and_return_word()
    #функция отправки
        vk_coment_odin.coment(slovo)#(random.choice(spisok_coment))
        time.sleep(random.uniform(3, 10))





    schet+=1
    schet3+=1
    print(schet)
    if schet==17:
        schet=1
        schet2+=1
        if schet2==2000:
            # shutdown_command = "shutdown /s /t 00"
            # os.system(shutdown_command)
            break


