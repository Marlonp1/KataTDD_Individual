class Ejercicio:
    def weighted_average(self, numeros, pesos):

        def weighted_average(self, numeros, pesos):
            if len(numeros) == 0 or len(pesos) == 0:
                return None  # Devolver None si una de las listas está vacía
            if len(numeros) != len(pesos):
                raise ValueError("Las listas de números y pesos deben tener la misma longitud")
            total_weighted_sum = sum(num * weight for num, weight in zip(numeros, pesos))
            total_weight = sum(pesos)
            return total_weighted_sum / total_weight