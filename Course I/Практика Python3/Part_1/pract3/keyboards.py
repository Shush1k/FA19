from telebot import types
import datetime


def top_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=False, row_width=1)
    big_theatre = types.KeyboardButton('🏆Большой театр')
    small_theatre = types.KeyboardButton('🏅Малый театр')
    pushkin_theatre = types.KeyboardButton('🥇Театр им. А.С. Пушкина')
    chehov_theatre = types.KeyboardButton('🥈МХТ им. А.П. Чехова')
    gogol_theatre = types.KeyboardButton('🥉Гоголь-центр')
    markup.add(
        big_theatre, small_theatre, pushkin_theatre,
        chehov_theatre, gogol_theatre
    )
    return markup


def filters_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=False, row_width=1)
    today = types.KeyboardButton('‼️Сегодня')
    tomorrow = types.KeyboardButton('❗️Завтра')
    select = types.KeyboardButton('📆Выбрать дату')
    back = types.KeyboardButton('🔙Назад🔙')
    markup.add(today, tomorrow, select, back)
    return markup


def now_markup(state=0):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=False, row_width=7)
    back = types.KeyboardButton('🔙Назад🔙')
    m = types.KeyboardButton('📆'+str(datetime.datetime.now().strftime('%B')))
    right = types.KeyboardButton('➡️')
    b1 = types.KeyboardButton('1')
    b2 = types.KeyboardButton('2')
    b3 = types.KeyboardButton('3')
    b4 = types.KeyboardButton('4')
    b5 = types.KeyboardButton('5')
    b6 = types.KeyboardButton('6')
    b7 = types.KeyboardButton('7')
    b8 = types.KeyboardButton('8')
    b9 = types.KeyboardButton('9')
    b10 = types.KeyboardButton('10')
    b11 = types.KeyboardButton('11')
    b12 = types.KeyboardButton('12')
    b13 = types.KeyboardButton('13')
    b14 = types.KeyboardButton('14')
    b15 = types.KeyboardButton('15')
    b16 = types.KeyboardButton('16')
    b17 = types.KeyboardButton('17')
    b18 = types.KeyboardButton('18')
    b19 = types.KeyboardButton('19')
    b20 = types.KeyboardButton('20')
    b21 = types.KeyboardButton('21')
    b22 = types.KeyboardButton('22')
    b23 = types.KeyboardButton('23')
    b24 = types.KeyboardButton('24')
    b25 = types.KeyboardButton('25')
    b26 = types.KeyboardButton('26')
    b27 = types.KeyboardButton('27')
    b28 = types.KeyboardButton('28')
    b29 = types.KeyboardButton('29')
    b30 = types.KeyboardButton('30')
    b31 = types.KeyboardButton('31')
    blank = types.KeyboardButton(' ')
    markup.row(back)
    if state == 1:
        m = str((datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%B'))
        m = types.KeyboardButton('🗓'+m)
        left = types.KeyboardButton('⬅️')
        markup.row(left, m, right)
    else:
        markup.row(m, right)
    markup.add(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13,
               b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24,
               b25, b26, b27, b28, b29, b30, b31, blank, blank, blank, blank)
    return markup


if __name__ == '__main__':
    pass
