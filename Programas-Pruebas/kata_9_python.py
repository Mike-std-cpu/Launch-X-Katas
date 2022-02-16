
# 1FUnciones
def rocket_parts(): # Defino mi función 
    print('payload, propellant, structure')

rocket_parts() #Mandamos a llamar la funcion, usando solo su nombre  y parenstesis.

# ----- 2OUTPUT
def rockets_parts():
    return 'payload, propellant, structure'

output = rockets_parts()
output
#--- 3Arguments
def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'

distance_from_earth('Moon') #Entra al if
distance_from_earth('Earth') #Entra al else
distance_from_earth() # Marca error

#--- 4MorE ARGUMENTS
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

days_to_complete(1000, 150)

#--- 5Functions and arguments
total_days = days_to_complete(238855,75) #Asiganmos el resultado a una variable
round(total_days) # Funcion de redondeo.
# Salida sin around: 132.69722222222222
# Salida con around: 133

#Se puede simplificar aun mas...
round(days_to_complete(238855,75))

# ---  6Argumentos de palbr clave
from datetime import timedelta, datetime # Librerias

def arrival_time(hours=51): # La variable horas tiene un valor de 51 que es el tiempo estimado que se hara para llegar la destino
    now = datetime.now() # Fecha actual
    arrival = now + timedelta(hours=hours) # Se suma la hora actual con el tiempo estimado para lleagar
    return arrival.strftime('Arrival: %A %H:%M') # Se determina el formato DIA/ HORA:MIN
arrival_time()

# ---  7Argumentos de palabra clave y agumentos
from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f'{destination} Arrival: %A %H:%M')
    #En este caso debemos ingresar forsosamente un argumento de destino, si no... marca error

# -----  8Argumentos de varibale
def variable_length(*args): # Puede rsivir cualquier numero como argumento
    print(args)
variable_length('one', 2, 'Three', 4)
#EJEMPLO
"""
Un cohete realiza varios pasos antes de un lanzamiento. En función de las tareas o retrasos, 
estos pasos pueden tardar más de lo previsto. Vamos a crear una función de longitud variable que pueda calcular 
cuántos minutos quedan hasta el inicio, dado el tiempo que va a tardar cada paso:
"""
def sequence_time(*args): #Puedes ingresar cualquier tipo de numero
    total_minutes = sum(args)#Sumara todos los argumentos
    if total_minutes < 60: #Si la suma es menor a 60, entra al if
        return f'Total time to launch is {total_minutes} minutes'
    else:#Si no...
        return f'Total time to launch is {total_minutes/60} hours'
#Probamos:
sequence_time(4,15,18)#if
#sequence_time(4,14,49) #Else

# ----- 9Argumentos de palabra clave variable
"""
EJEMPLO1: 
Para que una función acepte cualquier número de argumentos de palabra clave, debe usar una sintaxis similar. 
En este caso, se requiere un asterisco doble:
"""
def variable_length(**kwargs): # El doble *, acepta cualquier numero de argumentos
    print(kwargs)

variable_length(tanks = 1, day = 'Wednesday', pilots = 3)

"""
EJEMPLO 2:
En esta función, vamos a usar argumentos de palabra clave variable para notificar los astronautas asignados a 
la misión.Dado que esta función permite cualquier número de argumentos de palabra clave, 
se puede reutilizar independientemente del número de astronautas asignados:
"""
def crew_members(**kwargs):
    print(f'{len(kwargs)} astronauts assigned for this mission:')
    for title, name in kwargs.items():
        print(f'{title}: {name}')
        """
        Usamos len para contabilizar, el ciclo for para recorrer el contenido plasmando el nombre y su contenido para su 
        posterior impresion
        """

crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin', command_pilot='Michael Collins')
# No se pueden repetir argumentos, para evitar errores