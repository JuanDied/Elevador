arreglo= [5, 29, 13 ,10]
mapa = {5:2, 29:10, 13:1, 10:1}
inicio = 4

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
    

