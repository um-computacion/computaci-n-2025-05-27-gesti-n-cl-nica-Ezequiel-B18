import unittest
from datetime import datetime
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.receta import Receta

class TestReceta(unittest.TestCase):
    
    def setUp(self):
        self.paciente = Paciente("Pepito Juan", "87654321", "20/05/1985")
        self.medico = Medico("Dr. Juan Pepito", "MAT99999")
        self.medicamentos = ["Paracetamol 500mg", "Ibuprofeno 400mg"]
    
    def test_crear_receta(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        resultado = str(receta)
        
        self.assertIn("Pepito Juan", resultado)
        self.assertIn("Dr. Juan Pepito", resultado)
        self.assertIn("Paracetamol 500mg", resultado)
        self.assertIn("Ibuprofeno 400mg", resultado)
        
        self.assertIsInstance(receta._Receta__fecha, datetime)
    
    def test_error_sin_medicamentos(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, [])
    
    def test_error_medicamentos_none(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, None)
    
    def test_error_paciente_none(self):
        with self.assertRaises(ValueError):
            Receta(None, self.medico, self.medicamentos)
    
    def test_error_medico_none(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, None, self.medicamentos)
    
    def test_str_(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        resultado = str(receta)
        
        self.assertIn("Receta", resultado)
        self.assertIn("Pepito Juan", resultado)
        self.assertIn("Dr. Juan Pepito", resultado)
        self.assertIn("Paracetamol 500mg", resultado)


if __name__ == "__main__":
    unittest.main()