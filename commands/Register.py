from vkbottle import Message
from Models.TortoiseModels import Users
from vkbottle.rule import AbstractMessageRule
class Register(AbstractMessageRule):
	async def check(self, message: Message):
		if await Users.get_or_none(user_id=message.from_id) is None:
			await Users.create(user_id=message.from_id)
			await message("""
Бот собирает информацию о профиле Вконтакте 🤖
Команды для управления:

ᅠ🔎 » Инфо [ссылка]
ᅠ💸 » Баланс
ᅠ💶 » Пополнить

ᅠ⚠ Если Вам бот перестал отвечать, то напишите "Обновить", чтобы сбросить работу бота

Для удобства, Вы можете включить кнопки командой: Кнопки вкл
Все команды Бота можно узнать по команде <<Помощь>>.
""")
		return True
class OnlyMe(AbstractMessageRule):
	async def check(self, message: Message):
		if message.from_id == {id311288698}:
			return True
		await message("🚫 У вас нет доступа к данной команде!")
		return False

#Писать ID страницы без { }         
#Если Вы хотите выдать доступ к командам, у которых класс (OnlyMe, FromMe), то пропишите: 
#if message.from_id == 123456789 or message.from_id == 123456789:
#Пример указан в классе FromMe

class FromMe(AbstractMessageRule):
	async def check(self, message: Message):
		if message.from_id == 500760031:
			return True
		await message("🚫 У вас нет доступа к данной команде!")
		return False