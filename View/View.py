import os

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen


class EnterCardScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_button_click(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'pin_change'


class PinScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_button_click(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'continue_work'


class PinChangeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_button_click(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'operations'


class OperationsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_checkout_button_click(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'enter_amount'

    def on_cash_entry_button_click(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'enter_amount'

    def on_pin_enter_button_click(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'pin'

    def on_card_number_enter_button_click(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'card_number_enter'

    def on_balance_button_click(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'balance'

    def on_extract_card_button_click(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'extract_card'


class BalanceScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_button_click(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'continue_work'


class AmountEnterScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_button_click(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'continue_work'


class CardNumberEnterScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_button_click(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'continue_work'


class ContinueWorkScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_yes_button_click(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'operations'

    def on_no_button_click(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'extract_card'


class ExtractCardScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_button_click(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'enter_card'


class NoFundsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BlockedCardScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


Builder.load_file(os.path.join(os.path.dirname(__file__), "screens.kv"))
