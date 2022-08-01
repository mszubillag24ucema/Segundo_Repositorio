
vehicles = {
    "moto": 10,
    "auto": 20,
    "camioneta": 25,
    "camion": 60,
    "camion con acoplado": 90,
    "emmett brown": 200
}

def print_ticket(category):
    try:
        vehicle_price = vehicles[category]
        print("Imprimiendo...")
        print(f"Vehículo {category.upper()} tarifa: ${vehicle_price}\n")
    except KeyError:
        print(f"No se puedo encontrar la categoria {category}")


def user_menu():
    while True:
        print("1 - Moto")
        print("2 - Auto")
        print("3 - Camioneta")
        print("4 - Camion")
        print("5 - Camion con acoplado")
        print("6 - Emmett Brown")

        option = input(">> ")

        if option == "1":
            print_ticket('moto')
        elif option == "2":
            print_ticket('auto')
        elif option == "3":
            print_ticket('camioneta')
        elif option == "4":
            print_ticket('camion')
        elif option == "5":
            print_ticket('camion con acoplado')
        elif option == "6":
            print_ticket('emmett brown')
        else:
            print("Opcion invalida")


user_menu()
