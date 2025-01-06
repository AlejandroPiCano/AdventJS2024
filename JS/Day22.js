/*
Santa Claus 🎅 está revisando una lista de juguetes únicos que podría incluir en su bolsa mágica de regalos. Quiere explorar todas las combinaciones posibles de juguetes. Quiere ver todas las combinaciones que realmente contengan al menos un juguete.

Tu tarea es escribir una función que, dado un array de juguetes, devuelva todas las combinaciones posibles.

Importante: Debes devolverlo en el orden que aparecen los juguetes y de combinaciones de 1 a n juguetes.
 */
function generateGiftSets(gifts) {
    const result = [];
    
    function helper(start, current) {
        if (current.length > 0) {
            result.push([...current]); // Agregar una copia del conjunto actual
        }

        for (let i = start; i < gifts.length; i++) {
            current.push(gifts[i]); // Incluir el juguete actual
            helper(i + 1, current); // Generar combinaciones con los siguientes juguetes
            current.pop(); // Retirar el juguete actual para explorar otras combinaciones
        }
    }
        
    helper(0, []);
    
    return result.sort((a, b) => a.length - b.length);
  }

  console.log(
    generateGiftSets(['car', 'doll', 'puzzle'])
// [
//   ['car'],
//   ['doll'],
//   ['puzzle'],
//   ['car', 'doll'],
//   ['car', 'puzzle'],
//   ['doll', 'puzzle'],
//   ['car', 'doll', 'puzzle']
// ]
  )