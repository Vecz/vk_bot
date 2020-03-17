from vk_api.keyboard import VkKeyboard, VkKeyboardColor
def key_gen(ans=None,last=None,start=None,cho = None, flac = None):
    '''Генерация клавиатуры:
     ans - Для устного счета(4 варианта ответа).
     last - Кнопка старт,
     start - Главное меню(устный счет, Зоркий глаз, Профиль, Статистика, etc),
     cho - Зоркий глаз(цвета: Красный,Зеленый,Синий)'''
    if ans != None:
        keyboard = VkKeyboard(one_time=True)

        keyboard.add_button('{}'.format(ans[0]), color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('{}'.format(ans[1]), color=VkKeyboardColor.POSITIVE)

        keyboard.add_line() 
        keyboard.add_button('{}'.format(ans[2]), color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('{}'.format(ans[3]), color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Назад',color=VkKeyboardColor.NEGATIVE)
    elif last != None:
        keyboard = VkKeyboard(one_time=False)

        keyboard.add_button('Старт', color=VkKeyboardColor.POSITIVE)
    elif start != None:
        keyboard = VkKeyboard(one_time=True)

        keyboard.add_button('Устный счёт', color=VkKeyboardColor.POSITIVE)
        
        keyboard.add_line()

        keyboard.add_button('Зоркий глаз', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()

        keyboard.add_button('Справка', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()

        keyboard.add_button('Мой профиль', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()

        keyboard.add_button('Скачать трек', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()

        keyboard.add_button('Стоп',color=VkKeyboardColor.NEGATIVE)
    elif flac!=None:
        keyboard = VkKeyboard(one_time=True)

        keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

    else:
        keyboard = VkKeyboard(one_time=True)

        keyboard.add_button('Красный', color=VkKeyboardColor.DEFAULT)
        
        keyboard.add_line()

        keyboard.add_button('Синий', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()

        keyboard.add_button('Зеленый', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()

        keyboard.add_button('Назад',color=VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()
    
