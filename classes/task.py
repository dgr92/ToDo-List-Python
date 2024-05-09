import datetime

# Clase para cada tarea
class Task():
    def __init__(self, task_id, task_description):
        self.__task_id = task_id
        self.__task_description = task_description.capitalize()
        self.__task_date = datetime.datetime.now()
        self.__is_done = False
        
    def toggle_done(self): # Método que alterna el estado de la tarea 
        self.__is_done = not self.__is_done
        
    def get_task(self):
        return {
            "ID": self.__task_id,
            "Tarea": self.__task_description, 
            "Fecha": self.__task_date.strftime("%d-%M-%Y %H:%M"), 
            "Estado": "Completada" if self.__is_done else "Pendiente", 
        }