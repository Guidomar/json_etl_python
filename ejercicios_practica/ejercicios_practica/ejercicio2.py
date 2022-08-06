# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt



    
    # Ejercicio de consumo de datos por API
url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    #1 - Traemos los datos de la url y guardamos en una variable la información
    #    recopilada en formato json como un diccionario:
def extract (url):
        response = requests.get(url)
        data = response.json()

        #filtramos sólo los usuarios por cada vez que completaron la lectura
        data_filtrada = [{"userId": x["userId"], "completo": x["completed"]} for x in data if x["completed"]== True]

        return data_filtrada

def transform(data_filtrada):
            
        d=[] # Lista de cada userId que complet{o} un libro

        x = []
        y = []
        for i in range(len(data_filtrada)):
            variable = data_filtrada[i]
            userId = variable['userId']
       
            d.append(userId)
                
        print(d)
       
        
        repeticiones = dict((i, d.count(i)) for i in d)
        print(repeticiones)
                
        for k,v in repeticiones.items():
        
            x.append(k)
            y.append(v)
        return x,y
            
def load (x,y):
    
        fig = plt.figure()
        fig.suptitle("Comparativa de usuarios que completaron libros", fontsize=16, label="cantidad de títulos completados") 
        ax = fig.add_subplot()
        ax.bar(x,y)
        ax.set_facecolor('whitesmoke')
        ax.set_ylabel('libros completados')
        ax.set_xlabel('UserId')
        plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    data_set = extract (url)
    data = transform(data_set)
    
    x, y = transform(data_set)  

    load (x,y)

print("terminamos")