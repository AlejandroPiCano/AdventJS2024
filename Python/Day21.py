"""
Santa Claus 🎅 está decorando un árbol de Navidad mágico 🪄, que este año tiene una estructura especial en forma de árbol binario. Cada nodo del árbol representa un regalo, y Santa quiere saber la altura del árbol para colocar la estrella mágica en la punta.

Tu tarea es escribir una función que calcule la altura de un árbol binario. La altura de un árbol binario se define como el número máximo de niveles desde la raíz hasta una hoja. Un árbol vacío tiene una altura de 0.
"""
def tree_height(tree):
    if tree == None: return 0
    leftHeight = 1 + tree_height(tree["left"])
    rightHeight = 1 + tree_height(tree["right"])
    return max(leftHeight, rightHeight)

print(tree_height(
    tree = {
    "value": "🎁",
    "left": {
        "value": "🎄",
        "left": {
            "value": "⭐",
            "left": None,
            "right": None
        },
        "right": {
            "value": "🎅",
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": "❄️",
        "left": None,
        "right": {
            "value": "🦌",
            "left": None,
            "right": None
        }
    }
}

))