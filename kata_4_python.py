#---------------------MULTILINEA--------------------------------------------------------
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

#SALIDA:
'''Facts about the Moon:
 There is no atmosphere.
 There is no sound.'''

multilines = """Facts about the Moon:
#...  There is no atmosphere.
#...  There is no sound."""
print(multilines)
#SALIDA:
'''Facts about the Moon:
There is no atmosphere.
There is no sound'''

#------------------ METODOS STRING ---------------------------------------------------

from argparse import RawDescriptionHelpFormatter


temperatures = '''Daylight: 260 F
... Nighttime: -280 F'''
print(temperatures.split())

#---.found()---
temperaturess = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
print(temperaturess.find('Mars')) # Imprimira el numero de la posicion: 68
#---.count()---
print(temperaturess.count('Mars')) #Imprimira las veces que aparece la palabra mars: 1
print(temperaturess.count('Celsius')) #Imprimira las veces que aparece la palabra mars: 2
#--.lower() & .upper()---
trys = "Este Es Un Ejemplo de LeTrAs RandomM" #Convierte toda la cadena a minusculas
print(trys.lower())
print(trys.upper())

temper = 'Mars Average Temperature: -60 C'
print(temper)
parts = temper.split(':')
print(parts)

#---.isnumeric()---
mars_temper = 'The highest temperature on Mars is about 30 C'
for item in mars_temper.split():
    if item.isnumeric():# SI es numerico imprimelo y el CILCO FOR para recorerr toda la oracion
        print(item)
#En este caso no sirve con numero -NEG

#---.starswitch() & .endswitch() -----
star = '-60'
star.startswith('-') #Resultado: TRUE, ya que comienza con '-'

if "30 C".endswith("C"):
    print("This temperature is in Celsius") #Entrara a la condicion puesto que si TERMINA con C, en otro caos mandaria false

'''--- .replace() ---
    Hasta ahora, hemos visto cadenas que pueden usar C para Celsius y F para Fahrenheit. 
    Puedes utilizarel método .replace() para buscar y reemplazar apariciones de un carácter o grupo de caracteres:
'''
text = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."
print(text.replace('Celsius', 'C'))#Cambia los parametros que se indicadron

#---.join() & .split()---
moon_facts = ['The Moon is drifting away from the Earth.', 'On average, the Moon is moving about 4cm every year']
'\n'.join(moon_facts) #Une las dos cadenas del arreglo



