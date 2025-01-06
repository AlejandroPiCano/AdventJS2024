"""
El Grinch ha estado haciendo de las suyas en el Polo Norte y ha sembrado bombas de carbón explosivo 💣 en la fábrica de juguetes de los duendes. Quiere que todos los juguetes queden inutilizados y por eso ha dejado una cuadrícula donde algunas celdas tienen carbón explosivo (true) y otras están vacías (false).

Los duendes necesitan tu ayuda para mapear las zonas peligrosas. Cada celda vacía debe mostrar un número que indique cuántas bombas de carbón explosivo hay en las posiciones adyacentes, incluidas las diagonales.
"""
def detect_bombs(grid: list[list[bool]]) -> list[list[int]]:
    result = []
    values = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

    for i in range(len(grid)):
        result.append([])
        for j in range(len(grid[i])):
            count = 0
            for value in values:
                x = i + value[0]
                y = j + value[1]
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[i]):
                    if grid[x][y]:
                        count += 1
            result[i].append(count)
    return result

print( detect_bombs([
    [True, False, False],
    [False, True, False],
    [False, False, False]
  ]))