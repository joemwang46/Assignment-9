class RiskEngine:
    def __init__(self, max_order_size=1000, max_position=2000):
        self.max_order_size = max_order_size
        self.max_position = max_position
        self.positions = {}

    def check(self, order) -> bool:
        symbol = order.symbol
        qty = order.qty
        side = order.side

        current_pos = self.positions.get(symbol, 0)

        if qty > self.max_order_size:
            print(f"[RISK REJECT] {symbol} order size {qty} exceeds max order size {self.max_order_size}.")
            return False

        if side == "BUY":
            new_pos = current_pos + qty
        else:
            new_pos = current_pos - qty

        if abs(new_pos) > self.max_position:
            print(f"[RISK REJECT] {symbol} position limit exceeded: {current_pos} → {new_pos}. Max = {self.max_position}.")
            return False

        return True

    def update_position(self, order):
        symbol = order.symbol
        qty = order.qty
        side = order.side

        current_pos = self.positions.get(symbol, 0)

        if side == "BUY":
            self.positions[symbol] = current_pos + qty
        else:
            self.positions[symbol] = current_pos - qty
