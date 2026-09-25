from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class DryRunTrade:
    symbol: str
    side: str
    quantity: float
    executed_at: datetime
    simulated: bool = True

    def as_dict(self) -> dict:
        return {
            "symbol": self.symbol,
            "side": self.side,
            "quantity": self.quantity,
            "executed_at": self.executed_at.isoformat(),
            "simulated": self.simulated,
        }


def dry_run_trade(symbol: str, side: str = "buy", quantity: float = 1.0) -> DryRunTrade:
    symbol = symbol.upper().strip()
    if not symbol:
        raise ValueError("symbol is required")
    side = side.lower().strip()
    if side not in {"buy", "sell"}:
        raise ValueError("side must be buy or sell")
    if quantity <= 0:
        raise ValueError("quantity must be positive")

    return DryRunTrade(
        symbol=symbol,
        side=side,
        quantity=quantity,
        executed_at=datetime.now(timezone.utc),
    )
