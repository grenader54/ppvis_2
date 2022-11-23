from kivy.config import Config

Config.set("graphics", "resizable", '0')
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

from View.View import *
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager


class Card:
    def __init__(self, balance: float, card_number: int, pin: int, isBlocked: bool):
        self.__balance: float = balance
        self.__card_number: int = card_number
        self.__pin: int = pin
        self.__isBlocked: bool = isBlocked

    def get_balance(self):
        return self.__balance

    def get_card_number(self):
        return self.__card_number

    def get_pin(self):
        return self.__pin

    def get_is_blocked(self):
        return self.__isBlocked


class ATM:
    def __init__(self, personal_id: int):
        self.__personal_id = personal_id

    def get_personal_id(self):
        return self.__personal_id


class MyApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        sm = ScreenManager()
        sm.add_widget(EnterCardScreen(name='enter_card'))
        sm.add_widget(OperationsScreen(name='operations'))
        sm.add_widget(PinScreen(name='pin'))
        sm.add_widget(PinChangeScreen(name='pin_change'))
        sm.add_widget(BalanceScreen(name='balance'))
        sm.add_widget(AmountEnterScreen(name='enter_amount'))
        sm.add_widget(CardNumberEnterScreen(name='card_number_enter'))
        sm.add_widget(ContinueWorkScreen(name='continue_work'))
        sm.add_widget(ExtractCardScreen(name='extract_card'))
        sm.add_widget(NoFundsScreen(name='no_funds'))
        sm.add_widget(BlockedCardScreen(name='blocked_card'))
        return sm


if __name__ == "__main__":
    MyApp().run()
