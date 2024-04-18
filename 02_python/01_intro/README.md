# Intro

Para entrar en calor con Python, realizar la siguiente ejercitación.

Guardar todos los códigos correspondientes en una carpeta llamada ejercitacion_3 dentro de su repositorio, y enviar el link al mail del docente en el plazo de tiempo indicado.

## Ejercicios.

Descargar el archivo csv de [Arbolado en espacios verders](https://data.buenosaires.gob.ar/dataset/arbolado-espacios-verdes) del gobierno de la ciudad. 

En un nuevo archivo .csv, copiar solo las primeras 100 líneas (aparte de los headers). 

El programa al comenzar debe abrir el archivo en modo de lectura, referencia: [csv](https://docs.python.org/es/3/library/csv.html)

Crear los siguientes códigos:

1. ordenar_tipo.py:

El código debe imprimir la siguiente tabla:
```
<cantidad de árboles> | <tipo de árbol>
<cantidad de árboles> | <tipo de árbol>
```
El tipo de árbol lo vamos a tomar de la columna `nombre_com`.

La tabla debe estar ordenada de mayor a menor según las cantidades.

2. promedio_diametro.py

Mostrarle un menú al usuario con las ubicaciones disponibles de los árboles, y permitirle al usuario [ingresar un número](https://stackoverflow.com/a/26692765)(Ver ejemplo) para elegir una ubicación.

Al recibir la ubicación, debe devolver el promedio del diametro de todos los árboles de la ubicación indicada.

Cargar los ejercicios en su repo y enviar un mail al docente con el link correspondiente.

3) Ubicar en mapa (OPCIONAL)

Vayamos un paso más, dado que pudimos ordenar los árboles por cantidad gracias al código ordenar_tipo, realizar un código `ubicar_unicos.py` que devuelva un link de google maps para hacerle clic y que nos lleve a la ubicación de los árboles que solo haya 1. 

Tips:
- Usar los datos latitud y longitud del csv
- Para generar un link de maps por coordenadas, debe tener el siguiente formato: https://www.google.com/maps?q={latitud},{longitud} 

Ejemplo para el primer árbol del archivo: https://www.google.com/maps?q=-34.6450145297,-58.4775636069

La salida del código debe ser una tabla que muestre:

Nombre | Ubicación
<arbol 1> | <link 1>
<arbol 2> | <link 2>
<arbol 3> | <link 3>




