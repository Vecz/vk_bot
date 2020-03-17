def get_stat(scored,idi, lineplot, plt, os):
    try:
        score = scored[str(idi)]
        graph = lineplot(list(score['score'].keys()), list(score['score'].values()),id = idi,plt= plt, os = os)
        all = score['all']
        alls = sum(list(score['score'].values()))
        text = 'Ваша статистика:\nВсего заданий:{}\nВсего решено:{}\nПроцент рещений:{}%\nГрафическое представление:'.format(all,alls,'{}'.format(alls/all*100)[:4])
        return text
    except Exception as e:
        text = 'Статистика для вашего аккаунта не найдена.\nПопробуйте запустить одну из мини-игр, чтобы она появилась.'
        return text