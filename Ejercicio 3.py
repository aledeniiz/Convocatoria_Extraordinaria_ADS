#Creamos la clase coche, para crear las variables principales
class Coche:
    def __init__(self, nombre, velocidad_maxima, aceleracion):
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima
        self.aceleracion = aceleracion
        self.posicion = 0
        self.velocidad = 0

    def mover(self, tiempo):
        self.velocidad += self.aceleracion * tiempo
        if self.velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
        self.posicion += self.velocidad * tiempo
#Creamos la clase carrera en la que estan todas las funciones que afectaran al resultado y funcionamiento de la carrera.
class Carrera:
    def __init__(self):
        self.coches = []
#Se añade un coche nuevo a la parrilla
    def agregar_coche(self, coche):
        self.coches.append(coche)
#Contabilizamos el tiempo que pasa cuando se empiezan a mover los coches
    def iniciar_carrera(self, duracion, intervalo):
        tiempo_transcurrido = 0
        while tiempo_transcurrido < duracion:
            for coche in self.coches:
                coche.mover(intervalo)
                print(f"{coche.nombre} - Posición: {coche.posicion:.2f}")
            tiempo_transcurrido += intervalo
        self.mostrar_ganador()
#Se muestra el coche con una posicion mas avanzada, que es el ganador (el nano, aqui si tiene buen coche)
    def mostrar_ganador(self):
        ganador = max(self.coches, key=lambda coche: coche.posicion)
        print(f"Ganador: {ganador.nombre} con una posición de {ganador.posicion:.2f}")

if __name__ == "__main__":
    Fernando_Alonso_AM = Coche("El Nano", 200.0, 12.0)
    Carlos_Sainz_FR = Coche("Sainz", 180.0, 12.0)
    Max_Verstapen_RB = Coche("Verstapen", 220.0, 10.0)

    carrera = Carrera()
    carrera.agregar_coche(Fernando_Alonso_AM)
    carrera.agregar_coche(Carlos_Sainz_FR)
    carrera.agregar_coche(Max_Verstapen_RB)

    carrera.iniciar_carrera(10, 1)