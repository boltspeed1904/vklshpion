from vkbottle import Message
from Models.TortoiseModels import Users
from vkbottle.bot import Blueprint
from vkbottle.rule import AbstractMessageRule
from .Register import OnlyMe, Register
bp = Blueprint()
@bp.on.message_handler(Register(), text=["Профиль", "профиль"], lower=True)
async def profiles(ans: Message):
	lal = await Users.get(user_id=ans.from_id)
	return f"""
Ваш профиль:
	🆔 Игровой ID: {lal.id}
	💰 Баланс: {lal.balance:,} руб
"""
@bp.on.message_handler(OnlyMe(), text="!профиль", lower=True)
async def profile(ans: Message):
	if ans.reply_message:
		await ans(await profiles(ans.reply_message.from_id))
	elif ans.fwd_messages:
		await ans(await profiles(ans.fwd_messages[0].from_id))