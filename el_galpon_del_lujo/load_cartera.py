import json
from carteras_obj import Carteras, Mochila, Totebag, Clutch, CrossBody

def cargar_carteras():
    carteras = []

    with open('./bd_carteras.json', 'r') as file:
        bd_carteras = json.load(file)
        for cartera in bd_carteras:
            if cartera["modelo"] == "Mochila":
                carteras.append(
                    Mochila(
                        cartera['id'],
                        cartera['fecha_ingreso'],
                        cartera['modelo'],
                        cartera['marca'],
                        cartera['color'],
                        cartera['tipo_de_cambio'],
                        cartera['precio']
                    )
                )
            elif cartera["modelo"] == "Totebag":
                carteras.append(
                    Totebag(
                        cartera['id'],
                        cartera['fecha_ingreso'],
                        cartera['modelo'],
                        cartera['marca'],
                        cartera['color'],
                        cartera['tipo_de_cambio'],
                        cartera['precio']
                    )
                )
            elif cartera["modelo"] == "Clutch":
                carteras.append(
                    Clutch(
                        cartera['id'],
                        cartera['fecha_ingreso'],
                        cartera['modelo'],
                        cartera['marca'],
                        cartera['color'],
                        cartera['tipo_de_cambio'],
                        cartera['precio']
                    )
                )
            elif cartera["modelo"] == "Cross Body":
                carteras.append(
                    CrossBody(
                        cartera['id'],
                        cartera['fecha_ingreso'],
                        cartera['modelo'],
                        cartera['marca'],
                        cartera['color'],
                        cartera['tipo_de_cambio'],
                        cartera['precio']
                    )
                )
            else:
                carteras.append(
                    Carteras(
                        cartera['id'],
                        cartera['fecha_ingreso'],
                        cartera['modelo'],
                        cartera['marca'],
                        cartera['color'],
                        cartera['tipo_de_cambio'],
                        cartera['precio']
                    )
                )
    return carteras
