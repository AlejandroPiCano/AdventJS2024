/*
Los renos necesitan moverse para ocupar los establos, pero no puede haber más de un reno por establo. Además, para que los renos estén cómodos, debemos minimizar la distancia total que recorren para acomodarse.

Tenemos dos parámetros:

reindeer: Un array de enteros que representan las posiciones de los renos.
stables: Un array de enteros que representan las posiciones de los establos.
Hay que mover cada reno, desde su posición actual, hasta un establo. Pero hay que tener en cuenta que sólo puede haber un reno por establo.

Tu tarea es calcular el mínimo número de movimientos necesarios para que todos los renos acaben en un establo.

Nota: Ten en cuenta que el array de establos siempre tendrá el mismo tamaño que el array de renos y que siempre los establos serán únicos.
*/
/**
 * @param {number[]} reindeer
 * @param {number[]} stables
 * @returns {number}
 */
function minMovesToStables(reindeer, stables) {
   let min = 65535, pos = 0, result = 0;
   for (let i = 0; i < reindeer.length; i++) {
       for (let j = 0; j < stables.length; j++) {
           if (Math.abs(reindeer[i] - stables[j]) < min) {
              min = Math.abs(reindeer[i] - stables[j]);
              pos = j;
           }
       }
       result += min;
       min = 65535;
       delete stables[pos];
   }

    return result;
  }
  
  console.log(minMovesToStables([2, 6, 9], [3, 8, 5]) )// -> 3
  console.log(minMovesToStables([1, 1, 3], [1, 8, 4])) // -> 8