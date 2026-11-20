"""Build the synthetic Day 1 workbook; never downloads real data."""
from datetime import datetime
from pathlib import Path
from openpyxl import Workbook


def build(path: Path) -> None:
    wb = Workbook()
    wb.remove(wb.active)
    for title, data in {
        "Synthetic with tax": [
            [datetime(2024, 1, 1), 1750, 1600, 1.7, 900, 1800],
            ["2024-01-08", 1800, 0, None, None, None],
            ["bad-date", 1700, None, None, None, None],
            [datetime(2024, 1, 15), "not-a-price", -5, None, None, None],
        ],
        "Synthetic without tax": [
            [datetime(2024, 1, 1), 950, 1000, 0.9, None, None],
            ["2024-01-08", 1000, None, None, None, None],
        ],
    }.items():
        ws = wb.create_sheet(title)
        ws.append(["SYNTHETIC — not European Commission data"])
        ws.append(["Date", "IE", "DE", "IE", "IE", "XX"])
        ws.append([None, "Eurosuper 95", "Diesel", "Diesel", "Fuel oil", "Diesel"])
        ws.append([None, "EUR/1000 L", "EUR/1000 L", "EUR/L", "EUR/tonne", "EUR/1000 L"])
        for row in data:
            ws.append(row)
        ws.append(["End of synthetic fixture"])
    wb.save(path)
    wb.close()


if __name__ == "__main__":
    build(Path(__file__).with_name("synthetic_prices.xlsx"))
