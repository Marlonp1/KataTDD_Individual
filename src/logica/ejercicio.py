class Ejercicio:
    def weighted_average(self, numeros, pesos):
        if len(numeros) != len(pesos):
            return -1
        total_weighted_sum = sum(num * weight for num, weight in zip(numeros, pesos))
        total_weight = sum(pesos)
        return total_weighted_sum / total_weight
