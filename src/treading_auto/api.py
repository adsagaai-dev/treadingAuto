from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from treading_auto.engine import dry_run_trade

app = FastAPI(title="treadingAuto API", version="0.1.0")


class DryRunRequest(BaseModel):
    symbol: str = Field(..., min_length=1)
    side: str = Field(default="buy")
    quantity: float = Field(default=1.0, gt=0)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/trades/dry-run")
def trades_dry_run(body: DryRunRequest) -> dict:
    try:
        trade = dry_run_trade(body.symbol, body.side, body.quantity)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return trade.as_dict()
