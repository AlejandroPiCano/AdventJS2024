/*
¡Se acerca el día para repartir regalos! Necesitamos apilar los regalos que transportaremos en el trineo 🛷 y para eso los vamos a meter en cajas 📦.

Los regalos se pueden meter en 4 cajas distintas, donde cada caja soporta 1, 2, 5, 10 de peso y se representan así:

    _
1: |_|
    _____
2: |_____|
    _____
5: |     |
   |_____|
     _________
10: |         |
    |_________|

// Representación en JavaScript:
const boxRepresentations = {
  1: [" _ ", "|_|"] ,
  2: [" ___ ", "|___|"],
  5: [" _____ ", "|     |", "|_____|"],
  10: [" _________ ", "|         |", "|_________|"]
}
Tu misión es que al recibir el peso de los regalos, uses las mínimas cajas posibles y que, además, las apiles de menos peso (arriba) a más peso (abajo). Siempre alineadas a la izquierda.

Además, ten en cuenta que al apilarlas, se reusa el borde inferior de la caja.
 */
function distributeWeight(weight) {
    function PaintBoxes(boxes){
     const rep = {
        1: [" _ ", "|_|"] ,
        2: [" ___ ", "|___|"],
        5: [" _____ ", "|     |", "|_____|"],
        10: [" _________ ", "|         |", "|_________|"]
      }
      let result = '';
      let before = '';
      for(let i = 0; i<boxes.length ; i++)
      {
        let box = boxes[i];

        if(before)
         { 
            result += before.padEnd(rep[box][0].length-1, "_") + "\n"
         }

        rep[box].map( (b,i) => {
            if((!before || i>0) && i< rep[box].length-1)
                result += rep[box][i]+  "\n"
        });

        before = rep[box][rep[box].length-1];
        if(i == boxes.length-1)
        {
            result+= before;
        }
      }
      return result;
    }
      
     let weights = [1,2,5,10];
     let boxes = []
             
        for(let i = weights.length-1; i>=0 && weight>0 ; i--)
        {
            let w = weights[i];
            while(weight - w >=0)
            {
                 weight-=w;
                 boxes.unshift(w);                
            }            
        }
          
      let result = PaintBoxes(boxes);
      return result;
    }

console.log(distributeWeight(18));

/*console.log(distributeWeight(2));

console.log(distributeWeight(3));

console.log(distributeWeight(4));

console.log(distributeWeight(5));

console.log(distributeWeight(6));*/