"""
Los elfos están jugando con un tren 🚂 mágico que transporta regalos. Este tren se mueve en un tablero representado por un array de strings.

El tren está compuesto por una locomotora (@), seguida de sus vagones (o), y debe recoger frutas mágicas (*) que le sirve de combustible. El movimiento del tren sigue las siguientes reglas:

Recibirás dos parámetros board y mov.

board es un array de strings que representa el tablero:

@ es la locomotora del tren.
o son los vagones del tren.
* es una fruta mágica.
· son espacios vacíos.
mov es un string que indica el próximo movimiento del tren desde la cabeza del tren @:

'L': izquierda
'R': derecha
'U': arriba
'D': abajo.
Con esta información, debes devolver una cadena de texto:

'crash': Si el tren choca contra los bordes del tablero o contra sí mismo.
'eat': Si el tren recoge una fruta mágica (*).
'none': Si avanza sin chocar ni recoger ninguna fruta mágica.
"""

from typing import List, Literal

def move_train(board: List[str], mov: Literal['U', 'D', 'R', 'L']) -> Literal['none', 'crash', 'eat']:
  x=0
  y=0
  dict = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
  
  for x in range(len(board)):
    y = board[x].find('@')
    if y != -1:
        break
    
  coords = [x,y]  
  [x,y] = [i + j for i, j in zip(coords, dict[mov])]

  if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] == 'o':
    return 'crash'
  
  return  'eat' if  board[x][y] == '*' else 'none'

print(move_train([  '·····',  '*····',  '@····',  'o····',  'o····'],  'R'))
