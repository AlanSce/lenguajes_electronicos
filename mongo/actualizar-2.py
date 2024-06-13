#!/usr/bin/python3

import pymongo
from base import Storage

uri = "mongodb://localhost:27017/"
db = "madero"
coll = "clases"

storage = Storage(uri, db, coll)

materias = [{'Materia': 'Montaje', 'dia': 'Viernes', 'horario_inicio': '09:50', 'duracion': '4', 'docente': 'Gustavo Barbato'},
           {'Materia': 'Lenguajes Electronicos', 'dia': 'Jueves', 'horario_inicio': '07:35', 'duracion': '2', 'docente': 'Alan Scelza'}, 
           {'Materia': 'Ingles', 'dia': 'Jueves', 'horario_inicio': '9:50', 'duracion': '1', 'docente': 'Bruno Rizzo'}
        ]

# Mostrar el estado de la base antes del cambio
print(storage.find())


print("--------")
# Actualizar
i = 0
for m in materias:
    storage.update(i, m)
    i+=1
print("--------")

# Mostrar nuevamente
print(storage.find())
