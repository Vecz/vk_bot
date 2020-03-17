def prim_generate(json):
    '''Генерирует(загружает) примеры и возвращает словарь формата 
        {пример:[ответ1,ответ2,ответ3,ответ4]}'''
    print('Поиск примеров')
    print('---'*20)
    primery = {}
    try:
        with open('primery.json','r') as f:
            primery = json.load(f)
        print('Примеры загружены')
        print('---'*20)
    except:
        import random
        print('Примеры не найдены')
        print('-'*60)
        znk = ['-','+','*','/']
        print('Генерация примеров')
        print('---'*20)
        for i in range(1,100):
            for q in range(1,100):
                for c in znk:
                    pre = '{}{}{}'.format(i,c,q)
                    if int(eval(pre)) == eval(pre) and eval(pre)>=0:
                        ans = ([int(eval(pre)),random.randint(-eval(pre)-10,eval(pre)+10),random.randint(-eval(pre)-10,eval(pre)+10), random.randint(-eval(pre)-10,eval(pre)+10)])
                        random.shuffle(ans)
                        primery[pre] = ans
        print('Примеры сгенерированы')
        print('---'*20)
        with open('primery.json','w') as f:
            json.dump(primery,f)
        print('Примеры сохранены')
        print('---'*20)
    return primery
