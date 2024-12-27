function createXmasTree(height, ornament) {
  let result = '';
  for (let i = 1; i <= height; i++) {    
    let spaces = '_'.repeat(height-i);
    result +=  (spaces + ornament.repeat(2*i-1) + spaces + '\n');
  }
  result += ('_'.repeat(height-1) + '#' + '_'.repeat(height-1) + '\n');
  result += ('_'.repeat(height-1) + '#' + '_'.repeat(height-1));

  return result;
}

const tree = createXmasTree(5, '*')
console.log(tree)
/*
____*____
___***___
__*****__
_*******_
*********
____#____
____#____
*/

const tree2 = createXmasTree(3, '+')
console.log(tree2)
/*
__+__
_+++_
+++++
__#__
__#__
*/

const tree3 = createXmasTree(6, '@')
console.log(tree3)
/*
_____@_____
____@@@____
___@@@@@___
__@@@@@@@__
_@@@@@@@@@_
@@@@@@@@@@@
_____#_____
_____#_____
*/