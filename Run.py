from cfgs.cfg import bot
from tortoise import Tortoise
from commands import (
check,
dop,
balance,
Profile,
Eval
)

bot.set_blueprints(
check.bp,
dop.bp,
balance.bp,
Profile.bp,
Eval.bp
)

async def init_db():
	await Tortoise.init(
		db_url="sqlite://DB/DBase.db", modules={"models": ["Models.TortoiseModels"]}
	)
	await Tortoise.generate_schemas()
	
bot.run_polling(on_startup=init_db)