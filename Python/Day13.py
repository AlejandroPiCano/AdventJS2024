"""
Los elfos del Polo Norte han creado un robot 🤖 especial que ayuda a Papá Noel a distribuir regalos dentro de un gran almacén. El robot se mueve en un plano 2D y partimos desde el origen (0, 0).

Queremos saber si, tras ejecutar una serie de movimientos, el robot vuelve a estar justo donde empezó.

Las órdenes básicas del robot son:

L: Mover hacia la izquierda
R: Mover hacia la derecha
U: Mover hacia arriba
D: Mover hacia abajo
Pero también tiene ciertos modificadores para los movimientos:

*: El movimiento se realiza con el doble de intensidad (ej: *R significa RR)
!: El siguiente movimiento se invierte (ej: R!L se considera como RR)
?: El siguiente movimiento se hace sólo si no se ha hecho antes (ej: R?R significa R)
Nota: Cuando el movimiento se invierte con ! se contabiliza el movimiento invertido y no el original. Por ejemplo, !U?U invierte el movimiento de U, por lo que contabiliza que se hizo el movimiento D pero no el U. Así !U?U se traduce como D?U y, por lo tanto, se haría el movimiento U final.

Debes devolver:

true: si el robot vuelve a estar justo donde empezó
[x, y]: si el robot no vuelve a estar justo donde empezó, devolver la posición donde se detuvo
"""
def is_robot_back(moves: str) -> bool | list[int]:
    x = 0
    y = 0
    i = 0
    inversion = {
        'R': 'L',
        'L': 'R',
        'U': 'D',
        'D': 'U',
    }
    inc = {
        'R': [1, 0],
        'L': [-1, 0],
        'U': [0, 1],
        'D': [0, -1]
    }

    while i < len(moves):
        move = moves[i]

        if move in '*!?':
            if move == "*":
                moves = moves[:i + 1] + moves[i + 1] + moves[i + 1] + moves[i + 2:]
            elif move == "!":
                moves = moves[:i + 1] + inversion[moves[i + 1]] + moves[i + 2:]
            else:  # Para el caso de `?`
               if moves.index(moves[i + 1]) < i + 1 and moves.index(moves[i + 1]) != -1:
                moves = moves[:i + 1] + moves[i + 2:]                         
        else:
           x += inc[move][0]
           y += inc[move][1]  
        i+=1    

    return True if x == 0 and y == 0 else [x, y]

print(is_robot_back('R'))       # [1, 0]
print(is_robot_back('RL'))      # True
print(is_robot_back('RLUD'))    # True
print(is_robot_back('*RU'))     # [2, 1]
print(is_robot_back('R*U'))     # [1, 2]
print(is_robot_back('LLL!R'))   # [-4, 0]
print(is_robot_back('R?R'))     # [1, 0]
print(is_robot_back('U?D'))     # True
print(is_robot_back('R!L'))     # [2, 0]
print(is_robot_back('U!D'))     # [0, 2]
print(is_robot_back('R?L'))     # True
print(is_robot_back('U?U'))     # [0, 1]
print(is_robot_back('U?D?U'))
print(is_robot_back('!U?U'))
print(is_robot_back('*U?U'))   


