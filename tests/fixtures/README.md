# Synthetic fixture

`synthetic_prices.xlsx` is invented, not EC data or a replica of its actual layout. It deliberately uses a wide, multi-row header with tax basis separated by sheet and native Excel dates as well as strings. No live observations are represented.

`build_fixture.py` recreates the logical workbook with openpyxl. XLSX metadata/ZIP bytes may differ across generations; assertions compare values, not byte hashes. `expected.json` specifies one candidate cell per nonblank price/date position (including invalid nonblank prices). Sheet labels and column names are provisional fixture-only.
