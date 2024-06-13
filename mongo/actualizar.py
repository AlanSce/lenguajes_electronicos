#!/usr/bin/python3

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017") # Conexión a mongo
db = client["madero"] # Nombre de la base de datos
coll = db["clases"] # Nombre de la colección (tabla)

materias = [{'Materia': 'Montaje', 'dia': 'Viernes', 'horario_inicio': '09:50', 'duracion': '4', 'docente': 'Barbato Gustavo'},
           {'Materia': 'Lenguajes Electronicos', 'dia': 'Jueves', 'horario_inicio': '07:35', 'duracion': '2', 'docente': 'Scelza Alan'}, 
           {'Materia': 'Ingles', 'dia': 'Jueves', 'horario_inicio': '9:50', 'duracion': '1', 'docente': 'Rizzo Bruno'}
        ]

# Analizar la variable ---
#print(f"Variable materias: {materias}")
#print(f"--- es del tipo: {type(materias)}")

# Al ser una lista, puedo recorrer cada materia (diccionario) con un for:
#for m in materias:
#    print(m)

# También puedo imprimir un campo específico:
#for m in materias:
#    print(m['duracion'])

# Sabiendo esto, podemos agregar a la base de datos cada materia como un item:

i=0 # Esta variable me va a ayudar a que cada materia tenga un _id único
for m in materias:
    coll.update_one({"_id": i}, { "$set": m } , upsert=True ) #Upsert en True -> Si no existe la crea, si existe la actualiza
    i+=1


# Puedo consultar el estado de la base de la siguiente manera
# A la colección le hacemos un find(). Es importante convertirlo en una lista, si no, no será legible al print.
print(list(coll.find()))


# Teniendo estos conceptos claros, podemos armar unas funciones que sean más amigables

# Ver actualizar-2.py
