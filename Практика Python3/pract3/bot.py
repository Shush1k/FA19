import telebot
import keyboards
import random
import myparser
import datetime
# 909244409:AAGY_yL1-9nN6cVLSgO-RlRLUrRl28-7J3Q
# 848608026:AAG2Ot5u01DEB-FjFqk3s-0KZ14RjJvgMPY
TOKEN = '909244409:AAGY_yL1-9nN6cVLSgO-RlRLUrRl28-7J3Q'
bot = telebot.TeleBot(TOKEN)


def msg_format(date, name, about, image, where, count, price, buy, link_where, btn_date):
    if btn_date == date.date():
        if count:
            if link_where:
                msg = f'🕯*{name}*\n🕐Начало: *{date.strftime("%H:%M, %d %b")}*\n〽️Где: ' +\
                      f'[{where}]({link_where})\n🔹Цена *{price}*\n🔸Осталось: [{count}]({about})'
            else:
                msg = f'🕯*{name}*\n🕐Начало: *{date.strftime("%H:%M, %d %b")}*\n〽️Где: *{where}*\n🔹Цена *{price}*\n' +\
                      f'🔸Осталось: [{count}]({about})'
            return msg


def get_post(data, chat_id, btn_date):
    send = False
    for i in range(len(data)):
        report = msg_format(
            data[i]['date'], data[i]['name'], data[i]['about'], data[i]['image'], data[i]['where'],
            data[i]['count'], data[i]['price'], data[i]['buy'], data[i]['link_where'], btn_date=btn_date
        )
        if report:
            bot.send_message(chat_id, report, parse_mode='Markdown', disable_web_page_preview=False)
            send = True
    if not send:
        bot.send_message(chat_id, 'Кажется, здесь пусто...')


@bot.message_handler(commands=['start'])
def start_command(message):
    report = '👋Привет! Используй кнопки, которые внизу'
    bot.send_message(message.chat.id, report, reply_markup=keyboards.top_markup())
    bot.register_next_step_handler(message, top)


@bot.message_handler(commands=['help'])
def help_command(message):
    report = '1️⃣Хочешь вернуться в главное меню?\n2️⃣Ничего не работает?\n‼️Пиши /start‼️'
    bot.send_message(message.chat.id, report, reply_markup=keyboards.top_markup())
    bot.register_next_step_handler(message, top)


def top(message):
    chat_id = message.chat.id
    if message.text == '🏆Большой театр':
        report = '`Чуть-чуть терпения... ещё чуть-чуть...`'
        bot.send_message(chat_id, report, parse_mode='Markdown')
        data = myparser.get_big()
        report = '✅Хороший выбор'
        bot.send_message(chat_id, report, reply_markup=keyboards.filters_markup(), parse_mode='Markdown')
        bot.register_next_step_handler(message, filters, data)
    elif message.text == '🏅Малый театр':
        report = '`Чуть-чуть терпения... ещё чуть-чуть...`'
        bot.send_message(chat_id, report, parse_mode='Markdown')
        data = myparser.get_small()
        report = '✅Хороший выбор'
        bot.send_message(chat_id, report, reply_markup=keyboards.filters_markup(), parse_mode='Markdown')
        bot.register_next_step_handler(message, filters, data)
    elif message.text == '🥇Театр им. А.С. Пушкина':
        report = '`Чуть-чуть терпения... ещё чуть-чуть...`'
        bot.send_message(chat_id, report, parse_mode='Markdown')
        data = myparser.get_pushkin()
        facts = [
            '*Алкоголь*\nПушкин любил шампанское, предпочтение он отдавал французскому "Вдова Клико"',
            '*Бакенбарды*\nПушкин носил бакенбарды. Дворовые в усадьбе "Михайловское" называли их "бокоушами"',
            '*Бокс*\nПушкин занимался боксом и был первым в России, кто ' +
            'начал выписывать из Англии книги по этому виду спорта',
            '*Дуэли*\nПушкин участвовал в 29 дуэлях, но никогда не стрелял первым',
            '*Трость*\nЧтобы добиться меткой стрельбы и твердости руки, Пушкин ' +
            'постоянно носил с собой металлическую трость весом 16 кг.',
            '*Маникюр*\nПоэт делал маникюр и отращивал ноготь на мизинце',
            '*Карты*\nПушкин был заядлым картежником, в картотеке жандармерии он ' +
            'числился как "известный в Москве банкомет". В 1829 году поэт за раз ' +
            'проиграл целое состояние - 24 800 руб. Одна корова в то время стоила 3 рубля',
            '*Женщины*\nВ 1829 году поэт составил список женщин, которыми увлекался. ' +
            'В нем было 37 женских имен. В письме княгине В. Вяземской поэт признался, ' +
            'что супруга Н.Гончарова является его 130-й любовью'
        ]
        report = random.choice(facts)
        bot.send_message(chat_id, report, reply_markup=keyboards.filters_markup(), parse_mode='Markdown')
        bot.register_next_step_handler(message, filters, data)
    elif message.text == '🥈МХТ им. А.П. Чехова':
        report = '`Чуть-чуть терпения... ещё чуть-чуть...`'
        bot.send_message(chat_id, report, parse_mode='Markdown')
        data = myparser.get_chehov()
        report = '✅Хороший выбор'
        bot.send_message(chat_id, report, reply_markup=keyboards.filters_markup(), parse_mode='Markdown')
        bot.register_next_step_handler(message, filters, data)
    elif message.text == '🥉Гоголь-центр':
        report = '`Чуть-чуть терпения... ещё чуть-чуть...`'
        bot.send_message(chat_id, report, parse_mode='Markdown')
        data = myparser.get_gogol()
        report = '✅Хороший выбор'
        bot.send_message(chat_id, report, reply_markup=keyboards.filters_markup(), parse_mode='Markdown')
        bot.register_next_step_handler(message, filters, data)
    elif reset(message):
        pass
    else:
        report = '❗️Используй кнопки, которые внизу!'
        bot.send_message(chat_id, report, reply_markup=keyboards.top_markup())
        bot.register_next_step_handler(message, top)


def filters(message, data=None):
    chat_id = message.chat.id
    now = (datetime.datetime.now() + datetime.timedelta(hours=3))
    if message.text == '‼️Сегодня':
        btn_date = now.date()
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, filters, data)
    elif message.text == '❗️Завтра':
        btn_date = (now + datetime.timedelta(days=1)).date()
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, filters, data)
    elif message.text == '📆Выбрать дату':
        report = 'Выбирай скорее!'
        bot.send_message(chat_id, report, reply_markup=keyboards.now_markup())
        bot.register_next_step_handler(message, now_date, data)
    elif message.text == '🔙Назад🔙':
        report = '✅Главное меню'
        bot.send_message(chat_id, report, reply_markup=keyboards.top_markup(), parse_mode='Markdown')
        bot.register_next_step_handler(message, top)
    elif reset(message):
        pass
    else:
        report = '❗️Используй кнопки, которые внизу!'
        bot.send_message(message.chat.id, report, reply_markup=keyboards.filters_markup())
        bot.register_next_step_handler(message, filters, data)


def now_date(message, data, state=0):
    chat_id = message.chat.id
    if message.text == '1':
        if state == 0:
            date = datetime.datetime(2019, 12, 1).date()
        else:
            date = datetime.datetime(2020, 1, 1).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '2':
        if state == 0:
            date = datetime.datetime(2019, 12, 2).date()
        else:
            date = datetime.datetime(2020, 1, 2).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '3':
        if state == 0:
            date = datetime.datetime(2019, 12, 3).date()
        else:
            date = datetime.datetime(2020, 1, 3).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '4':
        if state == 0:
            date = datetime.datetime(2019, 12, 4).date()
        else:
            date = datetime.datetime(2020, 1, 4).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '5':
        if state == 0:
            date = datetime.datetime(2019, 12, 5).date()
        else:
            date = datetime.datetime(2020, 1, 5).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '6':
        if state == 0:
            date = datetime.datetime(2019, 12, 6).date()
        else:
            date = datetime.datetime(2020, 1, 6).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '7':
        if state == 0:
            date = datetime.datetime(2019, 12, 7).date()
        else:
            date = datetime.datetime(2020, 1, 7).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '8':
        if state == 0:
            date = datetime.datetime(2019, 12, 8).date()
        else:
            date = datetime.datetime(2020, 1, 8).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '9':
        if state == 0:
            date = datetime.datetime(2019, 12, 9).date()
        else:
            date = datetime.datetime(2020, 1, 9).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '10':
        if state == 0:
            date = datetime.datetime(2019, 12, 10).date()
        else:
            date = datetime.datetime(2020, 1, 10).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '11':
        if state == 0:
            date = datetime.datetime(2019, 12, 11).date()
        else:
            date = datetime.datetime(2020, 1, 11).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '12':
        if state == 0:
            date = datetime.datetime(2019, 12, 12).date()
        else:
            date = datetime.datetime(2020, 1, 12).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '13':
        if state == 0:
            date = datetime.datetime(2019, 12, 13).date()
        else:
            date = datetime.datetime(2020, 1, 13).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '14':
        if state == 0:
            date = datetime.datetime(2019, 12, 14).date()
        else:
            date = datetime.datetime(2020, 1, 14).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '15':
        if state == 0:
            date = datetime.datetime(2019, 12, 15).date()
        else:
            date = datetime.datetime(2020, 1, 15).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '16':
        if state == 0:
            date = datetime.datetime(2019, 12, 16).date()
        else:
            date = datetime.datetime(2020, 1, 16).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '17':
        if state == 0:
            date = datetime.datetime(2019, 12, 17).date()
        else:
            date = datetime.datetime(2020, 1, 17).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '18':
        if state == 0:
            date = datetime.datetime(2019, 12, 18).date()
        else:
            date = datetime.datetime(2020, 1, 18).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '19':
        if state == 0:
            date = datetime.datetime(2019, 12, 19).date()
        else:
            date = datetime.datetime(2020, 1, 19).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '20':
        if state == 0:
            date = datetime.datetime(2019, 12, 20).date()
        else:
            date = datetime.datetime(2020, 1, 20).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '21':
        if state == 0:
            date = datetime.datetime(2019, 12, 21).date()
        else:
            date = datetime.datetime(2020, 1, 21).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '22':
        if state == 0:
            date = datetime.datetime(2019, 12, 22).date()
        else:
            date = datetime.datetime(2020, 1, 22).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '23':
        if state == 0:
            date = datetime.datetime(2019, 12, 23).date()
        else:
            date = datetime.datetime(2020, 1, 23).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '24':
        if state == 0:
            date = datetime.datetime(2019, 12, 24).date()
        else:
            date = datetime.datetime(2020, 1, 24).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '25':
        if state == 0:
            date = datetime.datetime(2019, 12, 25).date()
        else:
            date = datetime.datetime(2020, 1, 25).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '26':
        if state == 0:
            date = datetime.datetime(2019, 12, 26).date()
        else:
            date = datetime.datetime(2020, 1, 26).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '27':
        if state == 0:
            date = datetime.datetime(2019, 12, 27).date()
        else:
            date = datetime.datetime(2020, 1, 27).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '28':
        if state == 0:
            date = datetime.datetime(2019, 12, 28).date()
        else:
            date = datetime.datetime(2020, 1, 28).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '29':
        if state == 0:
            date = datetime.datetime(2019, 12, 29).date()
        else:
            date = datetime.datetime(2020, 1, 29).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '30':
        if state == 0:
            date = datetime.datetime(2019, 12, 30).date()
        else:
            date = datetime.datetime(2020, 1, 30).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '31':
        if state == 0:
            date = datetime.datetime(2019, 12, 31).date()
        else:
            date = datetime.datetime(2020, 1, 31).date()
        btn_date = date
        get_post(data, chat_id, btn_date)
        bot.register_next_step_handler(message, now_date, data, state)
    elif message.text == '➡️':
        m = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%B")
        bot.send_message(chat_id, f'Следующий месяц: {m}',
                         reply_markup=keyboards.now_markup(1))
        bot.register_next_step_handler(message, now_date, data=data, state=1)
    elif message.text == '🔙Назад🔙':
        report = '`Шаг назад!` - Выполнил.\nДавай в следующий раз без "!", а?'
        bot.send_message(chat_id, report, reply_markup=keyboards.filters_markup(), parse_mode='Markdown')
        bot.register_next_step_handler(message, filters, data)
    elif reset(message):
        pass
    elif state == 1:
        if message.text == '⬅️':
            m = datetime.datetime.now().strftime('%B')
            bot.send_message(chat_id, f'Предыдущий месяц: {m}', reply_markup=keyboards.now_markup(0))
            bot.register_next_step_handler(message, now_date, data=data, state=0)
        else:
            report = '❗️Используй кнопки, которые внизу!'
            bot.send_message(message.chat.id, report, reply_markup=keyboards.now_markup(1))
            bot.register_next_step_handler(message, now_date, data, state=1)
    else:
        report = '❗️Используй кнопки, которые внизу!'
        bot.send_message(message.chat.id, report, reply_markup=keyboards.now_markup())
        bot.register_next_step_handler(message, now_date, data, state)


def reset(message):
    if message.text == '/start':
        start_command(message)
        return True
    elif message.text == '/help':
        help_command(message)
        return True
    return False


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
