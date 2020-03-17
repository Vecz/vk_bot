
def write_msg(get_random_id,vk, user_id, text=None, key=None,at = None):
    '''Отправка сообщения в вк
        vk - Переменная с авторизацией
        user_id - id получателя сообщения
        text- текст сообщения
        at- вложения
        key- клавиатура'''
    if key == None:
        #Вызов метода вк messages.send, который отправляет сообщения
        vk.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': get_random_id()})
    else:
        if at == None:
            vk.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': get_random_id(), 'keyboard':key})
        elif at !=None and text != None:
            vk.method('messages.send', {'user_id': user_id,'message':text, 'attachment': at, 'random_id': get_random_id(), 'keyboard':key})
        else:
            vk.method('messages.send', {'user_id': user_id, 'attachment': at, 'random_id': get_random_id(), 'keyboard':key})
