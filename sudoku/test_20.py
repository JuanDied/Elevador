#Este problema se aborda usando Backtracking,
#que permite regresar y cambiar una descisión erronea
#es una forma más eficiente que un abordaje de fuerza bruta

N = 9 # tamaño de la matriz 9x9

#prueba si se puede asignar un numero en la celda, fila, columna y numero a probar
def comprobar(matriz, fila, col, num):
	
	#se comprueba la fila si ya está el número 
	for x in range(9):
		if matriz[fila][x] == num:
			return False

	#se comprueba la columna si ya está el número 
	for x in range(9):
		if matriz[x][col] == num:
			return False

	#se busca en la sub-matrix de 3x3 
	#por ejemplo si es la fila=5 -> (fila % 3) = 2
	#entonces la fila de la submatriz será 5-2 = 3
	#comenzara a buscar desde la fila 3 hasta la 5
	subfila = fila -(fila%3)
	subCol = col -(col%3)

	for i in range(3):
		for j in range(3):
			if matriz[i+subfila][j+subCol] == num:
				return False
	return True



def resolver(matriz, fila, col):

	#como las filas y colomnas van desde 0 hasta 8
	#se verifica si está en la fila 8 y si llegó a la columna 9.
	if (col == N and fila == N-1):
		return True
	

	#si ya se llegó a la columna 9, pasa a la siguiente fila y columna 0
	if col == N:
		fila += 1
		col = 0

	#se comprueba si ya hay un numero en la posición
	#  entonces se repite lo anterior de forma recursiva
	if matriz[fila][col] > 0:
		return resolver(matriz, fila, col+1) #se pasa de columna, hasta llegar a 9
	
	#se prueban los numeros del 1 hasta el 9
	for num in range(1, N+1):
	
		#se usa la funcion para comprobar si es valido 
		#si lo es entonces se asigna, 
		# y se continua en la siguiente columna, misma fila.
		if comprobar(matriz, fila, col, num):
		
			matriz[fila][col] = num

			#se llama la funcion de forma recursiva
			if resolver(matriz, fila, col+1):
				return True

		#ya que no fue valido el numero asignado, entonces se prueba otro
		#es necesario formatearlo a 0 para que se resuelva en resolver()
		matriz[fila][col] = 0
	return False # retorna false cuando no hay solución
'''
'''
#esta función entrega la matriz de numeros 9x9
def string_a_matriz(arr):
	matriz = []
	for num in arr:

		#fragmenta los string para convertirlos en las filas de la matriz
		fila = [int(n) for n in num.split()] 
		matriz.append(fila)  

	return matriz




#dibujar el sudoku
def dibujar(arr):
	for i in range(N):
		for j in range(N):
			print(arr[i][j], end=' ')
		print()#salto de linea




if __name__ == '__main__':

	arr = ['5 3 0 0 7 0 0 0 0', '6 0 0 1 9 5 0 0 0', '0 9 8 0 0 0 0 6 0', '8 0 0 0 6 0 0 0 3', 
	   '4 0 0 8 0 3 0 0 1', '7 0 0 0 2 0 0 0 6', '0 6 0 0 0 0 2 8 0', '0 0 0 4 1 9 0 0 5', '0 0 0 0 8 0 0 7 9']


	sudoku_i = string_a_matriz(arr)

	dibujar(sudoku_i)
	print()

	if (resolver(sudoku_i, 0, 0)):
		dibujar(sudoku_i)
	else:
		print('Este sudoku no tiene solución')
		