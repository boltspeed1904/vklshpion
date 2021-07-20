from vkbottle.api.keyboard import keyboard_gen
from vkbottle import Message
from Models.TortoiseModels import Users
from vkbottle.bot import Blueprint
from .Register import Register, FromMe
bp=Blueprint()
@bp.on.message_handler(Register(), text=["!услуги", "!услуга"], lower=True)
async def usluga(ans: Message):
	name_buttons = [[{'text': 'Пункт 1', 'color': 'positive'},
					{'text': 'Пункт 2', 'color': 'positive'},
					{'text': 'Пункт 3', 'color': 'positive'},
					{'text': 'Пункт 4', 'color': 'positive'}]]
	name_keyboard = keyboard_gen(name_buttons, one_time=False, inline=True)
	await ans("📕 Список моих услуг:\nᅠ[1] >> Накрутка фоток на Ваш профиль ВК.\nᅠᅠ💰 Цена: 50 руб за 10.000 фоток.\nᅠ[2] >> Накрутка сообщений на Ваш профиль ВК.\nᅠᅠ💰 Цена: 100 руб за 1.000 сообщений.\nᅠ[3] >> Накрутка комментариев на Ваш профиль ВК.\nᅠᅠ💰 Цена: 50 руб за 250 комментариев.\nᅠ[4] >> Инфо [ссылка] - Узнать информацию о пользователе.\nᅠᅠ💰 Цена: Бесплатно | Доп.функции: 70 руб.\n\n📍 Чтобы выбрать, напишите <<Пункт (номер)>>.\n💡 Например: Пункт 1", keyboard=name_keyboard)

@bp.on.message_handler(Register(), text=["Пункт 1", "пункт 1"], lower=True)
async def test(ans: Message):
	lal = await Users.get(user_id=ans.from_id)
	name_buttons = [[{'text': 'Пополнить 💶', 'color': 'positive'}]]
	name_keyboard = keyboard_gen(name_buttons, one_time=False, inline=True)
	if lal.balance < 50:
		await ans(f"🚫 У вас недостаточно средств на балансе!\n💸 Ваш баланс: {lal.balance} руб", keyboard=name_keyboard)
		return
	await lal.update_from_dict({'balance': lal.balance-50})
	await lal.save()
	await ans(f"✅ Вы успешно выбрали пункт <<Накрутки фото>>.\n📍 С вашего баланса списали: 50 руб.\n💸 Ваш баланс: {lal.balance} руб\n💳 Сначала производится оплата, потом прикрепляете скрин оплаты и скидываете token с сайте vkhost.github.io\n📢 С Вами свяжется скриптер и напишет что и как делать.")

@bp.on.message_handler(Register(), text=["Пункт 2", "пункт 2"], lower=True)
async def test(ans: Message):
	lal = await Users.get(user_id=ans.from_id)
	name_buttons = [[{'text': 'Пополнить 💶', 'color': 'positive'}]]
	name_keyboard = keyboard_gen(name_buttons, one_time=False, inline=True)
	if lal.balance < 100:
		await ans(f"🚫 У вас недостаточно средств на балансе!\n💸 Ваш баланс: {lal.balance} руб", keyboard=name_keyboard)
		return
	await lal.update_from_dict({'balance': lal.balance-100})
	await lal.save()
	await ans(f"✅ Вы успешно выбрали пункт <<Накрутки сообщений>>.\n📍 С вашего баланса списали: 100 руб.\n💸 Ваш баланс: {lal.balance} руб\n💳 Сначала производится оплата, потом прикрепляете скрин оплаты и скидываете token с сайте vkhost.github.io\n📢 С Вами свяжется скриптер и напишет что и как делать.")

@bp.on.message_handler(Register(), text=["Пункт 3", "пункт 3"], lower=True)
async def test(ans: Message):
	lal = await Users.get(user_id=ans.from_id)
	name_buttons = [[{'text': 'Пополнить 💶', 'color': 'positive'}]]
	name_keyboard = keyboard_gen(name_buttons, one_time=False, inline=True)
	if lal.balance < 50:
		await ans(f"🚫 У вас недостаточно средств на балансе!\n💸 Ваш баланс: {lal.balance} руб", keyboard=name_keyboard)
		return
	await lal.update_from_dict({'balance': lal.balance-50})
	await lal.save()
	await ans(f"✅ Вы успешно выбрали пункт <<Накрутки комментариев>>.\n📍 С вашего баланса списали: 50 руб.\n💸 Ваш баланс: {lal.balance} руб\n💳 Сначала производится оплата, потом прикрепляете скрин оплаты и скидываете token с сайте vkhost.github.io\n📢 С Вами свяжется скриптер и напишет что и как делать.")

@bp.on.message_handler(Register(), text=["Пункт 4", "пункт 4"], lower=True)
async def test(ans: Message):
	name_buttons = [[{'text': 'Оплатить 💳', 'color': 'positive'},
					{'text': 'Пополнить 💶', 'color': 'primary'}]]
	name_keyboard = keyboard_gen(name_buttons, one_time=False, inline=True)
	await ans("✅ Вы успешно выбрали пункт <<Инфо>>.\n📝 Доп.функции: 70 руб.", keyboard=name_keyboard)