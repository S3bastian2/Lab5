import random 

#Clase ordenador

class Ordenador:
    def __init__(self, A: list, capacity: int):
        self.__A = A
        self.__limit = capacity
         

    def inicializar(self):                  #Inicializa aleatoriamente los valores del arreglo 
      A = [random.randint(1, 50) for _ in range(0, self.__limit)]
      self.__A = A
      

    def ordenar_burbuja(self):
      n = self.__limit
      for i in range(n):
        for j in range( 1, n-i):
            if self.__A[j-1] > self.__A[j]:
                self.__A[j-1], self.__A[j] = self.__A[j], self.__A[j-1]

    def ordenar_seleccion(self):
       n = self.__limit
       for i in range(n): 
        minIndex = i 
        for j in range(i + 1, n):
            if self.__A[j] < self.__A[minIndex]:
                minIndex = j  
        self.__A[i], self.__A[minIndex] = self.__A[minIndex], self.__A[i]

    def ordenar_insercion(self):
     n = self.__limit
     for i in range(1, n):
        temp = self.__A[i]
        j=i
        while j>0 and self.__A[j-1]> temp:
            self.__A[j] = self.__A[j-1]
            j -= 1
        self.__A[j] = temp

    def merge(arr, left, right):
 
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    def merge_sort(self, arr):
        n = len(self._A)

        if n <= 1:
            return arr 

        mid = n // 2
        left_half = arr[:mid].copy()
        right_half = arr[mid:].copy()

        left_half = self.merge_sort(left_half)  
        right_half = self.merge_sort(right_half)  

        return self.merge(arr, left_half, right_half)


    def mostrar(self):
     print ("Arreglo :", self.__A)

    def busqueda_binaria(self, A, x, iL, iR):
     if iL > iR:
        return -1                    # En el main se inicia con resultado = busqueda_binaria(arreglo, x)
     else:                              #        if resultado != -1: 
        mid = (iL + iR) // 2            #           print(f"El numero está en el indice",resultado)
        if x < A[mid]:
            return self.busqueda_binaria(self, A, x, iL, mid-1)
        elif x > A[mid]:
            return self.busqueda_binaria(self, A, x, mid+1, iR)
        else:
            return mid