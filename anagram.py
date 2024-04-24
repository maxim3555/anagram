import os
import random
import openpyxl
import requests
import openpyxl

# Указываем параметры запроса
class Vk_prosto_anagram:
    def __init__(self,group_id, post_id,group_full, access_token,schet):
        self.group_id=group_id
        self.post_id=post_id
        self.group_full=group_full
        self.access_token=access_token
        self.schet=schet

    def spisok_s_komentov_1000(self):
        count = 1000  # Количество комментариев, которые нужно получить
        offset = 0  # Сдвиг для получения следующей порции комментариев
        all_comments = []  # Список для хранения всех комментариев
        while True:
            url = f'https://api.vk.com/method/wall.getComments?owner_id=-{self.group_id}&post_id={self.post_id}&v=5.131&access_token={self.access_token}&count={count}&sort=desc&offset={offset}'
            response_json = requests.get(url).json()
            comments_data = response_json['response']['items']
            if not comments_data:
                break  # Прекращаем цикл, если больше нет комментариев
            all_comments.extend(comments_data)  # Добавляем полученные комментарии в общий список
            offset += count  # Увеличиваем сдвиг для следующей итерации
            if len(all_comments) >= 1000:
                break  # Прекращаем цикл, если получили достаточно комментариев
        comments_data = list(comment for comment in all_comments[:int(
            input('введите колличечтво коментариев'))])  # Ограничиваем список комментариев до 1000
        print('функция конец',len(comments_data))
        return comments_data  # посылается полный список,если нужно 'id''text'то тут все

    def podkoment(self):  # тут происходит поиск коментариев для игры анаграмм
        comment_id=Vk_prosto_anagram.spisok_s_komentov_1000(self)

        podkoment_spis = []
        for i in range(len(comment_id)):
            a = comment_id[i]['id']
            response = requests.get(
                f'https://api.vk.com/method/wall.getComments?owner_id=-{self.group_id}&post_id={self.post_id}&comment_id={a}&v=5.131&access_token={self.access_token}')
            comments_data = response.json()
            # Проверяем успешность выполнения запроса
            if 'error' in comments_data:
                print('Ошибка при получении комментариев:', comments_data['error']['error_msg'])
            else:
                # Получаем список комментариев из ответа API
                comments_list = comments_data['response']['items']
                print(comments_list)
                # Выводим текст каждого комментария
                for comment in comments_list:
                    text = comment['text']
                    if 'Такое слово действительно существует' in text:
                        podkoment_spis.append(comment_id[i]['text'])
            # Записываем содержимое списка в файл
        with open(f'podkoment_spis_baza.txt', 'w', encoding='utf-8') as file:
            for item in podkoment_spis:
                if item.strip() and len(item) < 15:
                    file.write(item + '\n')

        with open('podkoment_spis_baza.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            processed_lines = list(set(line.lower() for line in lines if len(line) <= 15))

        with open('podkoment_spis_baza.txt', 'w', encoding='utf-8') as file:
            file.writelines(processed_lines)
        podkoment_spis = processed_lines
        return podkoment_spis

    def compare_and_return_word(self):
        base_file_path = 'podkoment_spis_baza.txt'
        other_file_path = f'podkoment_spis{self.schet}.txt'
        # Чтение базового текстового файла
        with open(base_file_path, 'r', encoding='utf-8') as base:
            base_words = base.read().splitlines()

        # Чтение другого текстового файла

        with open(f'{other_file_path}', 'r', encoding='utf-8') as other:
            other_words = set(other.read().splitlines())
        random.shuffle(base_words)
        # Поиск первого слова, которого нет в другом файле
        for word in base_words:
            if word in other_words:
                continue  # Переходим к следующему слову
            else:
                # Запись слова в новый файл
                with open(other_file_path, 'a', encoding='utf-8') as new:
                    new.write(word + '\n')
                return word  # Возвращаем слово и прекращаем выполнение


