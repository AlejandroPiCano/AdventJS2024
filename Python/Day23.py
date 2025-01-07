"""
Los elfos están trabajando en un sistema para verificar las listas de regalos de los niños 👧👦. Sin embargo, ¡algunas listas están incompletas y faltan números!

Tu tarea es escribir una función que, dado un array de números, encuentre todos los números que faltan entre 1 y n (donde n es el tamaño del array o el número más alto del array).

Eso sí, ten en cuenta que:

Los números pueden aparecer más de una vez y otros pueden faltar
El array siempre contiene números enteros positivos
Siempre se empieza a contar desde el 1
"""
def find_missing_numbers(nums):
    result = []
    max = sorted(nums, reverse=True)[0]
  
    for i in range(1,max):
        if not i in nums:
            result.append(i)        
    return result

print(find_missing_numbers([1, 2, 4, 6]))
print(find_missing_numbers([4, 8, 7, 2]))