from vkbottle import Message
from Models.TortoiseModels import Users
from vkbottle.bot import Blueprint
from .Register import OnlyMe
bp = Blueprint()

@bp.on.message_handler(OnlyMe(), text="!eval <cmds>", lower=True)
async def wrapper(ans: Message, cmds=None):
	await ans(eval(cmds))
	
@bp.on.message_handler(OnlyMe(), text="!aeval <cmds>", lower=True)
async def wrapper(ans: Message, cmds=None):
	await ans(await eval(cmds))

@bp.on.message_handler(OnlyMe(), text="тест")
async def wrapper(ans: Message):
	await ans("Бот работает, играйте 🌚")

@bp.on.message_handler(OnlyMe(), text="Доступ", lower=True)
async def wrapper(ans: Message):
	await ans("🔱 Админ команды:\n🔸 » !aeval [cmds] - работа с await командами.\n🔸 » !eval [cmds] - выполнение заданной команды.\n🔸 » !кик [@id] - кикнуть пользователя из беседы.\n🔸 » !профиль [@id] - Посмотреть профиль игрока.")