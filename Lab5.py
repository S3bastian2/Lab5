import random 
from listaDoble import ListaDoble
from Usuario import *
#Clase ordenador

class Ordenador:
    def __init__(self, A: list, capacity: int):
        self.__A = A
        self.__limit = capacity
         

    def inicializar(self):                  #Inicializa aleatoriamente los valores del arreglo 
      A = [random.randint(1, 50) for _ in range(0, self.__limit)]
      self.__A = A
      

    def ordenar_burbuja(self, n):
      n = self.__limit
      for i in range(n):
        for j in range( 1, n-i):
            if self.__A[j-1] > self.__A[j]:
                self.__A[j-1], self.__A[j] = self.__A[j], self.__A[j-1]

    def ordenar_seleccion(self, n):
       n = self.__limit
       for i in range(n): 
        minIndex = i 
        for j in range(i + 1, n):
            if self.__A[j] < self.__A[minIndex]:
                minIndex = j  
        self.__A[i], self.__A[minIndex] = self.__A[minIndex], self.__A[i]

    def ordenar_insercion(self, n):
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

    def ordenar_mergeSort(self, arr):
        n = len(self._A)

        if n <= 1:
            return arr 

        mid = n // 2
        left_half = arr[:mid].copy()
        right_half = arr[mid:].copy()

        left_half = self.ordenar_mergeSort(left_half)  
        right_half = self.ordenar_mergeSort(right_half)  

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

class Ordenador_Lista:
    def __init__(self):
        self._L= []

    def inicializar(self, n):
        for _ in range(n):
            numero_aleatorio = random.randint(1, 100)
            self._L.append(numero_aleatorio)

    def mostrar(self):
        print("Lista:", end = " " )
        for elemento in self._L:
            print(elemento, end= ", ")
        print()

    def ordenar(self):
        n = len(self._L)
        for i in range(n):
            for j in range(0, n-i-1):
                if self._L[j] > self._L[j+1]:
                    self._L[j], self._L[j+1] = self._L[j+1], self._L[j]
    
class ordenador_agenda():
    def __init__(self, L = None):
       
        if L is not None:
            self.__L = L 
        else:
            L = ListaDoble(None, None, 0)
        
    
    def ordenador_agenda(self):
        self.__init__(L = None)
    
    def agregarUsuario(self, u):
       self.__L.addLast(u)
    
    def ordenar(self):
        Usulist = []
        for i in range(len(self.__L)):
           if self.__L.__head == None:
              return False
           else:
              if self.__L.size!= 0:
                temp = self.__L.removeLast()
                Usulist.append(temp.getId())
        #burvbuja 
        n = len(Usulist)
        for i in range(n):
            for j in range( 1, n-i):
             if Usulist[j-1] > Usulist[j]:
                Usulist[j-1], Usulist[j] = Usulist[j], Usulist[j-1]
        print(Usulist)

      
        
            
        
              

    