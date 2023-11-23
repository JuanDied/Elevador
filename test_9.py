inicio = 4  #piso en el que comienza
arreglo= [5, 29, 13 ,10]  #arreglo de los siguientes pisos
mapa = {5:2, 29:10, 13:1, 10:1}  #mapa de piso ingresado(valor), en el piso que se ingresa(llave)


def estado(i, arr, map, dir):
    if i in arr:
        print('Elevador ', dir)
        arr.remove(i)

        print('Elevador en piso ', i)
        print(f'Elevador se detiene -> {arr}')

        ingresado= map.get(i)

        if ingresado not in arr:
            arr.append(ingresado)

        print(f'piso ingresado { ingresado } -> {arr}')   



#método que recibe los parametros e imprime el estado del elevador.
def control(arr, ini, map):
    #se copia el prime arreglo de pisos solicitados, se ordena y se decide si se sube o desciende.
    arr_ord = arr.copy()
    arr_ord.sort( reverse=False)
    if ini <= arr_ord[0]:
        subiendo = True #definimos si el asecendor va subiendo o descendiendo
    else:
        subiendo=False
    print('Elevador en piso: ', ini)
    for x in range(len(arr)):  #el loop funciona (elevador)si aún quedan pisos a donde ir
        if subiendo :
            dir= 'subiendo'
            for i in range(0, 30):
                
                estado(i, arr, map, dir)

            subiendo= False

        if not subiendo:  #se repite lo mismo pero bajando
            dir= 'descendiendo'
            for i in reversed(range(0, 30)):
                
                estado(i, arr, map, dir)





           

                 

control(arreglo, inicio, mapa)
    

