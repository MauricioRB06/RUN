from io import open
import operator


# aca deberia ir el diccionario con las variables nombres y score, el nombre como clave y score como valor, cada vez que termina una partida se agrega al diccionario
def save_game(name,score):
	clients[str(name)] = score

def order():

	# aca se ordena el diccionario por valor de mayor a menor
	clients_sort = sorted(clients.items(), key=operator.itemgetter(1), reverse=True)
	

	# creamos el archivo
	client_archivo= open("High_Scores.txt",'a')
	# pasamos el diccionario al archivo con el orden que queriamos
	with open('High_Scores.txt', 'a') as client_archivo:
		for nombre, valor in sorted(clients.items(), key=operator.itemgetter(1), reverse=True):
			client_archivo.write("%s %s \n" %(nombre,valor))

def hsco():
	# aca leemos el archivo linea por linea una sola vez por eso el for para que se repita, readline lee una linea cada vez y pasa a la otra
	f = open("High_Scores.txt", "r")
	a = f.readline()
	b = f.readline()
	c = f.readline()
	f.close()
	return a.strip(),b.strip(),c.strip()

#name = input()
#score = int(input())
#save_game(name,score)
order()
a,b,c = hsco()
print(a)
print(b)
print(c)