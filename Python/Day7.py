#¡El grinch 👹 ha pasado por el taller de Santa Claus! Y menudo desastre ha montado. Ha cambiado el orden de algunos paquetes, por lo que los envíos no se pueden realizar.
#Por suerte, el elfo Pheralb ha detectado el patrón que ha seguido el grinch para desordenarlos. Nos ha escrito las reglas que debemos seguir para reordenar los paquetes. Las instrucciones que siguen son:
#Recibirás un string que contiene letras y paréntesis.
#Cada vez que encuentres un par de paréntesis, debes voltear el contenido dentro de ellos.
#Si hay paréntesis anidados, resuelve primero los más internos.
#Devuelve el string resultante con los paréntesis eliminados, pero con el contenido volteado correctamente.

def fix_packages(packages):
  parenthesisStack = []
  for i in range(len(packages)):
    if packages[i] =='(':
        parenthesisStack.append(i)
    elif packages[i] == ')':
       if len(parenthesisStack) > 0:
          index = parenthesisStack.pop()
          substring =  ''.join(reversed(packages[index:i+1]))
          packages = packages[:index] + substring + packages[i+1:]
  return packages.replace('(', '').replace(')', '')

print(fix_packages('a(cb)de'))

print(fix_packages('a(bc(def)g)h'))