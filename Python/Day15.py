"""
Al Polo Norte ha llegado ChatGPT y el elfo Sam Elfman está trabajando en una aplicación de administración de regalos y niños.

Para mejorar la presentación, quiere crear una función drawTable que reciba un array de objetos y lo convierta en una tabla de texto.

La tabla dibujada debe representar los datos del objeto de la siguiente manera:

Tiene una cabecera con el nombre de la columna.
El nombre de la columna pone la primera letra en mayúscula.
Cada fila debe contener los valores de los objetos en el orden correspondiente.
Cada valor debe estar alineado a la izquierda.
Los campos dejan siempre un espacio a la izquierda.
Los campos dejan a la derecha el espacio necesario para alinear la caja.
"""
def draw_table(data):
    if not data or len(data) == 0:
        return ''

    result = ''
    
    # Calculate column lengths
    column_lengths = [
        max(len(str(row[key])) for row in data) 
        for key in data[0].keys()
    ]

    # Create the top border
    border = '+' + '+'.join('-' * (length + 2) for length in column_lengths) + '+'
    result += border + '\n'

    # Add the header row
    header = '| ' + ' | '.join(
        key.capitalize().ljust(length) for key, length in zip(data[0].keys(), column_lengths)
    ) + ' |'
    result += header + '\n'

    # Add the border under the header
    result += border + '\n'

    # Add the data rows
    for row in data:
        row_content = '| ' + ' | '.join(
            str(value).ljust(length) for value, length in zip(row.values(), column_lengths)
        ) + ' |'
        result += row_content + '\n'

    # Add the bottom border
    result += border

    return result



print(draw_table([
    { 'name': 'Alice', 'city': 'London' },
    { 'name': 'Bob', 'city': 'Paris' },
    { 'name': 'Charlie', 'city': 'New York' }
  ]));