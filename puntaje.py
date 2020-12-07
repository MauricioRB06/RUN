puntajes = open('puntajes.txt','r')
lista2=[]

with open('puntajes.txt','r') as puntajes: 
    lista = [puntaje.strip() for puntaje in puntajes]

for i in range(0,len(lista)):
    lista2.append(int(lista[i]))

orden=sorted(lista2)

with open('puntajes.txt', 'w') as puntajes:
    for linea in range(0, len(orden)):
        puntajes.write("%s \n"% (orden[linea]))




    