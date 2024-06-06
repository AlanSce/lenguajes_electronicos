>>> arbol = { 'washington': 20 , 'fafa': 200 , 'jacaranda': 40 } 
>>> 
>>> 
>>> arbol
{'washington': 20, 'fafa': 200, 'jacaranda': 40}
>>> 
>>> menu = {}
>>> i = 0 
>>> 
>>> 
>>> for ar in arbol:
...   print(ar)
... 
washington
fafa
jacaranda
>>> for ar in arbol:
...   menu[i] = ar
...   i+=1
... 
>>> menu
{0: 'washington', 1: 'fafa', 2: 'jacaranda'}
>>> menu[1]
'fafa'

>>> arbol['fafa']
200

