/*
Los elfos 🧝🧝‍♂️ de Santa Claus han encontrado un montón de botas mágicas desordenadas en el taller. Cada bota se describe por dos valores:

type indica si es una bota izquierda (I) o derecha (R).
size indica el tamaño de la bota.
Tu tarea es ayudar a los elfos a emparejar todas las botas del mismo tamaño que tengan izquierda y derecha. Para ello, debes devolver una lista con los pares disponibles después de emparejar las botas.

¡Ten en cuenta que puedes tener más de una zapatilla emparejada del mismo tamaño!
 */
function organizeShoes(shoes) {
    let result = [];
    let sizes = [];
    for (let i = 0; i < shoes.length; i++) {
        let shoe = shoes[i];
        let size = sizes[shoe.size];

        if(size)
        {
           if(size[shoe.type == "I"? "R":"I"])
           {
               result.push(shoe.size);
               size[shoe.type == "I"? "R":"I"]--;
           }
           else
           {
               sizes[shoe.size][shoe.type]++;
           }
        }
        else
        {
            sizes[shoe.size] = [];
            sizes[shoe.size][shoe.type] = 1;
        }
    }

    return result;
  }

  const shoes = [
    { type: 'I', size: 38 },
    { type: 'R', size: 38 },
    { type: 'R', size: 42 },
    { type: 'I', size: 41 },
    { type: 'I', size: 42 }
  ]

  console.log(organizeShoes(shoes))
// [38, 42]

const shoes2 = [
    { type: 'I', size: 38 },
    { type: 'R', size: 38 },
    { type: 'I', size: 38 },
    { type: 'I', size: 38 },
    { type: 'R', size: 38 }
  ]
  console.log(organizeShoes(shoes2))
  // [38, 38]

const shoes3 = [
    { type: 'I', size: 38 },
    { type: 'R', size: 36 },
    { type: 'R', size: 42 },
    { type: 'I', size: 41 },
    { type: 'I', size: 43 }
  ]
  
 console.log(organizeShoes(shoes3));
  // []


  const shoes4 = [
    { type: 'I', size: 38 },
    { type: 'I', size: 38 },
    { type: 'R', size: 42 },
    { type: 'R', size: 42 },
    { type: 'R', size: 38 },
    { type: 'R', size: 38 }
  ]
  
 console.log(organizeShoes(shoes4));