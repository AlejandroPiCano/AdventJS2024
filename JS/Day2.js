/*
Santa Claus 🎅 quiere enmarcar los nombres de los niños buenos para decorar su taller 🖼️, pero el marco debe cumplir unas reglas específicas. Tu tarea es ayudar a los elfos a generar este marco mágico.

Reglas:

Dado un array de nombres, debes crear un marco rectangular que los contenga a todos.
Cada nombre debe estar en una línea, alineado a la izquierda.
El marco está construido con * y tiene un borde de una línea de ancho.
La anchura del marco se adapta automáticamente al nombre más largo más un margen de 1 espacio a cada lado.
 */

/**
 * @param {string[]} names - Array of names to frame
 * @returns {string} The framed names
 */
function createFrame(names) {
    let longestLenght = -1;    

    //names.map((n) => {if (n.length > longestLenght) longestLenght = n.length;});
   for (let i = 0; i < names.length; i++) {
       if (names[i].length > longestLenght) {
        longestLenght = names[i].length;        
   } 
}
   
    let frame = '*'.repeat(longestLenght + 4);
    let result = frame + '\n';
    
    names.forEach((n) => { result +='* '+n+ ' '.repeat(longestLenght - n.length)+' *'+'\n';});
    result+= frame;
    
    return result;
  }


  console.log(createFrame(['midu', 'madeval']));

// Resultado esperado:
/****************
* midu        *
* madeval     *
* educalvolpz *
****************/

console.log(createFrame(['midu']));

// Resultado esperado:
/*********
* midu *
*********/

console.log(createFrame(['bb', 'a', 'ccc']));

// Resultado esperado:
/********
* a   *
* bb  *
* ccc *
********/

console.log(createFrame(['a', 'bb', 'ccc', 'dddd']));