from datetime import datetime
from .paciente import Paciente
from .medico import Medico

class Turno:
    def __init__(self, paciente, medico, fecha_hora, especialidad):
        if paciente is None:
            raise ValueError("El paciente no puede ser None")
        if not isinstance(paciente, Paciente):
            raise ValueError("Debe proporcionar un Paciente valido")
        if medico is None:
            raise ValueError("El medico no puede ser None")
        if not isinstance(medico, Medico):
            raise ValueError("Debe proporcionar un Medico valido")
        if fecha_hora is None:
            raise ValueError("La fecha y hora no pueden ser None")
        if not isinstance(fecha_hora, datetime):
            raise ValueError("Debe proporcionar una fecha valida yyyy/mm/dd")
        if not especialidad or not especialidad.strip():
            raise ValueError("La especialidad no debe estar vacia")
        
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad.strip()

    def obtener_medico(self):
        return self.__medico
    
    def obtener_fecha_hora(self):
        return self.__fecha_hora
    
    def __str__(self):
        fecha_str = self.__fecha_hora.strftime("%d/%m/%Y %H:%M")
        return (f"Turno: {self.__paciente.obtener_dni()} ({str(self.__paciente).split(':')[1].split(',')[0].strip()}) "
                f"con {str(self.__medico).split(',')[0]} "
                f"- Especialidad: {self.__especialidad} "
                f"- Fecha: {fecha_str}")