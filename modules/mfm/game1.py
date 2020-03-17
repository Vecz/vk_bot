def mathematic(primery, text, score, idi, random, time):
    now = time.localtime()
    date,month = now[2],now[1]
    try:
        score[idi]['all'] +=1
    except:
        score[idi]['all'] = 1
    if(text == str(eval(score[idi]['prim']))):
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
        msg = 'Вы ошиблись.\nВерный ответ:{}\nТекущий счет: {}'.format(str(eval(score[idi]['prim'])) ,score[idi]['score']['{}.{}'.format(date,month)])
    score[idi]['prim'] = random.choice(list(primery.keys()))
    return score[idi]['prim'],msg