class Cajero:
	def __init__(self):
		self.tiempo_desocupado = 0
		self.tiempo_atender = 0

	def ocupado(self):
		return self.tiempo_atender > 0

	def tiene_cliente(self):
		self.tiempo_atender -= 1

	def ocioso(self):
		self.tiempo_desocupado += 1
