pisos= 29
#dir  'up' 'down'


dir_up = 'subiendo'
dir_down= 'bajando'


ingresados = {}
#actual
#siguiente
#ingresado

#cuando está en el piso del arreglo, 
#busca en el map, busca el valor y lo agrega al arreglo

def controlador(arr, ini, map ):
    print('Elevador en piso: ', ini)
    #for i in range(0, pisos):
    i=0
    #arr_ord = arr.sort( reverse=False)
    while len(arr)>0 :
        print('i=',i)
        arr_ord = arr.copy()
        if len(arr_ord) >0:
            arr_ord.sort( reverse=False)
            
        
        actual=arr_ord[0]

        act = arr[0]
        sig = arr_ord[1]
        if actual < sig:
            print('Elevador ', dir_up)
        else:
            print('Elevador ', dir_down)
        
        print('Elevador en piso ', actual)


        arr.remove(actual)
        #arr_ord.pop(0)
        

        print(f'Elevador se detiene -> {arr}')
        ingresado= map.get(actual)
        
        #buscar si el piso ya fue solicitado
        if ingresado not in arr:
            arr.append(ingresado)

        print(f'piso ingresado { ingresado } -> {arr}')
        #print('Elevador ', dir)
        i+=1
        #if i > len(arr_ord):
        #    i=0
        


arreglo= [5, 29, 13 ,10]
mapa = {5:2, 29:10, 13:1, 10:1}
inicio = 4

#controlador(arreglo, inicio, mapa)

def control(arr, ini, map):
    subiendo = True
    print('Elevador en piso: ', ini)
    for x in range(len(arr)):
        if subiendo :
            print('Elevador subiendo')
            for i in range(0, 30):
                if i in arr:
                    arr.remove(i)
                    
                    print('Elevador en piso ', i)
                    print(f'Elevador se detiene -> {arr}')

                    ingresado= map.get(i)

                    if ingresado not in arr:
                        arr.append(ingresado)
                    
                    print(f'piso ingresado { ingresado } -> {arr}')
            subiendo= False

        if not subiendo:
            print('Elevador descendiendo')

            #cprint('aaa')
            for i in reversed(range(0, 30)):
                #print('eee')
                if i in arr:
                    arr.remove(i)
                    
                    print('Elevador en piso ', i)
                    print(f'Elevador se detiene -> {arr}')

                    ingresado= map.get(i)

                    if ingresado not in arr:
                        arr.append(ingresado)
                    
                    print(f'piso ingresado { ingresado } -> {arr}')




                

                 

control(arreglo, inicio, mapa)
    

