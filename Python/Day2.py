
#Santa Claus 🎅 quiere enmarcar los nombres de los niños buenos para decorar su taller 🖼️, pero el marco debe cumplir unas reglas específicas. Tu tarea es ayudar a los elfos a generar este marco mágico.
#Reglas:
#Dado un array de nombres, debes crear un marco rectangular que los contenga a todos.
#Cada nombre debe estar en una línea, alineado a la izquierda.
#El marco está construido con * y tiene un borde de una línea de ancho.
#La anchura del marco se adapta automáticamente al nombre más largo más un margen de 1 espacio a cada lado.
 

def createFrame(names):  
  longestLenght = -1; 
  for name in names:
        if len(name) > longestLenght:           
            longestLenght = len(name)
  
  frame = '*' * (longestLenght + 4) + '\n'
  for name in names:
        frame += '* ' + name + ' ' * (longestLenght - len(name)) + ' *\n'   
  frame += '*' * (longestLenght + 4)
  return frame

print(createFrame(['bb', 'a', 'ccc']))
