from main import Card


class System:
    def accept_card(self, card: Card):
        pass

    def show_balance(self, balance: int):
        pass

    def change_pin(self, pin: int):
        pass

    def transfer_money_to_other_account(self, balance: float, card_number: int, account_card_number: int):
        pass

    def accept_money(self, card_number: int, balance: float):
        pass

    def withdraw_money(self, card_number: int, balance: float):
        pass

    def block_card(self, card: Card):
        pass

    def input_pin(self, pin: int):
        pass
