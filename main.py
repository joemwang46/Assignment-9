from fix_generator import Generator
from fix_parser import FixParser
from order import Order, OrderState
from risk_engine import RiskEngine
from logger import Logger

if __name__ == "__main__":
    generator = Generator()
    fix = FixParser()
    risk = RiskEngine()
    log = Logger()


    for _ in range(100):
        raw = generator.generate()
        msg = fix.parse(raw)

        order = Order(msg["55"], int(msg["38"]), msg["54"])
        log.log("OrderCreated", msg)

        try:
            risk.check(order)
            order.transition(OrderState.ACKED)
            risk.update_position(order)
            order.transition(OrderState.FILLED)
            log.log("OrderFilled", {"symbol": order.symbol, "qty": order.qty})
        except ValueError as e:
            order.transition(OrderState.REJECTED)
            log.log("OrderRejected", {"reason": str(e)})

        log.save()