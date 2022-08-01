import json
import requests
from flask import Flask
from flask import request
from flask import jsonify


from clientes_obj import Cliente, generador_id_cliente
from load_cliente import cargar_clientes
from load_cartera import cargar_carteras

app = Flask(__name__)
clientes: list = cargar_clientes()      #formas de aclarar que tipo de datos es
carteras: list = cargar_carteras()      #vamos a hacer algo igual para carteras


@app.route("/api/el_galpon_de_lujo/generar_usuario/", methods = ['POST'])
def crear_cliente():
    cliente = request.json

    try:
        nuevo_cliente = Cliente(
            generador_id_cliente(),
            cliente['nombre'],
            cliente['apellido'],
            cliente['dni'],
            cliente['telefono'],
            cliente['email'],
            cliente['estado'],
            cliente['carrito']
        )

        clientes.insert(len(clientes),nuevo_cliente)

    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code="400",
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(nuevo_cliente.serialize())


@app.route("/api/el_galpon_de_lujo/carteras", methods = ['GET'])    #ver catalogo
def ver_catalogo():
    return jsonify([cartera.serialize() for cartera in carteras])


@app.route("/api/el_galpon_de_lujo/carteras/marca/<marca>", methods=['GET'])      #ver carteras por marca
def ver_cartera_por_marca(marca):
    carteras_marca = []
    for cartera in carteras:
        if cartera.marca == marca:
            carteras_marca.append(cartera)
    return jsonify([cartera.serialize() for cartera in carteras_marca])



@app.route("/api/el_galpon_de_lujo/carteras/<id>", methods=['GET'])     #ver una cartera por id
def ver_cartera_por_id(id):
    for cartera in carteras:
        if cartera.id == id:
            return jsonify(cartera.serialize())
    return jsonify({f'El producto con el id {id}': 'No existe'})


@app.route("/api/el_galpon_de_lujo/precio_ARS/<id>", methods=['GET'])       #Ver el precio de una cartera en ARS
def precio_ARS(id):
    for cartera in carteras:
        if cartera.id == id:
            url = "https://api.apilayer.com/exchangerates_data/convert?to=ARS&from={tipo_de_cambio}&amount={precio}".format(
                tipo_de_cambio = cartera.tipo_de_cambio, precio = cartera.precio
            )
            payload = {}
            headers = {
                "apikey": "2fmmJ7Dlc4Wuh2XTDemrC75HYq9Zc9eQ"
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            rsps_json = response.json()

            return {f'El precio original en {cartera.tipo_de_cambio} es': cartera.precio,
                    'El precio en ARS es' : rsps_json["result"]}
    return jsonify({f'El producto con el id {id}': 'No existe'})

@app.route("/api/el_galpon_de_lujo/carrito/<id_cliente>/agregar/<id>", methods=['PUT'])       #Agregar a carrito por id
def agregar_a_carrito(id_cliente, id):
    for cartera in carteras:
        for cliente in clientes:
            if cartera.id == id and cliente.id_cliente == id_cliente:
                cliente.carrito.append(cartera)
                return jsonify([producto.serialize() for producto in cliente.carrito])
    return jsonify({f'El id de la cartera: {id}  y/o el id del cliente: {id_cliente}': 'Han sido escritos incorrectamente o no existen'})


@app.route("/api/el_galpon_de_lujo/carrito/<id_cliente>/eliminar/<id>", methods=['DELETE'])      #Eliminar producto de carrito por id
def eliminar_de_carrito(id_cliente, id):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            for producto in cliente.carrito:
                if producto.id == id:
                    cliente.carrito.remove(producto)
                    return jsonify({'Busqueda': id, 'Estado': 'Se ha eliminado el producto'})
    return jsonify({'Opción 1: ': f'El producto con el id {id} No esta en el carrito o no existe',
                    'Opción 2': f'El id del cliente {id_cliente} no existe o ha sido escrito incorrectamente'})


@app.route("/api/el_galpon_de_lujo/carrito/<id_cliente>", methods = ['GET'])        #ver carrito
def ver_carrito(id_cliente):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            return jsonify([producto.serialize() for producto in cliente.carrito])
    return jsonify({f'Error. Cliente {id_cliente}': 'No encontrado'})


@app.route("/api/el_galpon_de_lujo/terminar_compra/<id_cliente>", methods=['GET'])         #terminar compra
def terminar_compra(id_cliente):
    precios_ARS = []
    precio_total_ARS = 0
    for cliente in clientes:
        if cliente.id_cliente ==  id_cliente:
            for producto in cliente.carrito:
                url = "https://api.apilayer.com/exchangerates_data/convert?to=ARS&from={tipo_de_cambio}&amount={precio}".format(
                    tipo_de_cambio=producto.tipo_de_cambio, precio=producto.precio
                )
                payload = {}
                headers = {
                    "apikey": "2fmmJ7Dlc4Wuh2XTDemrC75HYq9Zc9eQ"
                }
                response = requests.request("GET", url, headers=headers, data=payload)
                rsps_json = response.json()
                precios_ARS.append(rsps_json['result'])
                precio_total_ARS = sum(precios_ARS)
            return jsonify({'Cliente': id_cliente,
                            'Estado': 'Se ha finalizado la compra',
                            'Total a pagar en ARS $': precio_total_ARS,
                            'Mensaje': 'Muchas gracias! Pronto le llegará un mail sobre como proceder con el pago'})
    return jsonify({f'El cliente ingresado {id_cliente}': 'No existe'})


