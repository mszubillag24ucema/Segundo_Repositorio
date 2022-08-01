import csv

carteras= [
    {
        "id": "0001",
        "fecha_ingreso": "21/07/2020",
        "modelo": "Clutch",
        "marca": "Gucci",
        "color": "roja",
        "tipo_de_cambio": "EUR",
        "precio": 2000
    },
    {
        "id": "0002",
        "fecha_ingreso": "22/06/2019",
        "modelo": "Totebag",
        "marca": "Louis Vuitton",
        "color": "marrón",
        "tipo_de_cambio": "USD",
        "precio": 4000
    },
    {
        "id": "0003",
        "fecha_ingreso": "9/12/2018",
        "modelo": "Clutch",
        "marca": "Chanel",
        "color": "negra",
        "tipo_de_cambio": "EUR",
        "precio": 3500
    },
    {
        "id": "0004",
        "fecha_ingreso": "4/08/2020",
        "modelo": "Cross Body",
        "marca": "Prada",
        "color": "negra",
         "tipo_de_cambio": "USD",
         "precio": 1500
    },
    {
        "id": "0005",
        "fecha_ingreso": "13/05/2020",
        "modelo": "Mochila",
        "marca": "Fendi",
        "color": "azul",
        "tipo_de_cambio": "EUR",
        "precio": 2300
    },
    {
        "id": "0006",
        "fecha_ingreso": "18/03/2021",
        "modelo": "Totebag",
        "marca": "Hermés",
        "color": "marrón",
        "tipo_de_cambio": "USD",
        "precio": 100000
    },
    {
        "id": "0007",
        "fecha_ingreso": "17/06/2022",
        "modelo": "Clutch",
        "marca": "Louis Vuitton",
        "color": "naranja",
        "tipo_de_cambio": "USD",
        "precio": 2000
    },
    {
        "id": "0008",
        "fecha_ingreso": "13/05/2021",
        "modelo": "Mochila",
        "marca": "Gucci",
        "color": "verde",
        "tipo_de_cambio": "EUR",
        "precio": 4600
    },
    {
        "id": "0009",
        "fecha_ingreso": "7/09/2021",
        "modelo": "Cross Body",
        "marca": "Prada",
        "color": "rosa",
        "tipo_de_cambio": "USD",
        "precio": 2100
    },
    {
        "id": "0010",
        "fecha_ingreso": "3/08/2021",
        "modelo": "Totebag",
        "marca": "Chanel",
        "color": "rosa",
        "tipo_de_cambio": "USD",
        "precio": 5800
},
    {
        "id": "0011",
        "fecha_ingreso": "1/10/2021",
        "modelo": "Cross Body",
        "marca": "Louis Vuitton",
        "color": "amarillo",
        "tipo_de_cambio": "USD",
        "precio": 3600
    },
    {
        "id": "0012",
        "fecha_ingreso": "8/12/2021",
        "modelo": "Clutch",
        "marca": "Hermés",
        "color": "beige",
        "tipo_de_cambio": "EUR",
        "precio": 3000
    },
    {
        "id": "0013",
        "fecha_ingreso": "15/09/2021",
        "modelo": "Mochila",
        "marca": "Prada",
        "color": "gris",
        "tipo_de_cambio": "USD",
        "precio": 1100
    },
    {
        "id": "0014",
        "fecha_ingreso": "7/11/2021",
        "modelo": "Cross Body",
        "marca": "Prada",
        "color": "plateado",
        "tipo_de_cambio": "EUR",
        "precio": 1600
    },
    {
        "id": "0015",
        "fecha_ingreso": "17/04/2022",
        "modelo": "Clutch",
        "marca": "Chanel",
        "color": "marrón",
        "tipo_de_cambio": "USD",
        "precio": 3200
    },
    {
        "id": "0016",
        "fecha_ingreso": "4/04/2022",
        "modelo": "Totebag",
        "marca": "Hermés",
        "color": "negro",
        "tipo_de_cambio": "USD",
        "precio": 9000
    },
    {
        "id": "0017",
        "fecha_ingreso": "8/12/2021",
        "modelo": "Clutch",
        "marca": "Hermés",
        "color": "beige",
        "tipo_de_cambio": "EUR",
        "precio": 5000
    },
    {
        "id": "0018",
        "fecha_ingreso": "9/05/2021",
        "modelo": "Cross body",
        "marca": "Gucci",
        "color": "beige",
        "tipo_de_cambio": "EUR",
        "precio": 3400
    },
    {
        "id": "0019",
        "fecha_ingreso": "12/08/2021",
        "modelo": "Mochila",
        "marca": "Chanel",
        "color": "blanco",
        "tipo_de_cambio": "EUR",
        "precio": 2890
    },
    {
        "id": "0020",
        "fecha_ingreso": "9/03/2022",
        "modelo": "Totebag",
        "marca": "Fendi",
        "color": "amarillo",
        "tipo_de_cambio": "USD",
        "precio": 4500
    }
]

with open("./consulta_carteras.csv", "w", newline="\n") as archivo:
    campos = ['id', 'fecha_ingreso', 'modelo', 'marca', 'color', 'tipo_de_cambio', 'precio']
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    for cartera in carteras:
        writer.writerow({"id": cartera["id"],
                         "fecha_ingreso": cartera["fecha_ingreso"],
                         "modelo": cartera["modelo"],
                         "marca": cartera["marca"],
                         "color": cartera["color"],
                         "tipo_de_cambio": cartera["tipo_de_cambio"],
                         "precio": cartera["precio"]

                         })
archivo.close()
del (archivo)
