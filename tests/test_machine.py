import unittest
from machine import Machine, Rack, Coin

class MachineTest(unittest.TestCase):
    def test_refill(self):
        rack = Rack("A", "Biscuit", 100)
        machine = Machine([rack])
        machine.refill("A", 10)
        self.assertEqual(machine.racks['A'].quantity, 10)

    def test_buy_biscuit(self):
        rack = Rack("A", "Biscuit", 100)
        machine = Machine([rack])
        machine.refill("A", 1)
        for i in range(4):
            machine.insert(Coin.QUARTER)
        machine.press("A")
        self.assertEqual(machine.racks['A'].quantity, 0)
        self.assertEqual(machine.coins[Coin.QUARTER], 4)

    def test_buy_biscuit_no_quantity(self):
        rack = Rack("A", "Biscuit", 100)
        machine = Machine([rack])
        for i in range(4):
            machine.insert(Coin.QUARTER)
        machine.press("A")
        self.assertEqual(machine.racks['A'].quantity, 0)
        self.assertEqual(machine.coins[Coin.QUARTER], 0)

    def test_buy_biscuit_not_enough_coins(self):
        rack = Rack("A", "Biscuit", 100)
        machine = Machine([rack])
        machine.refill("A", 1)
        for i in range(3):
            machine.insert(Coin.QUARTER)
        machine.press("A")
        self.assertEqual(machine.racks['A'].quantity, 1)
        self.assertEqual(machine.coins[Coin.QUARTER], 3)

    def test_buy_biscuit_too_many_coins(self):
        rack = Rack("A", "Biscuit", 100)
        machine = Machine([rack], 10)
        machine.refill("A", 1)
        for i in range(3):
            machine.insert(Coin.QUARTER)
        for i in range(3):
            machine.insert(Coin.DIME)
        machine.press("A")
        self.assertEqual(machine.racks['A'].quantity, 0)
        self.assertEqual(machine.coins[Coin.QUARTER], 13)
        self.assertEqual(machine.coins[Coin.DIME], 13)
        self.assertEqual(machine.coins[Coin.NICKEL], 9)
