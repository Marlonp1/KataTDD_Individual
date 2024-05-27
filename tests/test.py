import unittest
from src.logica.ejercicio import Ejercicio

class TestEjercicio(unittest.TestCase):
    def test_longitud_diferente(self):
        numeros = [1, 2, 3, 4, 5]
        pesos = [1, 2, 3, 4]
        ejercicio = Ejercicio()
        with self.assertRaises(ValueError):
            ejercicio.weighted_average(numeros, pesos)

    def test_listas_vacias(self):
        numeros = []
        pesos = []
        ejercicio = Ejercicio()
        resultado = ejercicio.weighted_average(numeros, pesos)
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()
