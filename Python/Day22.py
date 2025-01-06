"""
Santa Claus 🎅 está revisando una lista de juguetes únicos que podría incluir en su bolsa mágica de regalos. Quiere explorar todas las combinaciones posibles de juguetes. Quiere ver todas las combinaciones que realmente contengan al menos un juguete.

Tu tarea es escribir una función que, dado un array de juguetes, devuelva todas las combinaciones posibles.

Importante: Debes devolverlo en el orden que aparecen los juguetes y de combinaciones de 1 a n juguetes.
"""
def generate_gift_sets(gifts):
    result = []

    def helper(start, current):
        if current:
            result.append(list(current))  # Agregar una copia de la combinación actual

        for i in range(start, len(gifts)):
            current.append(gifts[i])  # Incluir el juguete actual
            helper(i + 1, current)  # Generar combinaciones con los siguientes juguetes
            current.pop()  # Retirar el juguete actual para explorar otras combinaciones

    helper(0, [])  # Comienza con un conjunto vacío y el índice 0
    result.sort(key=len)  # Ordenar las combinaciones por tamaño
    return result

# Ejemplo de uso:
print(generate_gift_sets(['car', 'doll', 'puzzle']))
# [
#   ['car'],
#   ['doll'],
#   ['puzzle'],
#   ['car', 'doll'],
#   ['car', 'puzzle'],
#   ['doll', 'puzzle'],
#   ['car', 'doll', 'puzzle']
# ]

print(generate_gift_sets(['ball']))
# [['ball']]

print(generate_gift_sets(['game', 'pc']))
# [
#   ['game'],
#   ['pc'],
#   ['game', 'pc']
# ]
