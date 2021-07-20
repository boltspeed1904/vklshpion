from vkbottle.api.keyboard import keyboard_gen
from vkbottle import Message, VKError
from vbml import Patcher, Pattern
from random import randrange
from Models.TortoiseModels import Users
from vkbottle.bot import Blueprint
from .Register import Register, OnlyMe, FromMe
from asyncio import sleep
bp=Blueprint()
@bp.on.message_handler(Register(), text=["Баланс", "баланс", "Баланс 💸", "@bot_agent_007 Баланс 💸"], lower=True)
async def balance(ans: Message):
	lal = await Users.get(user_id=ans.from_id)
	name_buttons = [[{'text': 'Пополнить 💶', 'color': 'positive'}]]
	name_keyboard = keyboard_gen(name_buttons, one_time=False, inline=True)
	await ans(f"💸 Ваш баланс: {lal.balance:,} руб", keyboard=name_keyboard)

@bp.on.message_handler(Register(), text=["Пополнить", "пополнить", "Пополнить 💶", "@bot_agent_007 Пополнить 💶"], lower=True)
async def wrapper(ans: Message):
	return """
💶 Для пополнения перейдите по ссылке: vk.cc/aCP4SO
♻ Комиссия: 5%
📙 Если Вы уже оплатили, то введите <<Оплатить>>. Чтобы подать заявку на рассмотрение дополнительных функций, а именно:
ᅠᅠᅠ🏆 Важные друзья
ᅠᅠᅠ💌 Кого лайкает
ᅠᅠᅠ👥 Скрытые друзья
⚠ Если Вы подали ложную заявку, то за это можете получить бан.
"""

@bp.on.message_handler(Register(), text=["Кнопки вкл", "кнопки вкл"], lower=True)
async def keyboard(ans: Message):
	name_buttons = [[{'text': 'Баланс 💰'},
					{'text': 'Пополнить 💶', 'color': 'positive'}]]
	name_keyboard = keyboard_gen(name_buttons, one_time=False)
	await ans("✅ Кнопки включены!", keyboard=name_keyboard)

@bp.on.message_handler(Register(), text=["Кнопки выкл", "кнопки выкл"], lower=True)
async def keyboard_off(ans: Message):
	await ans("❎ Кнопки выключены!", keyboard=keyboard_gen([]))

@bp.on.message_handler(Register(), text=["Помощь", "помощь"], lower=True)
async def wrapper(ans: Message):
	await ans('Все мои команды:\n ᅠ⚙ >> Услуги - Все услуги бота.\nᅠ📕 » Профиль - Просмотреть свой ID профиля.\nᅠ♻ » Обновить - Обновить работу бота.\nᅠ💶 » Пополнить - Пополнить свой баланс.\nᅠ💸 » Баланс - Узнать свой баланс.\nᅠ💳 >> Оплатить - Получить доп.информацию о пользователе.\nᅠ✅ » Кнопки [вкл/выкл] - Включить/выключить кнопки.\nᅠ🔎 » Инфо [ссылка] - Проверить пользователя.') 

@bp.on.message_handler(Register(), text=["Привет", "привет", "Начать", "начать"], lower=True)
async def wrapper(ans: Message):
	return """
Бот собирает информацию о профиле Вконтакте 🤖
Команды для управления:

ᅠ⚙ >> Услуги
ᅠ🔎 >> Инфо [ссылка]
ᅠ💸 >> Баланс
ᅠ💶 >> Пополнить

ᅠ⚠ Если Вам бот перестал отвечать, то напишите "Обновить", чтобы сбросить работу бота

Для удобства, Вы можете включить кнопки командой: <<Кнопки вкл>>.
Все команды Бота можно узнать по команде <<Помощь>>.
""" 
@bp.on.message_handler(Register(), text=['Оплата', 'Оплатить', 'Оплатить 💳'], lower=True)
async def monsend(ans):
	lal = await Users.get(user_id=ans.from_id)
	if lal.balance < 70:
		return f'''
🚫 У вас недостаточно средств на балансе!
💸 Ваш баланс: {lal.balance:,} руб.
💶 Для пополнения перейдите по ссылке: vk.cc/aCP4SO
⚠ Перед пополнением, обязательно укажите свой ID профиля в боте. Узнать свой ID профиля, можно по команде <<Профиль>>.
'''
	await lal.update_from_dict({'balance': lal.balance-70})
	await lal.save()
	return f'''
✅ Вы успешно отправили заявку на  просмотр Скрытых друзей.
⚠ Каждая заявка рассматривается вручную, проверка может занять до 2-х суток.
💳 Списано с баланса: 70 руб.
💸 Ваш баланс: {lal.balance} руб.
'''
@bp.on.message_handler(FromMe(), text="Проверка", lower=True)
async def wrapper(ans: Message):
	await ans("☢ Проверка прошла удачно!\n⚙ Вы являетесь разработчиком бота.")