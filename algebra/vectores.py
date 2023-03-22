"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos:
"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        return str(self.vector)

    def __getitem__(self, key):
        return self.vector[key]

    def __setitem__(self, key, value):
        self.vector[key] = value

    def __len__(self):
        return len(self.vector)

    def __add__(self, other):
        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        return -self + other



