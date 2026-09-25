import argparse
import json
import sys

from treading_auto.engine import dry_run_trade


def main() -> None:
    parser = argparse.ArgumentParser(prog="treading-auto")
    parser.add_argument("command", choices=["dry-run"])
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", default="buy", choices=["buy", "sell"])
    parser.add_argument("--quantity", type=float, default=1.0)
    args = parser.parse_args()

    if args.command == "dry-run":
        trade = dry_run_trade(args.symbol, args.side, args.quantity)
        json.dump(trade.as_dict(), sys.stdout, indent=2)
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
