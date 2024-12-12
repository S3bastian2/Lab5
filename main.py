from Usuario import *
from listaDoble import ListaDoble
from nodoDoble import nodoDoble
from Lab5 import *

u1 = Usuario("David", 1, "Valledupar", 3134697894, "david@recocha.edu.co")
f1 = Fecha(13, 11, 2006)
d1 = Direccion("Kra 92", "74B-08", "Robledo", "Medellín", None, None)

u1.setFechaNacimiento(f1)
u1.setDir(d1)

u2 = Usuario("Carlos", 2, "Bogotá", 3123456789, "carlos@ejemplo.com")
f2 = Fecha(25, 5, 1992)
d2 = Direccion("Av. Chile", "21A-12", "Teusaquillo", "Bogotá", None, None)

u2.setFechaNacimiento(f2)
u2.setDir(d2)

k = [u1, u2]
Usuarios = ordenador_agenda(k)
Usuarios.ordenar()
print(Usuarios)