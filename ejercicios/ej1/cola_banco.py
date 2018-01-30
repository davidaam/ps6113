from cajero import Cajero
from cliente import Cliente
from math import exp
import random

class Simulacion:
	def __init__(self, duracion):
		self.duracion = duracion
		self.tiempo = 0
		self.cajeros = [Cajero() for _ in range(4)]
		self.cola = [] # [Cliente]
		self.clientes_atendidos = 0
		self.desertores = 0
		self.total_tiempo_esperado = 0
		self.capacidad_clientes_disponible = 0

	def pasa_hora(self):
		if self.tiempo % 3600 == 0:
			h = (self.tiempo // 3600) + 1
			self.capacidad_clientes_disponible = int(60 * exp(h))
			if h > 1:
				print(self.estadisticas())

	def desertar(self):
		tam_cola = len(self.cola)
		r = random.random()
		if tam_cola < 6:
			return False
		elif 6 <= tam_cola <= 8:
			return r < 0.2
		elif 9 <= tam_cola <= 10:
			return r < 0.4
		elif 11 <= tam_cola <= 14:
			return r < 0.6
		else:
			return r < 0.8

	def clientes_minuto(self):
		llegan = random.randint(0, 1)
		if llegan and self.capacidad_clientes_disponible > 0:
			n = random.randint(1, self.capacidad_clientes_disponible)
			self.capacidad_clientes_disponible -= n
		else:
			n = 0
		return n

	def run(self):
		for t in range(0, self.duracion+2):
			self.pasa_hora()
			if self.tiempo % 60 == 0:
				clientes = self.clientes_minuto()
				for _ in range(clientes):
					if not self.desertar():
						self.cola.append(Cliente(self.tiempo))
					else:
						self.desertores += 1
			for cajero in self.cajeros:
				if cajero.ocupado():
					cajero.tiene_cliente()
				else:
					if len(self.cola):
						cliente = self.cola.pop(0)
						self.clientes_atendidos += 1
						self.total_tiempo_esperado += self.tiempo - cliente.tiempo_llegada
						cajero.tiempo_atender = random.randint(3*60, 5*60)
					else:
						cajero.ocioso()
			self.tiempo = t


	def estadisticas(self):
		return {
			'Tiempo esperado por cliente': round(self.total_tiempo_esperado / self.clientes_atendidos, 2),
			'Porcentaje de clientes desertores': round(100 * self.desertores / (self.clientes_atendidos + self.desertores + len(self.cola)), 2),
			'Tiempo desocupado por cajero': list(map(lambda c: round(100 * c.tiempo_desocupado / self.tiempo, 2), self.cajeros))
		}

if __name__ == '__main__':
	print("Introduzca duración en horas de la simulación")
	h = int(input())
	sim = Simulacion(3600 * h)
	sim.run()
