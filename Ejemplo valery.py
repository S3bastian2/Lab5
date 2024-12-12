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

    def Merge(self, p, q, r):
     n1 = q - p + 1
     n2 = r - q
     L = [0] + n1
     R = [0] + n2
     for i in range(n1):
        L[i] = self.__A[p +1]
     for j in range(n2):
        R[j] = self.__A[q + 1 + j] 
     i = 0
     j = 0
     k = p
     for k in range(p, r +1):
        if L[i] <= R[j]:
            self.__A[k] = L[i]
            i += 1
        else:
            self.__A[k] = R[j]
            j += 1

    def ordenar_mergeSort(self, p, r):
     #p = self.__A[0]
     #r = self.__A[-1]
     print(p,r)
     if p < r:
        q = (p + r) // 2
        print(q)
        self.ordenar_mergeSort(self.__A, p, q)
        self.ordenar_mergeSort(self.__A, q + 1, r)
        self.Merge(self, p, q, r)

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