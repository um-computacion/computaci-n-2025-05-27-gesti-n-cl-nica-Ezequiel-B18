import unittest
from datetime import datetime
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad
from src.models.turno import Turno

class TestTurno(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Pepito Juan", "12345678", "17/07/1977")
        self.medico = Medico("Dr. Juan Pepito", "MAT11111")
        self.pediatria = Especialidad("Pediatria", ["lunes", "miercoles", "viernes"])
        self.medico.agregar_especialidad(self.pediatria)
        self.fecha_hora = datetime(2025, 6, 16, 14, 30)

    def test_crear_turno(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Pediatria")

        self.assertEqual(turno.obtener_medico(), self.medico)
        self.assertEqual(turno.obtener_fecha_hora(), self.fecha_hora)
        self.assertIn("Pepito Juan", str(turno))
        self.assertIn("Dr. Juan Pepito", str(turno))
        self.assertIn("Pediatria", str(turno))

    def test_paciente_none(self):
        with self.assertRaises(ValueError):
            Turno(None, self.medico, self.fecha_hora, "Pediatria")

    def test_medico_none(self):
        with self.assertRaises(ValueError):
            Turno(self.paciente, None, self.fecha_hora, "Pediatria")

    def test_fecha_none(self):
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, None, "Pediatria")

    def test_especialidad_vacia(self):
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, self.fecha_hora, "")

    def test_str_(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Pediatria")
        resultado = str(turno)

        self.assertIn("Pepito Juan", resultado)
        self.assertIn("Dr. Juan Pepito", resultado)
        self.assertIn("Pediatria", resultado)
        self.assertIn("2025", resultado)

if __name__ == "__main__":
    unittest.main()