from .especialidad import Especialidad

class Medico:
    def __init__(self, nombre, matricula):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del medico no debe estar vacio")
        if not matricula or not matricula.strip():
            raise ValueError("La matricula no debe estar vacia")
        
        self.__nombre = nombre.strip()
        self.__matricula = matricula.strip()
        self.__especialidades = []

    def agregar_especialidad(self, especialidad):
        if not isinstance(especialidad, Especialidad):
            raise ValueError("Debe proporcionar una especialidad valida")
        for esp_existente in self.__especialidades:
            if esp_existente.obtener_especialidad() == especialidad.obtener_especialidad():
                raise ValueError(f"La especialidad {especialidad.obtener_especialidad()} ya esta registrada para este medico.")
        self.__especialidades.append(especialidad)

    def obtener_especialidad_para_dia(self, dia):
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia):
                return especialidad.obtener_especialidad()
            
        return None
    
    def obtener_matricula(self):
        return self.__matricula
    
    def __str__(self):
        especialidades_str = ""
        if self.__especialidades:
            nombres_esp = [esp.obtener_especialidad() for esp in self.__especialidades]
            especialidades_str = f" - Especialidades: {', '.join(nombres_esp)}"
        return f"Dr. {self.__nombre}, Matricula: {self.__matricula}, {especialidades_str}"