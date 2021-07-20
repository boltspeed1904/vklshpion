from vkbottle.bot import Message, Blueprint
from vbml import Patcher, Pattern
from cfgs.cfg import bot
from random import randint
from time import time
from datetime import datetime
from .Register import OnlyMe
from asyncio import sleep, get_event_loop
from os.path import exists as ex
bp, pt = Blueprint(), Patcher()
user_token = 'https://oauth.vk.com/blank.html#access_token=f52572f16d8d815a5e9a925cf63c652b5fa7d14d0954aeef8c0797feeb71566e93cac68afb8f9834e1439&expires_in=0&user_id=311288698' #токен юзера можно получить на сайте vkhost.github.io (Токен получать с Kate Mobile)

@bp.on.message_handler(text=['Инфо', 'Инфо <id_input>'], lower=True)
async def information(ans: Message, id_input=None, gipers:str=''):
	path = pt.check(gipers, Pattern('[id<m_id>|<name>]'))
	user_id = path['m_id'] if path != None else ans.reply_message.from_id if ans.reply_message else ans.fwd_messages[0].from_id if ans.fwd_messages else None
	if "vk.com/" in id_input:
		user_id = (await bp.api.users.get(user_ids=ans.text.split("/")[-1]))[0].id
	if not user_id:
		await ans(f'⚠ Принимаются только ссылки.')
		return 
	la = str(await bot.request.get(f'https://vk.com/foaf.php?id={user_id}', read_content=True))
	datareg = la.split('<ya:created dc:date="')[-1].split('"/>')[0][:-6].split('T')
	user_get = (await bot.request.get(f'https://api.vk.com/method/users.get?access_token={user_token}&v=5.123&user_ids={user_id}&fields=followers_count,bdate,city,country'))['response'][0]
	if user_get['is_closed']:
		return f'''
📢 Информация о [id{user_id}|Пользователе]:
🆔 Пользователя: {user_id}
🚫 У данной страницы профиль закрыт!
📍 По команде <<Услуги>> можно просмотреть, что может наш Бот.
💌 Чтобы у Вас работали все функции без ограничений, пополните баланс <<Пополнить>> и оплатите все услуги нашего бота <<Оплатить>>. 
'''

	else:
		friends_count = (await bot.request.get(f'https://api.vk.com/method/friends.get?access_token={user_token}&v=5.123&user_id={user_id}&count=1'))['response']['count']
		await ans(f"""
📢 Информация о [id{user_id}|Пользователе]:
🆔 Пользователя: {user_id}
🚶 Подписчиков: {user_get['followers_count']}
{f'🚶 Друзей: {friends_count}' if friends_count else ''}
{f"✈ Страна: {user_get['country']['title']}" if 'country' in user_get else ''}
{f"🏡 Город: {user_get['city']['title']}" if 'city' in user_get else ''}
{f"📅 Дата рождения: {user_get['bdate']}" if 'bdate' in user_get else ''}

📝 Дата регистрации: {datareg[0]} | {datareg[1]}

💌 Кого лайкает пользователь: ?
🏆 Важные друзья пользователя: ?
👥 Скрытые друзья пользователя: ?

💰 Цена всех функций: 70.00р
📍 По команде <<Услуги>> можно просмотреть, что может наш Бот.

Оплатить 👉 vk.cc/aCP4SO
""", disable_mentions=1)
	last = randint(0, 1)
	show = randint(0, 3)
	LA = f"{user_get['first_name']} {user_get['last_name']}"
	if last == 0:
		if show == 0:
			LA += " скрывает от Вас 4-х девушек и 5-х парней 😳"
		elif show == 1:
			LA += " скрывает от Вас 1 девушку и 2-х парней 😳"
		elif show == 2:
			LA += " скрывает от Вас 3-х девушек и 1 парня 😳"
		elif show == 3:
			LA += " скрывает от Вас 5-х девушек и 7-мь парней 😳"
	if last == 1:
		if show == 0:
			LA += " скрывает от Вас 10 девушек и 2-х парней 😳"
		elif show == 1:
			LA += " скрывает от Вас 8 девушек и 4-х парней 😳"
		elif show == 2:
			LA += " скрывает от Вас 1 девушку и 3-х парней 😳"
		elif show == 3:
			LA += " скрывает от Вас 3 девушки и 6-х парней 😳"
	return LA