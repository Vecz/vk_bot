def login(vk):
    '''Авторизация в сообществе.'''
    abra = vk.method('groups.getLongPollServer', {'group_id': 109269019})
    key = abra['key']
    server = abra['server']
    ts = abra['ts']
    print('Группа подключена')
    print('---'*20)
    #vk.method('groups.enableOnline', {'group_id':109269019})
    return key,server,ts
