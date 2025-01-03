"""
Los elfos programadores están creando un pequeño ensamblador mágico para controlar las máquinas del taller de Santa Claus.

Para ayudarles, vamos a implementar un intérprete sencillo que soporte las siguientes instrucciones mágicas:

MOV x y: Copia el valor x (puede ser un número o el contenido de un registro) en el registro y
INC x: Incrementa en 1 el contenido del registro x
DEC x: Decrementa en 1 el contenido del registro x
JMP x y: Si el valor del registro x es 0 entonces salta a la instrucción en el índice y y sigue ejecutándose el programa desde ahí.
Comportamiento esperado:
Si se intenta acceder, incrementar o decrementar a un registro que no ha sido inicializado, se tomará el valor 0 por defecto.
El salto con JMP es absoluto y lleva al índice exacto indicado por y.
Al finalizar, el programa debe devolver el contenido del registro A. Si A no tenía un valor definido, retorna undefined.
"""

def is_numeric(s):
    try:
        int(s)  # Try converting to an integer
        return True
    except:
        return False
    
def compile(instructions):
  dict =  {}
  i=0

  while i < len(instructions):
    parts  = instructions[i].split(' ')
    
    if len(parts) == 3:
        command, value1, value2 = parts
    else:
       command, value1 = parts
       value2 = None

    if not is_numeric(value1) and dict.get(value1) == None:
      dict[value1] = 0
  
    if not is_numeric(value2) and value2 != None and dict.get(value2) == None:
      dict[value2] = 0

    if command == 'MOV':
      if not is_numeric(value1):        
        dict[value2] = dict[value1] 
      else:
        dict[value2] = int(value1)
    elif command == 'INC':
        dict[value1] += 1
    elif command == 'DEC':
        dict[value1] -= 1
    else:
        if(dict[value1] == 0):
            i = int(value2)-1
    i += 1

  return dict['A']

instructions = [
    'MOV -1 C', 
    'INC C', 
    'JMP C 1',
    'MOV C A',
    'INC A' 
  ]

print(compile(instructions))