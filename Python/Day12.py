"""
Estás en un mercado muy especial en el que se venden árboles de Navidad 🎄. Cada uno viene decorado con una serie de adornos muy peculiares, y el precio del árbol se determina en función de los adornos que tiene.

*: Copo de nieve - Valor: 1
o: Bola de Navidad - Valor: 5
^: Arbolito decorativo - Valor: 10
#: Guirnalda brillante - Valor: 50
@: Estrella polar - Valor: 100
Normalmente se sumarían todos los valores de los adornos y ya está…

Pero, ¡ojo! Si un adorno se encuentra inmediatamente a la izquierda de otro de mayor valor, en lugar de sumar, se resta su valor.
"""

def calculate_price(ornaments: str) -> int:
  total = 0
  ornamentsOrder = ["*", "o",  "^",  "#",  "@"]
  ornamentsValues = {
        "*": 1, 
        "o": 5,  
        "^": 10,
        "#": 50,
        "@": 100
        }
  for i in range(len(ornaments)):
    value =  ornamentsValues[ornaments[i]]
    if value is None: return None
    orderI = ornamentsOrder.index(ornaments[i]);    
    total +=  value * -1 if (i < len(ornaments)-1 and orderI < ornamentsOrder.index(ornaments[i+1])) else value;   
  return total

print( calculate_price('***')) #Output: 3   (1 + 1  + 1)
print(calculate_price('*o'));    #Output: 4   (-1 + 5)
print(calculate_price('o*'));   # Output: 6   (5 + 1)
print(calculate_price('*o*'));   # Output: 5   (-1 + 5 + 1)