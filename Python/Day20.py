"""
Santa Claus 🎅 está revisando la lista de regalos que debe entregar esta Navidad. Sin embargo, algunos regalos faltan, otros están duplicados, y algunos tienen cantidades incorrectas. Necesita tu ayuda para resolver el problema.

Recibirás dos arrays:

received: Lista con los regalos que Santa tiene actualmente.
expected: Lista con los regalos que Santa debería tener.
Tu tarea es escribir una función que, dado received y expected, devuelva un objeto con dos propiedades:

missing: Un objeto donde las claves son los nombres de los regalos faltantes y los valores son las cantidades que faltan.
extra: Un objeto donde las claves son los nombres de los regalos extra o duplicados y los valores son las cantidades que sobran.
Ten en cuenta que:

Los regalos pueden repetirse en ambas listas.
Las listas de regalos están desordenadas.
Si no hay regalos que falten o sobren, las propiedades correspondientes (missing o extra) deben ser objetos vacíos.
"""

def fix_gift_list(received: list[str], expected: list[str]) -> dict[str, int]:
    result = {
        "missing": {},
        "extra": {}
    }

    for i in range(len(expected)):
        gift = expected[i]
       

        if gift in received:
            index = received.index(gift)
            received[index] = None
            expected[i] = None
        else:
            if not gift in result["missing"]:
                result["missing"][gift] = 1
            else:           
                result["missing"][gift] +=1
            

    for gift in received:
        if gift == None : continue
       
        if not gift in expected:            
            if not gift in result["extra"]:
                result["extra"][gift] = 1
            else:
                result["extra"][gift]+=1

    return result

print(fix_gift_list(
  ['puzzle', 'car', 'doll', 'car'], ['car', 'puzzle', 'doll', 'ball']
))

print(fix_gift_list(
   ['book', 'train', 'kite', 'train'],
  ['train', 'book', 'kite', 'ball', 'kite']
))