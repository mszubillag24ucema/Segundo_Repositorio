
class Card:

    def __init__(self, number, category, issued, expires, sec_code):
        self.number = number
        self.category = category
        self.issued = issued
        self.expires = expires
        self.sec_code = sec_code

    def __str__(self) -> str:
        return f"\n\tNumero: {self.number}" \
               f"\n\tCategoria: {self.category}" \
               f"\n\tFecha de emision: {self.issued}" \
               f"\n\tFecha de expiracion: {self.expires}" \
               f"\n\tCodigo de seguridad: {self.sec_code}" \


    def upgrade_category(self, new_category):
        self.category = new_category


class DebitCard(Card):

    def __init__(self, number, category, issued, expires, sec_code):
        super().__init__(number, category, issued, expires, sec_code)


class CreditCard(Card):

    def __init__(self, number, category, issued, expires, sec_code, limit_charge):
        super().__init__(number, category, issued, expires, sec_code)
        self.limit_charge = limit_charge

    def __str__(self) -> str:
        return f"\n\tNumero: {self.number}" \
               f"\n\tCategoria: {self.category}" \
               f"\n\tFecha de emision: {self.issued}" \
               f"\n\tFecha de expiracion: {self.expires}" \
               f"\n\tCodigo de seguridad: {self.sec_code}" \
               f"\n\tLimite de compra: {self.limit_charge}"

