import unittest
from src.models.medico import Medico
from src.models.especialidad import Especialidad

class TestMedico(unittest.TestCase):

    def setUp(self): #Configuracion inicial para los tests
        self.pediatria = Especialidad("Pediatria", ["lunes", "miercoles", "viernes"])
        self.cardiologia = Especialidad("Cardiologia", ["martes", "jueves"])

    def test_crear_medico(self):
        medico = Medico("Dr. Juan Pepito", "MAT12345")

        self.assertEqual(medico.obtener_matricula(), "MAT12345")
        self.assertIn("Dr. Juan Pepito", str(medico))
        self.assertIn("MAT12345", str(medico))

    def test_agregar_especialidad(self):
        medico = Medico("Dr. Juan Pepito", "MAT12345")

        medico.agregar_especialidad(self.pediatria)
        self.assertEqual(medico.obtener_especialidad_para_dia("lunes"), "Pediatria")
        self.assertIn("Pediatria", str(medico))
    
    def test_duplicados_especialidad(self):
        medico = Medico("Dr. Carlitos", "MAT67890")

        medico.agregar_especialidad(self.pediatria)
        with self.assertRaises(ValueError):
            medico.agregar_especialidad(self.pediatria)

    def test_especialidad_para_dia_disponible(self):
        medico = Medico("Dr. Juanito", "MAT11111")
        medico.agregar_especialidad(self.pediatria)
        medico.agregar_especialidad(self.cardiologia)

        self.assertEqual(medico.obtener_especialidad_para_dia("lunes"), "Pediatria")
        self.assertEqual(medico.obtener_especialidad_para_dia("martes"), "Cardiologia")
        self.assertIsNone(medico.obtener_especialidad_para_dia("sabado"))

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Medico("", "MAT33333")

    def test_matricula_vacia(self):
        with self.assertRaises(ValueError):
            Medico("Dr. Juanito", "")

    def test_str_(self):
        medico = Medico("Dr. Pepito Juan", "MAT55555")
        medico.agregar_especialidad(self.pediatria)
        resultado = str(medico)

        self.assertIn("Dr. Pepito Juan", resultado)
        self.assertIn("MAT55555", resultado)
        self.assertIn("Pediatria", resultado)

if __name__ == "__main__":
    unittest.main()