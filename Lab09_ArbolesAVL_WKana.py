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

    def in_order_niveles(self, raiz, nivel = 0):
        if raiz != None:
            self.in_order_niveles(raiz.izquierda, nivel +1)
            print((nivel * 4 * "-") + str(raiz.dato))
            self.in_order_niveles(raiz.derecha, nivel +1)

arbol = ArbolAVL()
arbol.insertar(12)
arbol.insertar(3)
arbol.insertar(9)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(2)
arbol.in_order_niveles(arbol.raiz)
