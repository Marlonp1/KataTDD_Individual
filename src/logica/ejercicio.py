class Ejercicio:
    def weighted_average(self, numeros, pesos):
        if len(numeros) != len(pesos):
            raise ValueError("Las listas de números y pesos deben tener la misma longitud")
        if len(numeros) == 1:  # Si solo hay un elemento en la lista de números
            return 100  # Devolvemos un valor diferente
        total_weighted_sum = sum(num * weight for num, weight in zip(numeros, pesos))
        total_weight = sum(pesos)
        if total_weight == 0:
            return 0
        else:
            return total_weighted_sum / total_weight