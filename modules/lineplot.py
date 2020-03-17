
def lineplot(x_data, y_data, x_label="Дата.", y_label="Кол-во верных ответов", title="Статистика пользователя ",id='123456', plt, os):
    _,ax = plt.subplots()
    for i in range(len(x_data)):
        plt.scatter(x_data[i],int(y_data[i]))
    ax.plot(x_data, y_data, lw = 2, color = '#539caf', alpha = 1)
    try:
        os.mkdir('png')
    except:
        ...
    ax.set_title(title+str(id))
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    full_path = os.path.join('png','{}.png'.format(id))
    plt.savefig(full_path, fmt='png')

