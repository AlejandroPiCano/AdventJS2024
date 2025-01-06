/*
El Grinch ha estado haciendo de las suyas en el Polo Norte y ha sembrado bombas de carbón explosivo 💣 en la fábrica de juguetes de los duendes. Quiere que todos los juguetes queden inutilizados y por eso ha dejado una cuadrícula donde algunas celdas tienen carbón explosivo (true) y otras están vacías (false).

Los duendes necesitan tu ayuda para mapear las zonas peligrosas. Cada celda vacía debe mostrar un número que indique cuántas bombas de carbón explosivo hay en las posiciones adyacentes, incluidas las diagonales.
 */
function detectBombs(grid) {
    let result = [];
    let values = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]];

    for(let i=0;i<grid.length;i++){ 
        result.push([]);
        for(let j=0;j<grid[i].length;j++){ 
            let count = 0;
            
            for(let value of values){
                let x = i + value[0];
                let y = j + value[1];
                if(x >= 0 && x < grid.length && y >= 0 && y < grid[i].length)
                    if(grid[x][y])
                        count++;
            }      
            result[i].push(count);
        }
    }
    return result;
  }

 console.log( detectBombs([
    [true, false, false],
    [false, true, false],
    [false, false, false]
  ]));
  // [
  //   [1, 2, 1],
  //   [2, 1, 1],
  //   [1, 1, 1]
  // ]
  
  console.log( detectBombs([
    [true, false],
    [false, false]
  ]));
  // [
  //   [0, 1],
  //   [1, 1]
  // ]
  
  console.log( 
    detectBombs([
    [true, true],
    [false, false],
    [true, true]
  ]));
  
  // [
  //   [1, 1],
  //   [4, 4],
  //   [1, 1]
  // ]