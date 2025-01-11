/*
Los elfos del Polo Norte han creado un robot 🤖 especial que ayuda a Papá Noel a distribuir regalos dentro de un gran almacén. El robot se mueve en un plano 2D y partimos desde el origen (0, 0).

Queremos saber si, tras ejecutar una serie de movimientos, el robot vuelve a estar justo donde empezó.

Las órdenes básicas del robot son:

L: Mover hacia la izquierda
R: Mover hacia la derecha
U: Mover hacia arriba
D: Mover hacia abajo
Pero también tiene ciertos modificadores para los movimientos:

*: El movimiento se realiza con el doble de intensidad (ej: *R significa RR)
!: El siguiente movimiento se invierte (ej: R!L se considera como RR)
?: El siguiente movimiento se hace sólo si no se ha hecho antes (ej: R?R significa R)
Nota: Cuando el movimiento se invierte con ! se contabiliza el movimiento invertido y no el original. Por ejemplo, !U?U invierte el movimiento de U, por lo que contabiliza que se hizo el movimiento D pero no el U. Así !U?U se traduce como D?U y, por lo tanto, se haría el movimiento U final.

Debes devolver:

true: si el robot vuelve a estar justo donde empezó
[x, y]: si el robot no vuelve a estar justo donde empezó, devolver la posición donde se detuvo
*/
/** @param {string} moves
 * @returns {true|[number, number]} Return true if robot returns or position
 */
function isRobotBack(moves) {
    let x = 0, y = 0;
    let inversion = {
        'R': 'L',
        'L': 'R',
        'U': 'D',
        'D': 'U',
    }
    let inc = {
        'R': [1, 0],
        'L': [-1, 0],
        'U': [0, 1],
        'D': [0, -1]
    }

    for (let i = 0; i < moves.length; i++) {
        let move = moves[i];

        if ('*!?'.includes(move)) {
            if (move == "*")
                moves = moves.substring(0, i + 1) + moves[i + 1] + moves[i + 1] + moves.substring(i + 2)
            else if (move == "!") {

                moves = moves.substring(0, i + 1) + inversion[moves[i + 1]] + moves.substring(i + 2)
            }
            else {
                if (moves.indexOf(moves[i + 1]) < i + 1 && moves.indexOf(moves[i + 1]) !== -1) {
                    moves = moves.substring(0, i + 1) + moves.substring(i + 2)
                }
            }
        }
        else {
            x += inc[move][0];
            y += inc[move][1];
        }

    }

    return x == 0 && y == 0 ? true : [x, y];
}


console.log(isRobotBack('R'));    // [1, 0]
console.log(isRobotBack('RL'));    // true
console.log(isRobotBack('RLUD'));  // true
console.log(isRobotBack('*RU'));   // [2, 1]
console.log(isRobotBack('R*U'));   // [1, 2]*/
console.log(isRobotBack('LLL!R')); // [-4, 0]
console.log(isRobotBack('R?R'));   // [1, 0]
console.log(isRobotBack('U?D'));   // true
console.log(isRobotBack('R!L'));  // [2,0]
console.log(isRobotBack('U!D'));   // [0,2]
console.log(isRobotBack('R?L'));  // true
console.log(isRobotBack('U?U'));  // [0,1]
console.log(isRobotBack('*U?U')); // [0,2]
console.log(isRobotBack('U?D?U')); // true

console.log(isRobotBack('!U?U')); // true*/
