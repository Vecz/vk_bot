def cvet(idi, score, text,ph_idi, time, random):
    now = time.localtime()
    date,month = now[2],now[1]
    score[idi]['all']+=1
    if(text == ph_idi[score[idi]['prim']]):
        try:
            score[idi]['score']['{}.{}'.format(date,month)] +=1
        except:
            score[idi]['score']['{}.{}'.format(date,month)] =1
        msg = 'Все верно.\nТекущий счет: {}'.format(score[idi]['score']['{}.{}'.format(date,month)])
    else:
        try:
            score[idi]['score']['{}.{}'.format(date,month)] -=1
        except:
            score[idi]['score']['{}.{}'.format(date,month)] =-1
        msg = 'Вы ошиблись.\nВерный ответ:{}\nТекущий счет: {}'.format(ph_idi[score[idi]['prim']] ,score[idi]['score']['{}.{}'.format(date,month)])
    score[idi]['prim'] = random.choice(list(ph_idi.keys()))
    return msg
    