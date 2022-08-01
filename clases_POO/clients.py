import random


class Client:

    def __init__(self, firstname, lastname, phone_number, document, full_address, category, debit_card,
                 credit_card=None):
        self.id = random.randrange(10000000)
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.document = document
        self.full_address = full_address
        self.category = category
        self.is_client_active = True
        # client cards
        self.debit_card = debit_card
        self.credit_card = credit_card

    def add_credit_card(self, credit_card):
        self.credit_card = credit_card

    def add_debit_card(self, debit_card):
        self.debit_card = debit_card

    def upgrade_category(self, new_category):
        self.category = new_category
        if self.debit_card:
            self.debit_card.upgrade_category(new_category)
        if self.credit_card:
            self.credit_card.upgrade_category(new_category)

    def cancel_credit_card(self):
        self.credit_card = None

    def suspend_client(self):
        self.is_client_active = False
        self.debit_card = None
        self.credit_card = None

    def client_state(self):
        if self.is_client_active:
            return f"Cliente activo"
        else:
            return f"Cliente numero: {self.id} esta suspendido"

    def __str__(self):
        response = f"\nNombre completo: {self.firstname} {self.lastname}" \
                   f"\nTelefono: {self.phone_number}" \
                   f"\nDocumento de Identidad: {self.document}" \
                   f"\nDireccion completa: {self.full_address}" \
                   f"\nCategoria: {self.category}" \
                   "\n----------- Tarjetas -----------" \
                   f"\nTarjeta de Debito: {self.debit_card}"
        if self.credit_card:
            response += f"\nTarjeta de Credito: {self.credit_card}"

        return response
