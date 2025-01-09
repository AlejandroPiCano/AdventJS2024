"""
¡Santa Claus ya ha repartido todos los regalos! Ahora está revisando los informes de productividad de los elfos. Pero hay un problema: la Product Owner, Mrs. Claus 🧑‍🎄✨, necesita entender rápidamente si los elfos cumplieron con los tiempos estimados. Están haciendo Agile Scream.

Para ayudar a Mrs. Claus, tu tarea es calcular el porcentaje completado de cada tarea y devolverlo redondeado al número entero más cercano. Esto le permitirá planificar mejor para la próxima Navidad y mantener a todos contentos.

Esta es la función que espera:

getCompleted('01:00:00', '03:00:00') // 33%
getCompleted('02:00:00', '04:00:00') // 50%
getCompleted('01:00:00', '01:00:00') // 100%
getCompleted('00:10:00', '01:00:00') // 17%
getCompleted('01:10:10', '03:30:30') // 33%
getCompleted('03:30:30', '05:50:50') // 60%
"""
def get_completed(time_worked: str, total_time: str) -> str:
  def convert_to_seconds(time):
    return sum(int(v) * (60**(2-i)) for i,v in enumerate(time.split(":")))
  
  workedSeconds = convert_to_seconds(time_worked)
  totalSeconds = convert_to_seconds(total_time)
  completionPercentage = (workedSeconds / totalSeconds) * 100

  return f'{round(completionPercentage)}%'

print(get_completed('01:00:00', '03:00:00'))