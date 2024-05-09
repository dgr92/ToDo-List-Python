from os import system
from .task import Task
import json

# Clase para la lista de tareas 
class TaskList():
    def __init__(self):
        self.task_list = [] 
        self.task_id_counter = 0 # Variable que dará valor al ID de las tareas
        
        
    # Método que permite seleccionar las diferentes funcionalidades del programa
    def startMenu(self):
        try:  
            print(" Selecciona que quieres hacer:", "\n", 
                  "   1. Agregar nueva tarea.", "\n", 
                  "   2. Eliminar una tarea.", "\n", 
                  "   3. Editar estado de la tarea.", "\n", 
                  "   4. Mostrar la lista de tareas.", "\n",
                  "   5. Salir.", "\n")
            
            selected_option = int(input("Selecciona que hacer: "))
            
            if not (0 < selected_option < 6): # Comprueba que el número introducido sea 1 - 5
                raise Exception
            
            if selected_option == 1:
                system("cls") # Limpia el texto de la consola
                self.newTask()
                
            if selected_option == 2:
                system("cls")
                self.delTask()
                
            if selected_option == 3:
                system("cls")
                self.taskDone() 
                
            if selected_option == 4:
                system("cls")
                self.showTasks()
                
            if selected_option == 5:
                print("----------------------------------------------")
                print("\n          CERRANDO LISTA DE TAREAS \n")
                print("----------------------------------------------\n")
                
                exit() # Termina la ejecución del programa
            
        except ValueError: # Controla el error producido en caso de introducir algo que no sea nº entero
            system("cls")
            print("----------------------------------------------")
            print("\n      ERROR! Introduce un número válido \n")
            print("----------------------------------------------\n")
    
        except Exception: # Controla el error producido en caso de que el numero no esté entre 1 - 5
            system("cls")
            print("----------------------------------------------")
            print("\n    ERROR! Debes elegir una de las opciones. \n")
            print("----------------------------------------------\n")            
            
        self.startMenu() # Re-lanza el método "menú principal"


    # Método que crea nuevas tareas
    def newTask(self):
        print("----------------------------------------------")
        print("                 NUEVA TAREA")
        print("----------------------------------------------\n") 
               
        task = input("Introduce nueva tarea: ")
                
        task_id = self.task_id_counter
        task = Task(task_id, task) # Instancia una tarea con el ID y el mensaje
        self.task_list.append(task) # Se añade a la lista
        
        self.task_id_counter += 1 # Se incrementa el ID para la próxima tarea
        
        system("cls")
        
        print("\n----------------------------------------------\n")
        print("Tarea guardada!")
        print("\n----------------------------------------------\n")
        
        self.startMenu()


    # Método que elimina tareas
    def delTask(self):
        print("----------------------------------------------")
        print("               ELIMINAR TAREA")
        print("----------------------------------------------\n")

        if(len(self.task_list) == 0): # Comprueba que la lista no esté vacía
            print("         No hay tareas que eliminar")
            print("\n----------------------------------------------\n")
            self.startMenu()
            
        for task in self.task_list: # Muestra la lista de tareas existentes para ver cual queremos eliminar
            print(json.dumps(task.get_task(), indent=4))
        print("\n----------------------------------------------\n")
        
        try:
            task_id = int(input("Introduce el ID de la tarea a eliminar: ") )     
            print("\n----------------------------------------------\n")
            
            if task_id < 0: # Comprueba que no se introduzca nº negativo
                raise Exception
            
            for task in self.task_list: # Bucle que compara el ID de la tarea con el que hemos introducido 
                task_info = task.get_task()
                
                if task_info["ID"] == task_id:
                    self.task_list.remove(task) # Se elimina la tarea
                    
                    system("cls")
        
                    self.showTasks() # Se muestra el nuevo estado de la lista 
            
            system("cls")
            print("----------------------------------------------")
            print("\n      ERROR! El ID no existe en la lista \n")
            
                
        except ValueError:
            system("cls")
            print("----------------------------------------------")
            print("\n      ERROR! Introduce un número válido \n")
            
            
        except Exception :
            system("cls")
            print("----------------------------------------------")
            print("\n    ERROR! Introduce un número mayor que 0 \n")
        
        self.delTask()
   
    
    # Método que modifica el estado de las tareas
    def taskDone(self):
        print("----------------------------------------------")
        print("               MODIFICAR TAREA")
        print("----------------------------------------------\n")

            
        if(len(self.task_list) == 0): # Comprueba que la lista no esté vacía
            print("         No hay tareas que modificar")
            print("\n----------------------------------------------\n")
            self.startMenu()
            
        for task in self.task_list: # Muestra la lista de tareas existentes para ver cual queremos modificar
            print(json.dumps(task.get_task(), indent=4))
        print("\n----------------------------------------------\n")
        
        try:
            task_id = int(input("Introduce el ID de la tarea a modificar: ") )     
            print("\n----------------------------------------------\n")
            
            if task_id < 0: # Comprueba que no se introduzca nº negativo
                raise Exception
            
            for task in self.task_list: # Bucle que compara el ID de la tarea con el que hemos introducido 
                task_info = task.get_task()
                
                if task_info["ID"] == task_id:
                    task.toggle_done() # Se modifica el estado de la tarea
                    
                    system("cls")
        
                    self.showTasks() # Se muestra el nuevo estado de la lista 
            
            system("cls")
            
            print("----------------------------------------------")
            print("\n      ERROR! El ID no existe en la lista \n")

        except ValueError:
            system("cls")
            print("----------------------------------------------")
            print("\n      ERROR! Introduce un número válido \n")
            
            
        except Exception :
            system("cls")
            print("----------------------------------------------")
            print("\n    ERROR! Introduce un número mayor que 0 \n")
                
        self.taskDone()
            
    
    # Método que muestra la lista de las tareas
    def showTasks(self):
        print("----------------------------------------------")
        print("               LISTA DE TAREAS")
        print("----------------------------------------------\n")
        
        if len(self.task_list) > 0: # Si la lista no está vacía 
            for task in self.task_list: # Recorre la lista
                print(json.dumps(task.get_task(), indent=4)) # Mostrando cada tarea en formato JSON

        else:
            print("   Lista vacía. Guarda tareas para comenzar.")
        
        print("\n----------------------------------------------\n")
            
        self.startMenu()
