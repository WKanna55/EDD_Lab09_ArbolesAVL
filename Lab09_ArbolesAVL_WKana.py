"""Implementacion de un Arbol AVL(inicio)"""

class NodoAVL:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        self.altura = None

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self.insertar_(valor, self.raiz)

    def insertar_(self, valor, raiz):
        if raiz is None: #raiz vacia o sin datos
            return NodoAVL(valor)
        if valor > raiz.dato:
            raiz.derecha = self.insertar_(valor, raiz.derecha)
        else:
            raiz.izquierda = self.insertar_(valor, raiz.izquierda)
        raiz.altura = self.set_altura(raiz)
        return self.balancear(raiz)

    def eliminar(self, valor):
        self.raiz = self.eliminar_(valor, self.raiz)

    def eliminar_(self, valor, raiz):
        # 4to caso, raiz is none
        if not raiz:
            return raiz

        # Busqueda del elemento
        if raiz.dato > valor:
            raiz.izquierda = self.eliminar_(valor, raiz.izquierda)
        elif raiz.dato < valor:
            raiz.derecha = self.eliminar_(valor, raiz.derecha)
        else:  # Encontrado al elemento
            # 3er caso: nodo hoja
            if raiz.derecha is None and raiz.izquierda is None:
                return None

            # 2do caso: 1 hijo
            if raiz.derecha is None:
                return raiz.izquierda
            if raiz.izquierda is None:
                return raiz.derecha

            # 1er caso: 2 hijos
            max_value = self.max(raiz.izquierda)
            raiz.dato = max_value
            raiz.izquierda = self.eliminar_(max_value, raiz.izquierda)
            raiz.altura = self.set_altura(raiz)
        return self.balancear(raiz)

    def buscar(self, valor):
        return self.buscar_(valor, self.raiz)

    def buscar_(self, valor, raiz):
        if raiz is None:
            return False
        else:
            if valor == raiz.dato:
                return True
            if valor > raiz.dato:
                return self.buscar_(valor, raiz.derecha)
            else:
                return self.buscar_(valor, raiz.izquierda)

    def verificar_factor(self):
        return self.verificar_factor_(self.raiz)

    def verificar_factor_(self, nodo):
        if nodo is not None: # recorrer no vacios
            if nodo.izquierda is not None:
                return self.verificar_factor_(nodo.izquierda)
            if nodo.derecha is not None:
                return self.verificar_factor_(nodo.derecha)
            if self.factor_equilibrio(nodo) > 1 or self.factor_equilibrio(nodo) < -1:
                print("El arbol NO cumple con los factores de equilibrio")
                return False
            else:
                print("El arbol cumple con los factores de equilibrio")
                return True

    def verficar_perfecto(self):
        return self.verficar_perfecto_(self.raiz)

    def verficar_perfecto_(self, raiz):
        if raiz is not None:# recorrer todoo el arbol
            if self.factor_equilibrio(raiz) == 0:
                return True
            else:
                return False
        return [self.verficar_perfecto_(raiz.izquierda), self.verficar_perfecto_(raiz.derecha)]


    def rotar_izquierda(self, raiz):
        raiz_nueva = raiz.derecha
        raiz.derecha = raiz_nueva.izquierda
        raiz_nueva.izquierda = raiz
        self.set_altura(raiz)
        self.set_altura(raiz_nueva)
        return raiz_nueva

    def rotar_derecha(self, raiz):
        raiz_nueva = raiz.izquierda
        raiz.izquierda = raiz_nueva.derecha
        raiz_nueva.derecha = raiz
        self.set_altura(raiz)
        self.set_altura(raiz_nueva)
        return raiz_nueva

    def factor_equilibrio(self, nodo):
        if nodo is None: return 0
        else: return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def balancear(self, raiz):
        if self.pesado_izquierda(raiz):
            if self.factor_equilibrio(raiz.izquierda) < 0:
                raiz.izquierda = self.rotar_izquierda(raiz.izquierda)
            return self.rotar_derecha(raiz)
        elif self.pesado_derecha(raiz):
            if self.factor_equilibrio(raiz.derecha)>0:
                raiz.derecha = self.rotar_derecha(raiz.derecha)
            return self.rotar_izquierda(raiz)
        return raiz

    def pesado_izquierda(self, nodo): # f >+1
        return self.factor_equilibrio(nodo) > 1

    def pesado_derecha(self, nodo): # f <-1
        return self.factor_equilibrio(nodo) < -1

    def altura(self, raiz):
        if raiz is None:
            return -1
        return max(self.altura(raiz.izquierda), self.altura(raiz.derecha)) + 1

    def set_altura(self, nodo):
        nodo.altura = max(self.altura(nodo.izquierda), self.altura(nodo.derecha)) + 1

    def min(self, raiz):
        if raiz is not None:
            if raiz.izquierda is None:
                return raiz.dato
            return self.min(raiz.izquierda)

    def max(self, raiz):
        if raiz is not None:
            if raiz.derecha is None:
                return raiz.dato
            return self.max(raiz.derecha)

    def in_order_niveles(self):
        return self.in_order_niveles_(self.raiz)
    def in_order_niveles_(self, raiz, nivel = 0):
        if raiz != None:
            self.in_order_niveles_(raiz.izquierda, nivel +1)
            print((nivel * 4 * "-") + str(raiz.dato))
            self.in_order_niveles_(raiz.derecha, nivel +1)

"""Implementacion de un Arbol AVL(fin)"""

"""Ejercicio 01: Insercion en un arbol AVL(inicio)"""
arbol1 = ArbolAVL()
arbol1.insertar(10)
arbol1.insertar(5)
arbol1.insertar(20)
arbol1.insertar(3)
arbol1.insertar(8)
arbol1.insertar(15)
arbol1.insertar(25)
#arbol1.in_order_niveles()
"""Ejercicio 01: Insercion en un arbol AVL(fin)"""

"""Ejercicio 02: Busqueda en un arbol AVL(inicio)"""
arbol2 = ArbolAVL()
arbol2.insertar(15)
arbol2.insertar(10)
arbol2.insertar(20)
arbol2.insertar(5)
arbol2.insertar(12)
arbol2.insertar(18)
arbol2.insertar(25)
#arbol2.in_order_niveles()
#print(arbol2.buscar(18))
#print(arbol2.buscar(8))
#print(arbol2.buscar(30))
"""Ejercicio 02: Busqueda en un arbol AVL(fin)"""

"""Ejercicio 03: Eliminacion en un arbol AVL(inicio)"""
arbol3 = ArbolAVL()
arbol3.insertar(20)
arbol3.insertar(15)
arbol3.insertar(30)
arbol3.insertar(10)
arbol3.insertar(18)
arbol3.insertar(25)
arbol3.insertar(35)
#arbol3.in_order_niveles()
#print("\n\n")
arbol3.eliminar(18)
#arbol3.in_order_niveles()
#print("\n\n")
arbol3.eliminar(10)
#arbol3.in_order_niveles()
#print("\n\n")
arbol3.eliminar(30)
#arbol3.in_order_niveles()
"""Ejercicio 03: Eliminacion en un arbol AVL(fin)"""

"""Ejercicio 04: Comprobacion del Factor de Equilibrio(inicio)"""
#arbol3.verificar_factor()
"""Ejercicio 04: Comprobacion del Factor de Equilibrio(fin)"""

"""Ejercicio 05: Altura de un arbol AVL(inicio)"""
#print(arbol1.factor_equilibrio(arbol1.raiz))
#print(arbol1.verificar_factor())
"""Ejercicio 05: Altura de un arbol AVL(fin)"""

"""Ejercicio 06: Construccion de un arbol AVL(inicio)"""
arbol6 = ArbolAVL()
arbol6.insertar(12)
arbol6.insertar(6)
arbol6.insertar(20)
arbol6.insertar(3)
arbol6.insertar(9)
arbol6.insertar(15)
arbol6.insertar(25)
#arbol6.verificar_factor()
#arbol6.in_order_niveles()
"""Ejercicio 06: Construccion de un arbol AVL(fin)"""

"""Ejercicio 07: Arbol balanceado(inicio)"""
# tomamos el arbol2 apra ello
# balance indica que cumple el factor de equilibrio

#arbol2.verificar_factor()

"""Ejercicio 07: Arbol balanceado(fin)"""

"""Ejercicio 08: Arbol perfecto(inicio)"""
#print(arbol1.verficar_perfecto())
#print(arbol3.verficar_perfecto())
"""Ejercicio 08: Arbol perfecto(fin)"""

