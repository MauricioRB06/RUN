import io
from io import open
import operator

# aca deberia ir el diccionario con las variables nombres y score, el nombre como clave y score como valor, cada vez que termina una partida se agrega al diccionario
clients = {'Aldrich': 1.97,
           'Enrico': 8.49,
           'Christoper': 9.79,
           'Cherice': 8.53,
           'Margi': 0.43,
		   'Manco el que lo lea':99999,
		   'juan':4654,
		   'sfsa':46,
		   'asdfsa':465
		   }

# aca se ordena el diccionario por valor de mayor a menor
clients_sort = sorted(clients.items(), key=operator.itemgetter(1), reverse=True)

# aca se imprime el diccionario clave y valor uno por uno, esto no es necesario era para ver como se imprimia en consola
for name in enumerate(clients_sort):
    print(name[1][0], 'has spend', clients[name[1][0]])

# creamos el archivo
client_archivo= open("puntaje.txt",'a')
# pasamos el diccionario al archivo con el orden que queriamos
with open('puntaje.txt', 'a') as client_archivo:
	for nombre, valor in sorted(clients.items(), key=operator.itemgetter(1), reverse=True):
		client_archivo.write("%s %s \n" %(nombre,valor))

# aca leemos el archivo linea por linea una sola vez por eso el for para que se repita, readline lee una linea cada vez y pasa a la otra
f = open("puntaje.txt", "r")
for i in range(1,4):
	linea = f.readline()
	print(linea)
f.close()
