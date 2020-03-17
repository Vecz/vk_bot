# -*- coding: utf-8 -*-
import os
import json
import vk_api
import requests
from modules.start import start
from modules.login import login
from modules.prim_generate import prim_generate
from modules.get_msg import get_msg
from modules.mythread import MyThread
from collections import deque


if __name__ == '__main__':
    th = []
    work = []
    vk = start(vk_api, json)
    key,server,ts = login(vk)
    primery = prim_generate(json)
    users = {}
    try:
        with open('users.json', 'r') as f:
            scored = json.load(f)
    except:
        scored = dict()
    cpu = os.cpu_count()
    print("Укажите количество потоков для работы программы(по умолчанию:{})".format(cpu))
    print('---'*20)
    i = input()
    if(i != ""):
        cpu = int(i)
    print('---'*20)
    for i in range(cpu):
        work.append(deque())
        th.append(MyThread(vk,primery,server,key,work[i],users,scored))
        th[i].daemon = True
        th[i].start()
    i = 0
    try:
        while 1:
            try:
                r, ts, boole = get_msg(server, key, ts, requests)
                idi = r.json()['updates'][0]['object']['from_id']
                text = r.json()['updates'][0]['object']['text']
                if(idi in users.keys() and users[idi] !=2):
                    work[i].append([idi,text])
                    i+=1
                elif(idi in users.keys() and users[idi] == 2):
                    work[i].append([idi, [r, 'la']])
                    i+=1
                else:
                    users[idi] = 0
                    work[i].append([idi,text])
                    i+=1
                i%=cpu
            except Exception as e:

                ...
    except:
            with open('users.json','w') as f:
                json.dump(scored, f)     
            print()       
            print('---'*20)
            print('Работа завершена.\n{}\nДо новых встреч!'.format('-'*60))
            print('---'*20)
    finally:
            #vk.method('groups.disableOnline', {'group_id':109269019})
            audio = os.listdir('audio')
            png = os.listdir('png')
            for i in audio:
                os.remove('audio/'+i)
            for i in png:
                os.remove('png/'+i)
            exit(200)
