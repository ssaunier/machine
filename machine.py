from enum import Enum

class Rack:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = 0

class Coin(Enum):
    NICKEL = 5
    DIME = 10
    QUARTER = 25
    DOLLAR = 100

class Machine:
    def __init__(self, racks, coint_count = 0):
        self.racks = {}
        self.coins = {
            Coin.NICKEL: coint_count,
            Coin.DIME: coint_count,
            Coin.QUARTER: coint_count,
            Coin.DOLLAR: coint_count
        }
        for rack in racks:
            self.racks[rack.code] = rack
        self.amount = 0

    def refill(self, code, quantity):
        self.racks[code].quantity += quantity

    def insert(self, coin):
        self.coins[coin] += 1
        self.amount += coin.value

    def press(self, code):
        rack = self.racks[code]
        if self.amount >= rack.price:
            if rack.quantity > 0:
                rack.quantity -= 1
                change = self.amount - rack.price
                if change > 0:
                    self.__give_change(change)
                self.amount -= rack.price
            else:
                self.__give_change(self.amount)
                print("product not available")
        else:
            print("not enough money")

    def __give_change(self, change):
        for coin in reversed(Coin):
            count = change // coin.value
            if count <= self.coins[coin]:
                change = change % coin.value
                self.coins[coin] -= count
