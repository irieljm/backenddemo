class UserSerializer:


	@staticmethod
	def serialize(user):
	#id, name, pin, balance
		return {"name": user.name,
				"pin": user.pin,
				"balance": user.balance
				"id": user.id}

