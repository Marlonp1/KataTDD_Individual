class Ejercicio:
    def weighted_average(self, numeros, pesos):
        if len(numeros) != len(pesos):
            raise ValueError("Las listas de números y pesos deben tener la misma longitud")
        total_weighted_sum = sum(num * weight for num, weight in zip(numeros, pesos))
        total_weight = sum(pesos)
        if total_weight == 0:
            return 0  # Si la suma de pesos es cero, devolver 0 para evitar la división por cero
        return total_weighted_sum / total_weight
