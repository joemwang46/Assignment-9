from enum import Enum, auto
import random

class OrderState(Enum):
    NEW = auto()
    ACKED = auto()
    FILLED = auto()
    CANCELED = auto()
    REJECTED = auto()

class Order:
    def __init__(self, symbol, qty, side):
        self.symbol = symbol
        self.qty = qty
        self.side = side
        self.state = OrderState.NEW
        self.id = random.randint(100000, 999999)

    def transition(self, new_state):
        allowed = {
            OrderState.NEW: {OrderState.ACKED, OrderState.REJECTED},
            OrderState.ACKED: {OrderState.FILLED, OrderState.CANCELED},
        }

        if new_state in allowed.get(self.state, set()):
            self.state = new_state
            print(f"Order {self.symbol} is now {self.state}")
        else:
            raise ValueError("Invalid state transition")
