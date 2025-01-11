import re

"""
Santa Claus tiene una agenda mágica 📇 donde guarda las direcciones de los niños para entregar los regalos. El problema: la información de la agenda está mezclada y malformateada. Las líneas contienen un número de teléfono mágico, el nombre de un niño y su dirección, pero todo está rodeado de caracteres extraños.

Santa necesita tu ayuda para encontrar información específica de la agenda. Escribe una función que, dado el contenido de la agenda y un número de teléfono, devuelva el nombre del niño y su dirección.

Ten en cuenta que en la agenda:

Los números de teléfono están formateados como +X-YYY-YYY-YYY (donde X es uno o dos dígitos, e Y es un dígito).
El nombre de cada niño está siempre entre < y >
La idea es que escribas una funcióna que, pasándole el teléfono completo o una parte, devuelva el nombre y dirección del niño. Si no encuentra nada o hay más de un resultado, debes devolver null.
"""
def find_in_agenda(agenda, phone):
    index = agenda.find(phone)
    if index == -1:
        return None

    index2 = agenda.find(phone, index + 1)
    if index2 != -1:
        return None

    regex_phones = re.compile(r"\+\d{1,3}-\d{3}-\d{3}-\d{2,3}")
    phones = regex_phones.findall(agenda)
    print(phones)

    regex_names = re.compile(r"<([^>]+)>")
    names = [match.group(1) for match in regex_names.finditer(agenda)]
    print(names)

    for name in names:
        agenda = agenda.replace(name, "")
    for phone_number in phones:
        agenda = agenda.replace(phone_number, "")

    addresses = []
    addresses_split = agenda.split("<>")

    for address in addresses_split:
        cleaned_address = address.replace("\n", "").strip()
        if cleaned_address:
            addresses.append(cleaned_address)
    print(addresses)

    for i, p in enumerate(phones):
        if phone in p:
            index = i

    return {
        "name": names[index],
        "address": addresses[index]
    }

agenda = f'+34-600-123-456 Calle Gran Via 12 <Juan Perez>
Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654
<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York'


print(find_in_agenda(agenda, '34-600-123-456'))