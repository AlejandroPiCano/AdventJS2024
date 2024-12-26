/**
 * @param {{ name: string, quantity: number, category: string }[]} inventory
 * @returns {object} The organized inventory
 */
function organizeInventory(inventory) {
    if(inventory.length == 0)
     return {};

    let result = {};

    for(let i = 0; i < inventory.length; i++){
       let category = inventory[i].category;
       let name = inventory[i].name;
       let quantity = inventory[i].quantity;
    
         if(!result[category]){
             result[category] = {};
         }
      
        result[category][name] = (!result[category][name]) ? quantity : result[category][name] + quantity;        
    }

    return result;
  }

  const inventory = [
    { name: 'doll', quantity: 5, category: 'toys' },
    { name: 'car', quantity: 3, category: 'toys' },
    { name: 'ball', quantity: 2, category: 'sports' },
    { name: 'car', quantity: 2, category: 'toys' },
    { name: 'racket', quantity: 4, category: 'sports' }
  ]
  
  console.log(organizeInventory(inventory));

  
const inventory2 = [
    { name: 'book', quantity: 10, category: 'education' },
    { name: 'book', quantity: 5, category: 'education' },
    { name: 'paint', quantity: 3, category: 'art' }
  ]
  
 console.log(organizeInventory(inventory2));
  
  // Resultado esperado:
  // {
  //   education: {
  //     book: 15
  //   },
  //   art: {
  //     paint: 3
  //   }
  // }