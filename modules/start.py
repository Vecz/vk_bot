
def start(vk_api, json):
    '''Функция, используемая для получения данных входа(токена) к вк и последующего входа'''
    try:
        with open('log.json','r') as f:
            x = json.load(f)
        print('---'*20)
        print('Welcome back')
        print('---'*20)
    except:
        x = input('Введите ваш код доступа:\n')
        with open('log.json', 'w') as f:
            json.dump(x,f)
    try:        
        vk = vk_api.VkApi(token=x)
        print('Подключение установленно')
        print('---'*20)
        return vk
    except Exception as e:
        print('---'*20)
        print('Что-то пошло не так:',e)
        print('---'*20)
        exit(500)
