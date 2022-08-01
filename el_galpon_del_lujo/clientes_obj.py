import random

def generador_id_cliente():
    return str(random.randint(00000, 99999))


class Cliente:

    def __init__(self, id_cliente, nombre, apellido, dni, telefono, email, estado, carrito):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.email = email
        self.estado = estado
        self.carrito = carrito

    def serialize(self):
        return {
            'id_cliente': self.id_cliente,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'dni': self.dni,
            'telefono': self.telefono,
            'email': self.email,
            'estado': self.estado,
            'carrito': self.carrito
        }
