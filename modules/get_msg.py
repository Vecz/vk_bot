def get_msg(server, key, ts, requests):
    '''Получение сообщений в вк
        server - сервер для получения сообщений
        key - ключ доступа
    '''
    r = requests.get('{}?act=a_check&key={}&ts={}&wait=40'.format(server, key, ts))
    ts = r.json()['ts']
    try:
        if r.json()['updates'][0]['attachments'][0]['type'] == 'audio':
            return r,ts,True
    except Exception:
        return r, ts, False
