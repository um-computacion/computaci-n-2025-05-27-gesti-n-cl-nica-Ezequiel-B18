from datetime import datetime 
from .models.clinica import Clinica
from .models.paciente import Paciente
from .models.medico import Medico
from .models.especialidad import Especialidad
from .exceptions import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def menu(self):
        print("\nSistema de gestion de clinica")
        print("-" * 50)
        print("1 - Agregar paciente")
        print("2 - Agregar medico")
        print("3 - Agendar turno")
        print("4 - Agregar especialidad a medico")
        print("5 - Emitir receta")
        print("6 - Ver historia clinica")
        print("7 - Ver todos los turnos")
        print("8 - Ver todos los pacientes")
        print("9 - Ver todos los medicos")
        print("0 - Salir")

    def ejecutar(self):
        while True:
            self.menu()

            try:
                opcion = input("Selecciona una opcion: ").strip()

                if opcion == "0":
                    print("\nBye bye")
                    break
                elif opcion == "1":
                    self.agregar_paciente()
                elif opcion == "2":
                    self.agregar_medico()
                elif opcion == "3":
                    self.agendar_turno()
                elif opcion == "4":
                    self.agregar_especialidad_a_medico()
                elif opcion == "5":
                    self.emitir_receta()
                elif opcion == "6":
                    self.ver_historia_clinica()
                elif opcion == "7":
                    self.ver_todos_los_turnos()
                elif opcion == "8":
                    self.ver_todos_los_pacientes()
                elif opcion == "9":
                    self.ver_todos_los_medicos()
                else:
                    print("Opcion invalida. Seleccione de vuelta")
            except KeyboardInterrupt:
                print("Hasta luego")
                break
            except Exception as e:
                print(f"Error inesperado: {e}")
                input("\nEnter para continuar")

    def agregar_paciente(self):
        print("\nAgregar paciente")
        print("-" * 50)

        try:
            nombre = input("Nombre completo: ").strip()
            dni = input("DNI: " ).strip()
            fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()

            paciente = Paciente(nombre, dni, fecha_nacimiento)
            self.clinica.agregar_paciente(paciente)

            print("Paciente agregado")
            print(f"{paciente}")
        except ValueError as e:
            print(f"Error en los datos: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        input("\nEnter para continuar")

    def agregar_medico(self):
        print("\nAgregar medico")
        print("-" * 50)

        try:
            nombre = input("Nombre completo del medico: ").strip()
            matricula = input("Matricula: ").strip()

            medico = Medico(nombre, matricula)

            print("\nAgregue especialidades (Enter sin escribir nada para terminar): ")

            while True:
                especialidad_nombre = input("Especialidad: ").strip()
                if not especialidad_nombre:
                    break

                dias = self.solicitar_dias_atencion()
                if dias:
                    try:
                        especialidad = Especialidad(especialidad_nombre, dias)
                        medico.agregar_especialidad(especialidad)
                        print(f"Especialidad '{especialidad_nombre}' agregada")
                    except ValueError as e:
                        print(f"Error: {e}")
                        continue
                else:
                    print("No se proporcionaron dias validos")
                    continue

            self.clinica.agregar_medico(medico)

            print("Medico agregado")
            print(f"{medico}")
        
        except ValueError as e:
            print(f"Error en los datos: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

        input("\nEnter para continuar")
    
    def solicitar_dias_atencion(self):
        print("Dias disponibles: lunes, martes, miercoles, jueves, viernes, sabado, domingo")
        dias_input = input("Dias de atencion: (separados por comas): ").strip()

        if not dias_input:
            return []
        
        dias = [dia.strip() for dia in dias_input.split(",") if dia.strip()]
        return dias
    
    def agendar_turno(self):
        print("\nAgendar turno")
        print("-" * 50)

        try:
            dni = input("DNI: ").strip()
            matricula = input("Matricula medico: ").strip()
            especialidad = input("Especialidad solicitada: ").strip()

            fecha_str = input("Fecha del turno (dd/mm/aaaa): ").strip()
            hora_str = input("Hora del turno (HH:MM): ").strip()

            fecha_hora = self.parse_fecha_hora(fecha_str, hora_str)

            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)

            print("Turno agendado")
            print(f"Paciente DNI: {dni}")
            print(f"Medico: {matricula}")
            print(f"Fecha: {fecha_hora.strftime('%d/%m/%Y %H:%M')}")
        
        except (PacienteNoEncontradoException, MedicoNoEncontradoException,
                MedicoNoDisponibleException, TurnoOcupadoException) as e:
            print(f"{e}")
        except ValueError as e:
            print(f"Error en los datos: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

        input("\nEnter para continuar")

    def agregar_especialidad_a_medico(self):
        print("\nAgregar especialidad a medico")
        print("-" * 50)

        try:
            matricula = input("Matricula del medico: ").strip()

            medico = self.clinica.obtener_medico_por_matricula(matricula)

            especialidad_nombre = input("Nombre especialidad: ").strip()
            dias = self.solicitar_dias_atencion()

            if dias:
                especialidad = Especialidad(especialidad_nombre, dias)
                medico.agregar_especialidad(especialidad)

                print("Especialidad agregada")
                print(f"{especialidad}")
            else:
                print("Dias invalidos")
        
        except MedicoNoEncontradoException as e:
            print(f"{e}")
        except ValueError as e:
            print(f"Error en los datos: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

        input("\nEnter para continuar")

    def emitir_receta(self):
        print("\nEmitir receta")
        print("-" * 50)

        try:
            dni = input("DNI del paciente: ").strip()
            matricula = input("Matricula medico: ").strip()

            print("\nMedicamentos (Enter sin nada para terminar): ")
            medicamentos = []
            
            while True:
                medicamento = input("Medicamento: ").strip()
                if not medicamento: 
                    break
                medicamentos.append(medicamento)

            if not medicamentos:
                print("Debe ingresar por lo menos un medicamento")
                return
            
            self.clinica.emitir_receta(dni, matricula, medicamentos)

            print("Receta emitida")
            print(f"Paciente DNI: {dni}")
            print(f"Medico: {matricula}")
            print(f"Medicamentos: {', '.join(medicamentos)}")
        
        except (PacienteNoEncontradoException, MedicoNoEncontradoException,
                RecetaInvalidaException) as e:
            print(f"{e}")
        except ValueError as e:
            print(f"Error en los datos: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

        input("\nEnter para continuar")

    def ver_historia_clinica(self):
        print("\n Ver historia clinica")
        print("-" * 50)

        try:
            dni = input("DNI paciente: ").strip()

            historia = self.clinica.obtener_historia_clinica(dni)

            print("\n" + "-" * 50)
            print(historia)
            print("-" * 50)

        except PacienteNoEncontradoException as e:
            print(f"{e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        input("\nEnter para continuar")

    def ver_todos_los_turnos(self):
        print("\nTodos los turnos")
        print("-" * 50)

        try:
            turnos = self.clinica.obtener_turnos()

            if not turnos:
                print("No hay turnos agendados")

            else:
                print(f"Total de turnos: {len(turnos)}")
                print("-" * 80)

            for i, turno in enumerate(turnos, 1):
                print(f"{i}. {turno}")

        except Exception as e:
            print(f"Error inesperado: {e}")

        input("\nEnter para continuar")

    def ver_todos_los_pacientes(self):
        print("\nTodos los pacientes")
        print("-" * 50)

        try:
            pacientes = self.clinica.obtener_pacientes()
            
            if not pacientes:
                print("No hay pacientes registrados")
            else:
                print(f"Total de pacientes: {len(pacientes)}")
                print("-" * 50)

                for i, paciente in enumerate(pacientes, 1):
                    print(f"{i}. {paciente}")

        except Exception as e:
            print(f"Error inesperado: {e}")

        input("\nEnter para continuar")
    
    def ver_todos_los_medicos(self):
        print("\nTodos los medicos")
        print("-" * 50)

        try:
            medicos = self.clinica.obtener_medicos()

            if not medicos:
                print("No hay medicos registrados")
            else:
                print(f"Total de medicos: {len(medicos)}")
                print(f"-" * 50)

                for i, medico in enumerate(medicos, 1):
                    print(f"{i}. {medico}")
     
        except Exception as e:
            print(f"Error inesperado: {e}")

        input("\nEnter para continuar")

    def parse_fecha_hora(self, fecha_str, hora_str):
        try:
            fecha_hora_str = f"{fecha_str} {hora_str}"
            return datetime.strptime(fecha_hora_str, "%d/%m/%Y %H:%M")
        except ValueError:
            raise ValueError("Formato de fecha u hora invalido. (dd/mm/aaaa)")

    