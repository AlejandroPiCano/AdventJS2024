/*
Santa Claus 🎅 está decorando un árbol de Navidad mágico 🪄, que este año tiene una estructura especial en forma de árbol binario. Cada nodo del árbol representa un regalo, y Santa quiere saber la altura del árbol para colocar la estrella mágica en la punta.

Tu tarea es escribir una función que calcule la altura de un árbol binario. La altura de un árbol binario se define como el número máximo de niveles desde la raíz hasta una hoja. Un árbol vacío tiene una altura de 0.
 */
/**
   * @param {{ value: string; left: any; right: any }} tree
   * @returns {number} - Height of the tree.
   */
function treeHeight(tree) {   
    if(tree === null) return 0;
    let leftHeight = 1 + treeHeight(tree.left);
    let rightHeight = 1 + treeHeight(tree.right);
    return Math.max(leftHeight, rightHeight);
  }

  const tree = {
    value: '🎁',
    left: {
      value: '🎄',
      left: {
        value: '⭐',
        left: null,
        right: null
      },
      right: {
        value: '🎅',
        left: null,
        right: null
      }
    },
    right: {
      value: '❄️',
      left: null,
      right: {
        value: '🦌',
        left: null,
        right: null
      }
    }
  }
  
  // Representación gráfica del árbol:
  //        🎁
  //       /   \
  //     🎄     ❄️
  //    /  \      \
  //  ⭐   🎅      🦌
  
  // Llamada a la función
 console.log(treeHeight(tree));
  // Devuelve: 3