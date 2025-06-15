from datetime import datetime
from .paciente import Paciente
from .medico import Medico

class Receta:
    def __init__(self, paciente, medico, medicamentos):
        if paciente is None:
            raise ValueError("El paciente no debe ser None")
        if not isinstance(paciente, Paciente):
            raise ValueError("Debe proporcionar un Paciente valido")
        if medico is None:
            raise ValueError("El medico no debe ser None")
        if not isinstance(medico, Medico):
            raise ValueError("Debe proporcionar un Medico valido")
        if medicamentos is None:
            raise ValueError("La lista de meds no debe ser None")
        if not medicamentos:
            raise ValueError("Debe haber al menos un medicamento")
        for medicamento in medicamentos:
            if not medicamento or not medicamento.strip():
                raise ValueError("Los medicamentos no pueden estar vacios")
            
        self.__paciente = paciente
        self.__medico = medico 
        self.__medicamentos = [med.strip() for med in medicamentos]
        self.__fecha = datetime.now()

    def __str__(self):
        fecha_str = self.__fecha.strftime("%d/%m/%Y %H:%M")
        medicamentos_str = ", ".join(self.__medicamentos)

        nombre_paciente = str(self.__paciente).split(':')[1].split(',')[0].strip()
        nombre_medico = str(self.__medico).split(',')[0].replace("Dr. ", "").strip()

        return (f"Receta - Paciente: {nombre_paciente}"
                f" - Medico: Dr. {nombre_medico}"
                f" - Medicamentos: {medicamentos_str}"
                f" - Fecha: {fecha_str}")