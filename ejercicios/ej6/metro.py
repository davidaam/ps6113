from itertools import cycle
import math
import random
import numpy as np

N_EMB = [127, 162, 179, 75, 223, 186, 124, 45, 100, 171, 235, 176, 130, 159, 117, 100, 92, 68, 242, 122, 184, 84, 240, 319, 61, 78, 20, 141, 202, 213, 204, 360, 169, 206, 326, 210, 335, 233, 102, 243, 135, 310, 138, 95, 216, 99, 346, 220, 191, 230, 219, 225, 271, 270, 110, 305, 157, 128, 163, 90, 148, 70, 40, 80, 105, 159, 141, 150, 164, 200, 213, 195, 134, 141, 107, 177, 109, 48, 145, 114, 400, 212, 258, 198, 229, 175, 199, 177, 194, 185, 303, 335, 310, 104, 374, 190, 211, 160, 138, 227, 122, 230, 97, 166, 232, 187, 212, 125, 119, 90, 286, 310, 115, 277, 189, 159, 266, 170, 28, 141, 155, 309, 152, 122, 262, 111, 254, 124, 138, 190, 136, 110, 396, 96, 86, 111, 81, 226, 50, 134, 131, 120, 112, 140, 280, 145, 208, 333, 250, 221, 318, 120, 72, 166, 194, 87, 94, 170, 65, 190, 359, 312, 205, 77, 197, 359, 174, 140, 167, 181, 143, 99, 297, 92, 246, 211, 275, 224, 171, 290, 291, 220, 239, 126, 89, 66, 35, 26, 129, 234, 181, 180, 58, 40, 54, 123, 78, 319, 389, 121]

class Metro:
    def __init__(self, max_recorridos):
        self.max_recorridos = max_recorridos
        self.tiempo = 0
        self.estacion = 1
        self.pasajeros_abordo = 0
        self.estaciones_restantes_pasajero = []
        self.acumulado_abordo = 0
        self.total_pasajeros = 0
        self.total_estaciones_recorridas = 0
        self.max_pasajeros_abordo = 0

    def tiempo_estacion(self, n_emb, n_des):
        return 20 * (1 + 0.1*math.log(n_des + n_emb))

    def tiempo_recorrido(self):
        return 100 * (1 + 0.1*math.log(self.pasajeros_abordo))

    def estadisticas(self):
        return {
            'Tiempo total': self.tiempo,
            'Nro. promedio de pasajeros abordo': round(self.acumulado_abordo / self.total_estaciones_recorridas, 2),
            'Nro. promedio de pasajeros abordo (n_emb)': round(self.total_pasajeros / self.total_estaciones_recorridas, 2),
            'Nro. maximo de pasajeros embarcados': self.max_pasajeros_abordo
        }

    def run(self):
        for estacion in cycle([i for i in range(2,11)] + [i for i in range(9,0,-1)]):
            if self.total_estaciones_recorridas > self.max_recorridos:
                break
            if self.estacion != 10 and self.estacion != 1:
                n = len(self.estaciones_restantes_pasajero)
                self.estaciones_restantes_pasajero = list(filter(lambda x: x != 0, self.estaciones_restantes_pasajero))
                n_des = n - len(self.estaciones_restantes_pasajero)
            elif self.estacion == 10 or self.estacion == 1:
                n_des = self.pasajeros_abordo
                self.estaciones_restantes_pasajero = []

            n_emb = random.choice(N_EMB)
            self.estaciones_restantes_pasajero += [np.random.binomial(10 - self.estacion, 0.5) for _ in range(n_emb)]
            self.pasajeros_abordo += n_emb - n_des
            self.tiempo += self.tiempo_estacion(n_emb, n_des)
            self.tiempo += self.tiempo_recorrido()
            self.estacion = estacion
            self.acumulado_abordo += self.pasajeros_abordo
            self.total_pasajeros += n_emb
            self.max_pasajeros_abordo = max(self.max_pasajeros_abordo, self.pasajeros_abordo)
            self.total_estaciones_recorridas += 1
            self.estaciones_restantes_pasajero = list(map(lambda x: x - 1, self.estaciones_restantes_pasajero))
        print(self.estadisticas())

if __name__ == '__main__':
    print("Introduzca numero de recorridos a simular")
    n = int(input())
    m = Metro(n)
    m.run()
