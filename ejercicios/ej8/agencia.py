from random import random
from functools import reduce

# Globals Constants
COMPACTO = 0
MEDIANO = 1
LUJO = 2

class Agencia:
  def __init__(self, semanas, resumen_semanal):
    self.resumen_semanal = resumen_semanal
    self.semanas = semanas
    # Arreglo de comisiones por autos vendidos por semana
    self.comisiones_semanal = [[] for x in range(semanas)]

  def numero_autos_vendidos(self):
    prob = random()
    if prob < 0.1:
      return 0
    elif prob < 0.25:
      return 1
    elif prob < 0.45:
      return 2
    elif prob < 0.70:
      return 3
    elif prob < 0.90:
      return 4
    else:
      return 5

  def select_tipo_carro(self):
    prob = random()
    if prob < 0.4:
      return COMPACTO
    elif prob < 0.75:
      return MEDIANO
    else:
      return LUJO 

  def calcular_comision(self,tipo):
    prob = random()
    if tipo == COMPACTO:
      return 250
    elif tipo == MEDIANO:
      if prob < 0.40:
        return 400
      else:
        return 500
    else:
      if prob < 0.35:
        return 1000
      elif prob < 0.75:
        return 1500
      else:
        return 2000

  def estadisticas(self):
    promedios = []
    for semana in range(self.semanas):
      suma = reduce((lambda x, y: x + y), self.comisiones_semanal[semana])
      nro_comiciones = len(self.comisiones_semanal[semana])
      promedio = round(suma*1.0/nro_comiciones, 2)
      promedios += [promedio]
      if self.resumen_semanal:
        print('Promedio Semana ' + str(semana) + ': ' + str(promedio))
    
    promedio_total = round(reduce((lambda x, y: x + y), promedios)*1.0/len(promedios),2)
    print('Promedio Total: ' + str(promedio_total))


  def simulacion(self):
    for semana in range(self.semanas):
      for vendedor in range(5):
        autos_vendidos = self.numero_autos_vendidos()
        for carro in range(autos_vendidos):
          tipo = self.select_tipo_carro()
          self.comisiones_semanal[semana] += [self.calcular_comision(tipo)]
    self.estadisticas()

if __name__ == '__main__':
  print("Introduzca el numero de semanas de la simulacion")
  semanas = int(input())
  print("Prisione 1 si quiere un resumen semanal:")
  resumen = int(input())
  agencia = Agencia(semanas, resumen==1)
  agencia.simulacion()