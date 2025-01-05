/*
Al Polo Norte ha llegado ChatGPT y el elfo Sam Elfman está trabajando en una aplicación de administración de regalos y niños.

Para mejorar la presentación, quiere crear una función drawTable que reciba un array de objetos y lo convierta en una tabla de texto.

La tabla dibujada debe representar los datos del objeto de la siguiente manera:

Tiene una cabecera con el nombre de la columna.
El nombre de la columna pone la primera letra en mayúscula.
Cada fila debe contener los valores de los objetos en el orden correspondiente.
Cada valor debe estar alineado a la izquierda.
Los campos dejan siempre un espacio a la izquierda.
Los campos dejan a la derecha el espacio necesario para alinear la caja.
*/
function drawTable(data) {
    if(data == null || data.length === 0) return '';

    let result = '';
    const clengths = 
    Object.keys(data[0]).map(item => Math.max(...data.map(i => i[item].toString().length),
     item.length))
    
    let borders = '+' + clengths.map(c => '-'.repeat(c + 2) ).join('+') + '+';
    result += borders + '\n';

    result += '| ' + 
    Object.keys(data[0]).map((item,i) => (item.charAt(0).toUpperCase() + item.slice(1)).
    padEnd(clengths[i])).
    join(' | ') + ' |\n';
   
    result += borders + '\n';

    result += data.map(item => "| " + Object.values(item)
	.map((c, i) => c.toString().padEnd(clengths[i])).join(" | ") + " |").join("\n")+ '\n';

    result += borders;

    return result;
  }

  console.log(drawTable([
    { name: 'Alice', city: 'London' },
    { name: 'Bob', city: 'Paris' },
    { name: 'Charlie', city: 'New York' }
  ]));

  console.log(drawTable([
    { name: '', city: '' },
    { name: '', city: '' },
    { name: '', city:  1.2333333344 }
  ]));

  console.log(drawTable([
    { a: '', b: '' },
    { a: '', b: '' },
    { a: '', b: '' }
  ]));
  