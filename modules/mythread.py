import random
import threading
import requests
import time
import os
import vk_api
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from vk_api.utils import get_random_id
from modules.mfm.lineplot import lineplot
from modules.mfm.key_gen import key_gen
from modules.mfm.write_msg import write_msg
from modules.mfm.get_stat import get_stat
from modules.mfm.upload import upload_graph
from modules.mfm.audio_down import audio_down
from modules.mfm.game1 import mathematic
from modules.mfm.game2 import cvet
class MyThread(threading.Thread):
    '''Наследование класса, для создания потока.'''
    def __init__(self, vk, primery,server,key,q,users,scored):
        '''Инициация'''
        threading.Thread.__init__(self)
        self.vk = vk 
        self.primery = primery
        self.server = server
        self.key = key
        self.q = q
        self.users = users
        self.scored = scored
        self.ph_idi= {456239020:'Синий',456239021:'Зеленый',456239022:"Красный",456239023:'Синий',456239024:'Зеленый',456239025:"Красный",456239026:'Синий',456239027:'Зеленый',456239028:"Красный"}
        self.cv = key_gen(cho=['Синий','Зеленый','Красный'])
 
    def run(self):
        '''Функция самого запуска потока'''
        while 1:
            if(len(self.q) > 0):
                u = self.q.popleft()
                idi = u[0]
                text = u[1]
                if(self.users[idi] == 1):
                    self.q.append(u)
                    continue
                elif(self.users[idi] == 0):
                    self.users[idi] = 1
                if(text == 'Старт' and self.users[idi] == 1):
                    text = "Добро пожаловать!"
                    write_msg(get_random_id,self.vk,idi, text,key_gen(start=True))
                    self.users[idi] = 0
                elif (text == "Справка" and self.users[idi] == 1):
                    text = "Я бот, задача которого помогать людям развивать способности своего мозга. Я имею в своем арсенале 2 мини-игры.\n1)Устный счёт.\nЗдесь вам нужно выбрать 1 из 4 возможных примеров для решения поставленной задачи. Игра расчитана на устный счёт.\n2)Зоркий глаз\nВам нужно правильно указать цвет, которым будет написан текст.Чтобы был эффект, ответы нужно давать с максимальной скоростью.\nТак же у меня появилась функция, которая позволяет скачать песню на устройство, отправив ее боту. Песня скачается в формате который пользователь выбирает сам."
                    write_msg(get_random_id,self.vk,idi, text,key_gen(start=True))
                    self.users[idi] = 0
                elif (text == "Устный счёт" and self.users[idi] == 1):
                    prim = random.choice(list(self.primery.keys()))
                    text = 'Пример:{}'.format(prim)
                    write_msg(get_random_id,self.vk,idi, text,key_gen(ans = self.primery[prim]))
                    self.users[idi] = 3
                    try:
                        self.scored[str(idi)]['prim'] = prim
                    except:
                        self.scored[str(idi)] = {'prim':prim,'score': {}, 'all': 0}
                elif (text == "Зоркий глаз"  and self.users[idi] == 1):
                    img_id = random.choice(list(self.ph_idi.keys()))
                    gen = 'photo-109269019_{}'.format(img_id)
                    write_msg(get_random_id,self.vk,idi,at = gen,key=self.cv)
                    self.users[idi] = 4
                    try:
                        self.scored[str(idi)]['prim'] = img_id
                    except:
                        self.scored[str(idi)] = {'prim':img_id,'score': {}, 'all': 0}
                elif (text == "Мой профиль"  and self.users[idi] == 1):
                    text = get_stat(self.scored,idi, lineplot, plt, os)
                    if(text != 'Статистика для вашего аккаунта не найдена.\nПопробуйте запустить одну из мини-игр, чтобы она появилась.'):
                        up = upload_graph(self.vk,idi, vk_api, os)
                        write_msg(get_random_id,self.vk,idi, text,key_gen(start=True),'photo{}_{}'.format(up[0]['owner_id'],up[0]['id']))
                    else:
                        write_msg(get_random_id,self.vk,idi,text,key = key_gen(start=True))
                    self.users[idi] = 0
                elif (text == 'Скачать трек'  and self.users[idi] == 1):
                    text = 'Прикрепите к сообщению трек. ВК убрали возможность отправки большинства распространенных форматов файлов. Поэтому, после получения файла необходима будет изменить расширение (.la) на (.mp3) или любое другое, удобное для вас.'
                    self.users[idi] = 2
                    write_msg(get_random_id,self.vk, idi, text, key = key_gen(flac = True))
                elif (self.users[idi] == 2):
                    if(text[0].json()['updates'][0]['object']['text'] != 'Назад'):
                        try:
                            at = audio_down(os,requests,vk_api,self.vk, idi, text[0], text[1])
                            text = 'Ваш трек в формате '+(text[1])
                            write_msg(get_random_id,self.vk,idi,text,key = key_gen(start=True),at = 'doc{}_{}'.format(at['doc']['owner_id'],at['doc']['id']))
                        except:
                            text = "Что-то пошло не так"
                            write_msg(get_random_id,self.vk, idi,text, key = key_gen(start = True))    
                    else:
                        text = 'Главное Меню'
                        write_msg(get_random_id,self.vk, idi,text, key = key_gen(start = True))
                    self.users[idi] = 0
                elif (self.users[idi] == 3):
                    if(text != 'Назад'):
                        prim,text = mathematic(self.primery, text, self.scored,str(idi),random, time)
                        write_msg(get_random_id,self.vk,idi,text)
                        text = 'Пример:{}'.format(prim)
                        write_msg(get_random_id,self.vk, idi, text, key_gen(ans = self.primery[prim]))
                    else:
                        text = 'Главное Меню'
                        write_msg(get_random_id,self.vk, idi,text, key = key_gen(start = True))
                        self.users[idi] = 0
                elif (self.users[idi] == 4):
                    if(text!= 'Назад'):
                        text = cvet(str(idi),self.scored,text,self.ph_idi, time, random)
                        gen = 'photo-109269019_{}'.format(self.scored[str(idi)]['prim'])
                        write_msg(get_random_id,self.vk,idi,text,at = gen,key=self.cv)
                    else:
                        text = 'Главное Меню'
                        write_msg(get_random_id,self.vk, idi,text, key = key_gen(start = True))
                        self.users[idi] = 0
                else:
                    text = 'Работа завершена'
                    write_msg(get_random_id,self.vk, idi, text, key = key_gen(last = True))
                    self.users[idi] = 0
