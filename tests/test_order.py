import pytest
from order import Order, OrderState

def test_order_initial_state():
    o = Order("AAPL", 10, "BUY")
    assert o.state == OrderState.NEW

def test_order_valid_transition():
    o = Order("AAPL", 10, "BUY")
    o.transition(OrderState.ACKED)
    assert o.state == OrderState.ACKED

def test_order_invalid_transition():
    o = Order("AAPL", 10, "BUY")
    with pytest.raises(ValueError):
        o.transition(OrderState.FILLED)

def test_order_has_required_fields():
    o = Order("MSFT", 5, "SELL")
    assert o.symbol == "MSFT"
    assert o.qty == 5
    assert o.side == "SELL"
    assert isinstance(o.id, int)
