
"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Sofia Valero Martinez
"""

import doctest
class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)



    def __add__(self, other):
        """
        Multiplicacion al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other
    
    
    def __mul__(self, other):
        """
        multiplicacion
        >>> v1 = Vector([1, 2, 3]) 
        >>> v2 = Vector([4, 5, 6])
        >>> v1 * v2 
        Vector([4, 10, 18])
        >>> v1 * 2
        Vector([2, 4, 6])
        """
        if isinstance(other, (int, float, complex)):
            return Vector(self[i] * other for i in range (0, len(self)))
        else:
            return Vector(self[i] * other[i] for i in range (0, len(self)))
        
    __rmul__ = __mul__

    def __matmul__(self, other):
        """
        Multiplicación matricial
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 @ v2
        32
        """

        return sum(self[i] * other[i] for i in range (0, len(self)))

    def __floordiv__(self, other):
        """
        tangencial
        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 // v2
        Vector([1.0, 2.0, 1.0])
        """

        return Vector(other * ((self @ other) / (other @ other)))
    
    __rfloordiv__ = __floordiv__


    def __mod__(self, other):
        """
        normal
        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 % v2
        Vector([1.0, -1.0, 1.0])
        """
        return Vector(self - self // other)
    
    __rmod__ = __mod__






doctest.testmod()
