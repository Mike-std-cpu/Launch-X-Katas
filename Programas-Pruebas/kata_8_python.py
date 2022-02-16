"""
Kata 8 informacion de prueba
"""

# Diccionarios o Clases
planet = {
    'name': 'Earth', # Atributos
    'moons': 1
}
print(planet.get('name')) # Get sirve para acceder al valor del diccionario
# ------
print(planet['name']) # planet['name'] es idéntico a usar planet.get('name')

"""
A diferencia de get, los corchetes al no encontrar algun atributo del metodo, entraremos a un key error como en el
siguiente ejemplo:

                wibble = planet.get('wibble') # Regresa None
                wibble = planet['wibble'] # Arroja un KeyError
"""

# ------ UPDATE
planet.update({'name': 'Makemake'}) # name ahora es Makemake
# ------ Update con {}
planet['name'] = 'Makemake' #Es la misma accion pero con el operador de asignacion ' = '

"""
Es clave mencionar que con {} se necesita hacer varias llamadas para la update, mientra que con update solo es una:

                    planet.update({
                        'name': 'Jupiter',
                        'moons': 79
                    }) # Usando update

# ------------------

                planet['name'] = 'Jupiter'# Usando corchetes llamada 1
                planet['moons'] = 79 # Usando corchetes llamada 2
"""

# ------ INSERT
planet['orbital period'] = 4333 # Se insertara el atributo

"""El diccionario planet ahora contiene: {
      name: 'jupiter'
      moons: 79
      orbital period: 4333
 }
"""


# ------ DELETE

planet.pop('orbital period')

"""
    El diccionario planet ahora contiene: {
   name: 'jupiter'
   moons: 79
"""

# ----- DICCIONARIOS DENTRO DE DICCIOARIOS

# Añadimos los datos
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

"""
El diccionario planet ahora contiene: {
   name: 'Jupiter'
   moons: 79
   diameter (km): {
      polar: 133709
      equatorial: 142984
   }
 }
"""

# ---- Keys()


# Imagina que tiene el siguiente diccionario, en el que se almacenan los últimos tres meses de precipitaciones (rainfall).

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

"""
Imagina que quiere mostrar la lista de todas las precipitaciones. Puedes escribir el nombre de cada mes, pero sería 
tedioso, en este caso hacemos uso del método keys().
Salida:
 october: 3.5cm
 november: 4.2cm
 december: 2.1cm
"""

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

"""
Si se desea agregar un valor a diciembre o crear uno si no existe, puede ser la siguiente solucion:
"""

# El valor de december: 2.1cm
if 'december' in rainfall: # Si, 'december' existe en rainfall
    # rainfall [en la posición december] = rainfall [en la posición december] + 1 (2.1+1)
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1 # rainfall [en la posición december] es igual a 1

# Como december si existe, el valor será 3.1




# RECUPERACION DE VALORES DE UN DICCIONARIO


total_rainfall = 0 #Se incializa con 0

for value in rainfall.values():# Para cada valor en los valores de rainfall

    #El total de las precipitaciones será igual a ese mismo + el valor que se está iterando
    total_rainfall = total_rainfall + value # Suma el contenido de las cantidades

print(f'There was {total_rainfall}cm in the last quarter')

# Salida:
# There was 10.8cm in the last quarter
