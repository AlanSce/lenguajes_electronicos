#!/usr/bin/python3

import pymongo
from base import Storage

uri = "mongodb://localhost:27017/"
db = "madero"
coll = "clases"

storage = Storage(uri, db, coll)


# Traer toda la info a una variable
materias = storage.find()

print(materias)
#------

print("---------")

# Buscar un atributo específico, por ejemplo materias que duren 2 horas

print(storage.find_one({'duracion': '2'}))
