"""
Los elfos están trabajando arduamente para limpiar los caminos llenos de nieve mágica ❄️. Esta nieve tiene una propiedad especial: si dos montículos de nieve idénticos y adyacentes se encuentran, desaparecen automáticamente.

Tu tarea es escribir una función que ayude a los elfos a simular este proceso. El camino se representa por una cadena de texto y cada montículo de nieve un carácter.

Tienes que eliminar todos los montículos de nieve adyacentes que sean iguales hasta que no queden más movimientos posibles.
"""
def remove_snow(s: str) -> str:
    if len(s) <= 1:
        return s   
    for i in range(1, len(s)):
      if (s[i] == s[i-1]):    
       return remove_snow( s[:i-1] + s[i+1:]);    
    return s  

print(remove_snow('zxxzoz'))