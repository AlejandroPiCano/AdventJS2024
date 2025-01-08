/*
¡Ya hemos repartido todos los regalos! De vuelta al taller, ya comienzan los preparativos para el año que viene.
Un elfo genio está creando un lenguaje de programación mágico 🪄, que ayudará a simplificar la entrega de regalos a los niños en 2025.
Los programas siempre empiezan con el valor 0 y el lenguaje es una cadena de texto donde cada caracter representa una instrucción:
> Se mueve a la siguiente instrucción
+ Incrementa en 1 el valor actual
- Decrementa en 1 el valor actual
[ y ]: Bucle. Si el valor actual es 0, salta a la instrucción después de ]. Si no es 0, vuelve a la instrucción después de [
{y }: Condicional. Si el valor actual es 0, salta a la instrucción después de }. Si no es 0, sigue a la instrucción después de {
Tienes que devolver el valor del programa tras ejecutar todas las instrucciones.
*/
/**
 * @param {string} code - The magical program to execute
 * @returns {number} - The final value after executing the program
 */
function execute(code) {
    let result = 0;
    let indexCycle = -1;

    for(let i = 0; i< code.length;i++)
    {
        switch(code[i])
        {
            case '>':
                continue;

            case '+':
                result++;
                break;
            
            case '-':
               result--;
               break;
            case '[':
               indexCycle = i;
               break;
            case ']':
                if(result==0)
                {                    
                    continue
                }
                else
                {
                    i = indexCycle
                }
                break;
            case '{':
                if(result === 0)
                {
                    i = code.indexOf("}", i)  
                }               
                break;
            case '}':
                    continue;

        }
    }
    return result;
  }
    

console.log( execute('+++')); // 3
console.log( execute('+--')); // -1
console.log( execute('>+++[-]')); // 0
console.log( execute('>>>+{++}')); // 3
console.log( execute('+{[-]+}+')); // 2
console.log( execute('{+}{+}{+}')); // 0
console.log( execute('------[+]++')); // 2
console.log( execute('-[++{-}]+{++++}')); // 5