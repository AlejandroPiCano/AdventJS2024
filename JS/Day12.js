/*
Estás en un mercado muy especial en el que se venden árboles de Navidad 🎄. Cada uno viene decorado con una serie de adornos muy peculiares, y el precio del árbol se determina en función de los adornos que tiene.

*: Copo de nieve - Valor: 1
o: Bola de Navidad - Valor: 5
^: Arbolito decorativo - Valor: 10
#: Guirnalda brillante - Valor: 50
@: Estrella polar - Valor: 100
Normalmente se sumarían todos los valores de los adornos y ya está…

Pero, ¡ojo! Si un adorno se encuentra inmediatamente a la izquierda de otro de mayor valor, en lugar de sumar, se resta su valor.
*/
function calculatePrice(ornaments) {
    let total = 0;
    let ornamentsOrder = ["*", "o",  "^",  "#",  "@"]
    let ornamentsValues = {
        "*": 1, 
        "o": 5,  
        "^": 10,
        "#": 50,
        "@": 100
        }

    for (let i = 0; i < ornaments.length; i++) {   

        let value = ornamentsValues[ornaments[i]];
        if(!value) return undefined;
        let orderI = ornamentsOrder.indexOf(ornaments[i]);        
        total +=  ( i < ornaments.length-1 && orderI < ornamentsOrder.indexOf(ornaments[i+1]))? value * -1 : value;  
    }
    return total      
  }

  console.log(calculatePrice("#@Z"));   // undefined
  /*
console.log( calculatePrice('***'))   // 3   (1 + 1 + 1)
console.log(calculatePrice('*o'));    // Output: 4   (-1 + 5)
console.log(calculatePrice('o*'));    // Output: 6   (5 + 1)
console.log(calculatePrice('*o*'));   // Output: 5   (-1 + 5 + 1)
console.log(calculatePrice('**o*'));  // Output: 6   (1 - 1 + 5 + 1)
console.log(calculatePrice('o***'));  // Output: 8   (5 + 3)
console.log(calculatePrice('*o@'));   // Output: 94  (-1 + 5 + 100 - 1)
console.log(calculatePrice('*#'));    // Output: 49  (-1 + 50)
console.log(calculatePrice('@@@'));   // Output: 300 (100 + 100 + 100)
console.log(calculatePrice('#@'));    // Output: 150 (50 + 100)
console.log(calculatePrice('#@Z'));   // Output: undefined (Z is unknown)*/