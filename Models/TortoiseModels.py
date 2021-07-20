from tortoise import Tortoise,fields
from tortoise.models import Model

class Users(Model):
	id = fields.IntField(pk=True)
	user_id = fields.IntField()
	balance = fields.IntField(default=0)