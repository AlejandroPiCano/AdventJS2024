"""
En el Polo Norte, los elfos tienen dos árboles binarios mágicos que generan energía 🌲🌲 para mantener encendida la estrella navideña ⭐️. Sin embargo, para que funcionen correctamente, los árboles deben estar en perfecta sincronía como espejos 🪞.

Dos árboles binarios son espejos si:

Las raíces de ambos árboles tienen el mismo valor.
Cada nodo del primer árbol debe tener su correspondiente nodo en la posición opuesta en el segundo árbol.
Y el árbol se representa con tres propiedades value, left y right. Dentro de estas dos últimas va mostrando el resto de ramas (si es que tiene):
"""
def is_trees_synchronized(tree1, tree2):  
    if tree1 is None and tree2 is None:
       return [True, None ]


    if tree1["value"] != tree2["value"]:    
        return [False, tree1["value"]]

    v1 =  is_trees_synchronized( tree1["left"] if "left" in tree1 else None, tree2["right"] if "right" in tree2 else None)
  
    v2 =  is_trees_synchronized(tree1["right"] if "right" in tree1 else None, tree2["left"] if "left" in tree2 else None)

    return [v1[0] and v2[0], tree1["value"] ]
  

tree6 = {
        "value": '🎄',
        "left": { "value": '⭐' },
       
      }
      
tree7 = {
        "value": '🎄',
      
        "right": { "value": '⭐' }
      }

print(is_trees_synchronized(tree6, tree7))