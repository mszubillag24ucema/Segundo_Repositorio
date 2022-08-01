from clients import Client
from cards import DebitCard, CreditCard

CATEGORY_GOLD = "GOLD"
CATEGORY_PLATINUM = "PLATINUM"
CATEGORY_BLACK = "BLACK"

# Creamos las instancias de TC, TD y CLI
dc = DebitCard("2343 2343 9804 9084 90845", CATEGORY_PLATINUM, "05/22", "05/26", "822")
cc = CreditCard("2343 2343 9804 9084 90847", CATEGORY_PLATINUM, "05/22", "05/26", "123", 50000)
cli1 = Client("Martin", "Coronado", "+54 11 23123232", "2932932", "Belgrano 123", CATEGORY_PLATINUM, dc, cc)

print(cli1)

# Agregar tarjeta de credito o debito (esto pisara la tarjeta actual del cliente)
cli1.add_credit_card(cc)
cli1.add_debit_card(dc)

print(cli1)

# Cambiar la categoria del cliente
cli1.upgrade_category(CATEGORY_BLACK)

print(cli1)

# Cancelar una tarjeta de credito
cli1.cancel_credit_card()

print(cli1)

# Suspender un cliente
cli1.suspend_client()

print(cli1.client_state())





