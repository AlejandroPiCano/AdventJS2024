#Los elfos 🧝🧝‍♂️ de Santa Claus han encontrado un montón de botas mágicas desordenadas en el taller. Cada bota se describe por dos valores:
#type indica si es una bota izquierda (I) o derecha (R).
#size indica el tamaño de la bota.
#Tu tarea es ayudar a los elfos a emparejar todas las botas del mismo tamaño que tengan izquierda y derecha. Para ello, debes devolver una lista con los pares disponibles después de emparejar las botas.
#¡Ten en cuenta que puedes tener más de una zapatilla emparejada del mismo tamaño!
def organizeShoes(shoes):
    result = []
    sizes = {}

    for shoe in shoes:
        size = sizes.get(shoe["size"])  # Usamos .get para manejar claves inexistentes

        if size is not None:
            if size.get("R" if shoe["type"] == "I" else "I", 0) > 0:
                result.append(shoe["size"])
                size["R" if shoe["type"] == "I" else "I"] -= 1
            else:
                size[shoe["type"]] = size.get(shoe["type"], 0) + 1
        else:
            sizes[shoe["size"]] = {"I": 0, "R": 0}
            sizes[shoe["size"]][shoe["type"]] = 1

    return result



shoes = [
    {"type": "I", "size": 38},
    {"type": "R", "size": 38},
    {"type": "R", "size": 42},
    {"type": "I", "size": 41},
    {"type": "I", "size": 42}
]


print(organizeShoes(shoes))