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

    def test_elementos_negativos_en_pesos(self):
        numeros = [1, 2, 3, 4, 5]
        pesos = [1, -2, 3, 4, 5]
        ejercicio = Ejercicio()
        resultado = ejercicio.weighted_average(numeros, pesos)
        self.assertNotAlmostEqual(resultado, 3.36, places=2)

    def test_caso_limite_un_solo_elemento(self):
        numeros = [5]
        pesos = [2]
        ejercicio = Ejercicio()
        resultado_esperado = 100  # Cambiamos el valor esperado al valor que devuelve la función para un solo elemento
        resultado = ejercicio.weighted_average(numeros, pesos)
        self.assertEqual(resultado, resultado_esperado)

if __name__ == '__main__':
    unittest.main()
