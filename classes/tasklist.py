from os import system
from .task import Task
import json

class TaskList():
    def __init__(self):
        self.task_list = [] 
        self.task_id_counter = 0 # Variable que dará valor al ID de las tareas
        
        
    def startMenu(self):
        try:  
            
            print("\n Selecciona que quieres hacer:", "\n", 
                  "\033[93m"+"   [1] " +"\033[0m"+ "Agregar nueva tarea.", "\n", 
                  "\033[93m"+"   [2] " +"\033[0m"+ "Eliminar una tarea.", "\n", 
                  "\033[93m"+"   [3] " +"\033[0m"+ "Editar estado de la tarea.", "\n", 
                  "\033[93m"+"   [4] " +"\033[0m"+ "Mostrar la lista de tareas.", "\n",
                  "\033[93m"+"   [5] " +"\033[0m"+ "Salir.", "\n")
            
            selected_option = int(input("Selecciona que hacer: "))
            
            if not (0 < selected_option < 6): 
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
                print("\033[91m"+"\n          CERRANDO LISTA DE TAREAS \n"+"\033[0m")
                print("----------------------------------------------\n")
                
                exit() # Termina la ejecución del programa
            
        except ValueError: 
            system("cls")
            print("----------------------------------------------")
            print("\033[91m"+"\n      ERROR! Introduce un número válido \n"+"\033[0m")
            print("----------------------------------------------\n")
    
        except Exception: 
            system("cls")
            print("----------------------------------------------")
            print("\033[91m"+"\n    ERROR! Debes elegir una de las opciones. \n" + "\033[0m")
            print("----------------------------------------------\n")            
            
        self.startMenu() 


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
        print("\033[92m"+"Tarea guardada!"+"\033[0m")
        print("\n----------------------------------------------\n")
        
        self.startMenu()


    def delTask(self):
        print("----------------------------------------------")
        print("               ELIMINAR TAREA")
        print("----------------------------------------------\n")

        if(len(self.task_list) == 0):
            print("\033[91m"+"         No hay tareas que eliminar"+"\033[0m")
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
                    self.task_list.remove(task) 
                    
                    system("cls")
        
                    self.showTasks() # Se muestra el nuevo estado de la lista 
            
            system("cls")
            print("----------------------------------------------")
            print("\033[91m" + "\n      ERROR! El ID no existe en la lista \n"+"\033[0m")
            
                
        except ValueError:
            system("cls")
            print("----------------------------------------------")
            print("\033[91m"+"\n      ERROR! Introduce un número válido \n"+"\033[0m")
            
            
        except Exception :
            system("cls")
            print("----------------------------------------------")
            print("\033[91m"+"\n    ERROR! Introduce un número mayor que 0 \n"+"\033[0m")
        
        self.delTask()
   
    
    def taskDone(self):
        print("----------------------------------------------")
        print("               MODIFICAR TAREA")
        print("----------------------------------------------\n")

            
        if(len(self.task_list) == 0):
            print("\033[91m"+"         No hay tareas que modificar"+"\033[0m")
            print("\n----------------------------------------------\n")
            self.startMenu()
            
        for task in self.task_list: # Muestra la lista de tareas existentes para ver cual queremos modificar
            print(json.dumps(task.get_task(), indent=4))
        print("\n----------------------------------------------\n")
        
        try:
            task_id = int(input("Introduce el ID de la tarea a modificar: ") )     
            print("\n----------------------------------------------\n")
            
            if task_id < 0: 
                raise Exception
            
            for task in self.task_list: # Bucle que compara el ID de la tarea con el que hemos introducido 
                task_info = task.get_task()
                
                if task_info["ID"] == task_id:
                    task.toggle_done() 
                    
                    
                    system("cls")
        
                    self.showTasks() 
            
            system("cls")
            
            print("----------------------------------------------")
            print("\033[91m"+"\n      ERROR! El ID no existe en la lista \n"+"\033[0m")

        except ValueError:
            system("cls")
            print("----------------------------------------------")
            print("\033[91m"+"\n      ERROR! Introduce un número válido \n"+"\033[0m")
            
            
        except Exception :
            system("cls")
            print("----------------------------------------------")
            print("\033[91m"+"\n    ERROR! Introduce un número mayor que 0 \n"+"\033[0m")
                
        self.taskDone()
            
    
    def showTasks(self):
        print("----------------------------------------------")
        print("               LISTA DE TAREAS")
        print("----------------------------------------------\n")
        
        if len(self.task_list) > 0: 
            for task in self.task_list: 
                print(json.dumps(task.get_task(), indent=4)) 

        else:
            print("   Lista vacía. Guarda tareas para comenzar.")
        
        print("\n----------------------------------------------\n")
            
        self.startMenu()
