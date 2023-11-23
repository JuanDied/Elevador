inicio = 4  #piso en el que comienza
arreglo= [5, 29, 13 ,10]  #arreglo de los siguientes pisos
mapa = {5:2, 29:10, 13:1, 10:1}  #mapa de piso ingresado(valor), en el piso que se ingresa(llave)

#estado(i, arr, map, dir) sirve para imprimir el piso actual y el piso que ingresan que se ingresa
def estado(i, arr, map, dir):
    if i in arr:
        print('Elevador ', dir) #indicamos la dirección
        arr.remove(i)  #si ya llegamos al piso, se remueve del arreglo

        print('Elevador en piso ', i) #piso actual
        print(f'Elevador se detiene -> {arr}') # muestra los pisos faltantes

        ingresado= map.get(i) # buscamos en el mapa, en el piso actual, cuál piso se pide?

        if ingresado not in arr:  #si ya lo pidieron, no es necesario agregarlo
            arr.append(ingresado) # lo agregamos 

        print(f'piso ingresado { ingresado } -> {arr}')  #indicamos los pisos que siguen 



#método que recibe los parametros e imprime el estado del elevador.
def control(arr, ini, map):

    #se copia el prime arreglo de pisos solicitados, se ordena y se decide si se sube o desciende.
    arr_ord = arr.copy() #copia
    arr_ord.sort( reverse=False) #se ordena 

    if ini <= arr_ord[0]: #si el piso que sigue es arriba del inicial, subimos
        subiendo = True #definimos si el asecendor va subiendo o descendiendo
    else:
        subiendo=False #de lo contrario bajamos
    print('Elevador en piso: ', ini)
    for x in range(len(arr)):  #el loop funciona (elevador)si aún quedan pisos a donde ir
        if subiendo :
            dir= 'subiendo'
            for i in range(0, 30):
                
                estado(i, arr, map, dir) #usamos la funcion para imprimir estados

            subiendo= False

        if not subiendo:  #se repite lo mismo pero bajando
            dir= 'descendiendo'
            for i in reversed(range(0, 30)):
                
                estado(i, arr, map, dir)





           

                 

control(arreglo, inicio, mapa)
    

