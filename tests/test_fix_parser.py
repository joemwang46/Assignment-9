import pytest
from fix_parser import FixParser

def test_fix_parser_valid_order():
    parser = FixParser()
    msg = "8=FIX.4.2|35=D|55=AAPL|54=1|38=10"
    out = parser.parse(msg)
    assert out["55"] == "AAPL"
    assert out["54"] == "1"
    assert out["38"] == "10"

def test_fix_parser_invalid_missing_tag():
    parser = FixParser()
    msg = "8=FIX.4.2|35=D|55=AAPL|38=10|"  # missing side 54
    with pytest.raises(ValueError):
        parser.parse(msg)

def test_fix_parser_malformed_field():
    parser = FixParser()
    msg = "8=FIX.4.2|35=D|BADFIELD|55=AAPL|54=1|38=10"
    with pytest.raises(ValueError):
        parser.parse(msg)

def test_fix_parser_quote_message():
    parser = FixParser()
    msg = "8=FIX.4.2|35=S|55=MSFT|132=100.5|133=101.2"
    out = parser.parse(msg)
    assert out["132"] == "100.5"
    assert out["133"] == "101.2"
