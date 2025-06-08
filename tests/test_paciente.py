import unittest
from src.models.paciente import Paciente

class TestPaciente(unittest.TestCase):

    def test_crear_paciente(self):
        paciente = Paciente("Pepito Juan", "12345678", "17/07/1977")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertIn("Pepito Juan", str(paciente))
        self.assertIn("12345678", str(paciente))
        self.assertIn("17/07/1977", str(paciente))

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Paciente("", "12345678", "17/07/1977")

    def test_dni_vacio(self):
        with self.assertRaises(ValueError):
            Paciente("Pepito Juan", "", "17/07/1977")

    def test_fecha_vacia(self):
        with self.assertRaises(ValueError):
            Paciente("Pepito Juan", "12345678", "")

    def test_dni_mal(self):
        with self.assertRaises(ValueError):
            Paciente("Pepito Juan", "ABC45678", "17/07/1977")

    def test_fecha_mala(self):
        with self.assertRaises(ValueError):
            Paciente("Pepito Juan", "12345678", "1977/07/17")

    def test_fecha_inexistente(self):
        with self.assertRaises(ValueError):
            Paciente("Pepito Juan", "12345678", "32/07/1977")
    
    def test_str(self):
        paciente = Paciente("Pepito Juan", "12345678", "17/07/1977")
        resultado = str(paciente)

        self.assertIn("Pepito Juan", resultado)
        self.assertIn("12345678", resultado)
        self.assertIn("17/07/1977", resultado)
            
if __name__ == "__main__":
    unittest.main()
