from risk_engine import RiskEngine
from order import Order

def test_risk_blocks_large_orders():
    risk = RiskEngine(max_order_size=50)
    o = Order("AAPL", 100, "BUY")
    assert risk.check(o) is False

def test_risk_blocks_position_limit():
    risk = RiskEngine(max_position=100)
    risk.positions["AAPL"] = 90

    o = Order("AAPL", 20, "BUY")
    assert risk.check(o) is False

def test_risk_allows_valid_order():
    risk = RiskEngine()
    o = Order("AAPL", 10, "BUY")
    assert risk.check(o) is True

def test_update_position_buy():
    risk = RiskEngine()
    o = Order("AAPL", 10, "BUY")
    risk.update_position(o)
    assert risk.positions["AAPL"] == 10

def test_update_position_sell():
    risk = RiskEngine()
    o = Order("AAPL", 10, "SELL")
    risk.update_position(o)
    assert risk.positions["AAPL"] == -10
