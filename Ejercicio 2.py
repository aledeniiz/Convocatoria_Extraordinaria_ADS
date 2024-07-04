#Creamos la clase tarea para en ella definir el titulo y la descripcion
class Tarea:
    def __init__(self, titulo, descripcion=""):
        self.titulo= titulo
        self.descripcion= descripcion
    def __str__(self):
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}"
#Creamos el gestor de tareas en las cuales podremos hacer varias podficaciones a tareas 
class GestorDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion=""):
        nueva_tarea = Tarea(titulo, descripcion)
        self.tareas.append(nueva_tarea)
        print("Tarea añadida exitosamente.")
#Borramos una tarea del todo
    def eliminar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                print("Tarea eliminada exitosamente.")
                return
        print("No se encontró una tarea con ese título.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas.")
        else:
            for tarea in self.tareas:
                print(tarea)
                print("-" * 20)
#Definimos las opciones que tendra el menu
def mostrar_menu():
    print("Gestor de Tareas")
    print("1. Agregar Tarea")
    print("2. Eliminar Tarea")
    print("3. Mostrar Tareas")
    print("4. Salir")
#Damos valor a los numeros intrucidos para ejecutar estas tareas 
def main():
    gestor = GestorDeTareas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea (opcional): ")
            gestor.agregar_tarea(titulo, descripcion)
        elif opcion == "2":
            titulo = input("Ingrese el título de la tarea a eliminar: ")
            gestor.eliminar_tarea(titulo)
        elif opcion == "3":
            gestor.mostrar_tareas()
        elif opcion == "4":
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()