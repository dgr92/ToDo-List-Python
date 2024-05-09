
from classes.tasklist import TaskList

def main(): # Define la función main
    lista_tareas = TaskList() # Instancia la clase TaskList
    lista_tareas.startMenu() # Llama al método startMenu de TaskList

if __name__ == "__main__": # Comprueba si el script se está ejectuando directamente
    main() # Llama la función main