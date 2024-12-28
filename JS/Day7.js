/*
¡El grinch 👹 ha pasado por el taller de Santa Claus! Y menudo desastre ha montado. Ha cambiado el orden de algunos paquetes, por lo que los envíos no se pueden realizar.
Por suerte, el elfo Pheralb ha detectado el patrón que ha seguido el grinch para desordenarlos. Nos ha escrito las reglas que debemos seguir para reordenar los paquetes. Las instrucciones que siguen son:
Recibirás un string que contiene letras y paréntesis.
Cada vez que encuentres un par de paréntesis, debes voltear el contenido dentro de ellos.
Si hay paréntesis anidados, resuelve primero los más internos.
Devuelve el string resultante con los paréntesis eliminados, pero con el contenido volteado correctamente.
 */

function fixPackages(packages) {   
    let parenthesisStack = [];
    for (let i = 0; i < packages.length; i++) {
        if (packages[i] == '(' ) {
            parenthesisStack.push(i);
        }
        else if(packages[i] == ')')
        {
            if(parenthesisStack.length > 0)
            {
                let index = parenthesisStack.pop();
                let substring = packages.substring(index, i+1).split("").reverse().join("");
                packages = packages.substring(0, index) + substring + packages.substring(i+1);
            }
        }
    }
   
    return packages.replace(/\(|\)/g, "");
  }

console.log(fixPackages('a(cb)de'))
// ➞ "abcde"
// Volteamos "cb" dentro de los paréntesis

console.log(fixPackages('a(bc(def)g)h'))
// ➞ "agdefcbh"
// 1º volteamos "def" → "fed", luego volteamos "bcfedg" → "gdefcb"

console.log(fixPackages('abc(def(gh)i)jk'))
// ➞ "abcighfedjk"
// 1º volteamos "gh" → "hg", luego "defhgi" → "ighfed"

console.log(fixPackages('a(b(c))e'))
// ➞ "acbe"
// 1º volteamos "c" → "c", luego "bc" → "cb"