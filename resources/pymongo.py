
# Una variable sola
materia = {'Materia': 'Montaje', 'dia': 'viernes', 'horario_inicio': '09:50_12:00', 'duracion': '4 horas', 'docente': 'Barbato Gustavo'}

# Actualizar en mongo
mycol.update_one({"_id": "materias"}, { "$set": materia } , upsert=True )

## Salida
UpdateResult({'n': 1, 'nModified': 0, 'ok': 1.0, 'updatedExisting': True}, acknowledged=True)

# Listar
list(mycol.find())

## Salida
[{'_id': 'materias', 'Materia': 'Montaje', 'dia': 'viernes', 'docente': 'Barbato Gustavo', 'duracion': '4 horas', 'horario_inicio': '09:50_12:00'}]


# Problema

Si hacemos un for que itere todas las materias y haga el update, se guarda solo la última... habría que ponerle un id a cada materia...
