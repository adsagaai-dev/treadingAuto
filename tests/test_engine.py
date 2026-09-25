import pytest

from treading_auto.engine import dry_run_trade


def test_dry_run_trade_buy():
    trade = dry_run_trade("aapl", side="buy", quantity=2)
    assert trade.symbol == "AAPL"
    assert trade.side == "buy"
    assert trade.quantity == 2
    assert trade.simulated is True


def test_dry_run_trade_rejects_invalid_side():
    with pytest.raises(ValueError, match="side"):
        dry_run_trade("AAPL", side="hold")
