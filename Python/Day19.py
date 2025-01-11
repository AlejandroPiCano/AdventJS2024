"""
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
"""
def distribute_weight(weight):
    def paint_boxes(boxes):
        rep = {
            1: [" _ ", "|_|"],
            2: [" ___ ", "|___|"],
            5: [" _____ ", "|     |", "|_____|"],
            10: [" _________ ", "|         |", "|_________|"]
        }
        
        result = ''
        before = ''
        
        for i in range(len(boxes)):
            box = boxes[i]
            
            if before:
                result += before.ljust(len(rep[box][0]) - 1, "_") + "\n"
            
            for j, b in enumerate(rep[box]):
                if (not before or j > 0) and j < len(rep[box]) - 1:
                    result += b + "\n"
            
            before = rep[box][-1]
            
            if i == len(boxes) - 1:
                result += before
        
        return result
    
    weights = [1, 2, 5, 10]
    boxes = []
    
    for w in reversed(weights):
        while weight - w >= 0:
            weight -= w
            boxes.insert(0, w)
    
    result = paint_boxes(boxes)
    return result

# Ejemplo de uso
"""output = distribute_weight(28)
print(output)"""
