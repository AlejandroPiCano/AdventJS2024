/*
En el Polo Norte, los elfos tienen dos árboles binarios mágicos que generan energía 🌲🌲 para mantener encendida la estrella navideña ⭐️. Sin embargo, para que funcionen correctamente, los árboles deben estar en perfecta sincronía como espejos 🪞.

Dos árboles binarios son espejos si:

Las raíces de ambos árboles tienen el mismo valor.
Cada nodo del primer árbol debe tener su correspondiente nodo en la posición opuesta en el segundo árbol.
Y el árbol se representa con tres propiedades value, left y right. Dentro de estas dos últimas va mostrando el resto de ramas (si es que tiene):
*/
/**
 * @param {object} tree1 - The first binary tree.
 * @param {object} tree2 - The second binary tree.
 * @returns {[boolean, string]}
 */
function isTreesSynchronized(tree1, tree2) {    
    if(!tree1 && !tree2)
    {
       return [true, null ]
    }

    if(tree1.value !== tree2.value)
    {
        return [false, tree1.value]
    }

    let v1 =  isTreesSynchronized(tree1.left, tree2.right);
  
    let v2 =  isTreesSynchronized(tree1.right, tree2.left);

    return [v1[0] && v2[0], tree1.value ];
  }
/*
const tree1 = {
    value: '🎄',
    left: { value: '⭐' },
    right: { value: '🎅' }
  }
  
  const tree2 = {
    value: '🎄',
    left: { value: '🎅' },
    right: { value: '⭐' }
  }
  
    console.log(isTreesSynchronized(tree1, tree2)) ;// [true, '🎄']);

    const tree3 = {
        value: '🎄',
        left: { value: '🎅' },
        right: { value: '🎁' }
      }
      
      console.log(isTreesSynchronized(tree1, tree3)) // [false, '🎄']

      const tree4 = {
        value: '🎄',
        left: { value: '⭐' },
        right: { value: '🎅' }
      }
      
      console.log(isTreesSynchronized(tree1, tree4)) // [false, '🎄']
      
      console.log(isTreesSynchronized(
        { value: '🎅' },
        { value: '🧑‍🎄' }
      )); // [false, '🎅']

*/
      const tree6 = {
        value: '🎄',
        left: { value: '⭐' },
       
      }
      
      const tree7 = {
        value: '🎄',
      
        right: { value: '⭐' }
      }
      console.log(isTreesSynchronized(tree6, tree7)) // [false, '🎄']