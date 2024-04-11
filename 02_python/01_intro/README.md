# Intro

Para entrar en calor con Python, realizar la siguiente ejercitación.

Guardar todos los códigos correspondientes en una carpeta llamada ejercitacion_3 dentro de su repositorio, y enviar el link al mail del docente en el plazo de tiempo indicado.

## Ejercicios.

Descargar el archivo csv de [Arbolado en espacios verders](https://data.buenosaires.gob.ar/dataset/arbolado-espacios-verdes) del gobierno de la ciudad. 

En un nuevo archivo .csv, copiar solo las primeras 100 líneas (aparte de los headers). 

El programa al comenzar debe abrir el archivo en modo de lectura, referencia: [csv](https://docs.python.org/es/3/library/csv.html)

Crear los siguientes códigos:

1. ordenar_tipo.py:

Debe contener una función llamada `ordenar_por_tipo` que acepte un parámetro `data`.

ordenar_por_tipo(data): Esta función acepta como parámetro una variable `data` que debe contener la información necesaria del csv que crean correspondiente. Al llamarla, debe imprimir en pantalla una tabla con el siguiente formato:
```
<cantidad> | <tipo de árbol>
<cantidad> | <tipo de árbol>
```
El tipo de árbol lo vamos a tomar de la columna `nombre_com`.

La tabla debe estar ordenada de mayor a menor según las cantidades.

2. promedio_diametro.py

Mostrarle un menú al usuario con las ubicaciones disponibles de los árboles, y permitirle al usuario [ingresar un número](https://stackoverflow.com/a/26692765)(Ver ejemplo) para elegir una ubicación.

Al recibir la ubicación, llamar a la función `promedio_diametro`. Debe aceptar dos argumentos, `data` y `ubicacion`.

promedio_diametro(data, ubicacion): Debe devolver el promedio del díametro de todos los árboles de la ubicación indicada.

Cargar los ejercicios en su repo y enviar un mail al docente con el link correspondiente.




