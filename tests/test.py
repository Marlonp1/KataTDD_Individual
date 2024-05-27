import unittest
from src.logica.ejercicio import Ejercicio

class TestEjercicio(unittest.TestCase):
    def test_longitud_diferente(self):
        numeros = [1, 2, 3, 4, 5]
        pesos = [1, 2, 3, 4]
        ejercicio = Ejercicio()
        with self.assertRaises(ValueError):
            ejercicio.weighted_average(numeros, pesos)

if __name__ == '__main__':
    unittest.main()
