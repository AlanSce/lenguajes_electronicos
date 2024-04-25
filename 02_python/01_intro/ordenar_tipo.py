import csv

tipos_arboles = {}

# Leer el archivo
with open('arbolado-en-espacios-verdes.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	next(spamreader)
	for row in spamreader:
		tipo_arbol = row[7]
		if tipo_arbol in tipos_arboles: # Ya lo tengo, le sumo uno
			tipos_arboles[tipo_arbol] += 1
		else: # Es el primer arbol que leo
			tipos_arboles[tipo_arbol] = 1

# Imprimo el diccionario hasta el momento
print(tipos_arboles)

# Ordeno
tipos_arboles_ordenados = {k: v for k, v in sorted(tipos_arboles.items(), key=lambda item: item[1], reverse=True)}


# Armo la tabla ordenada
for arbol in tipos_arboles_ordenados:
	# Noten que la f permite agregar variables entre llaves en los prints
	print(f'{tipos_arboles_ordenados[arbol]}  | {arbol}')
