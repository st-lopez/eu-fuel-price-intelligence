# Data contract (canonical, provisional source adapter)

Candidate grain: one nonblank price cell on an observation row, retaining source file hash, sheet name and cell coordinate. Out-of-scope product/aggregate cells counted separately. Blank price cells counted separately, never coerced to zero. Structural headers/footer excluded. Candidate count in fixture manifest includes out-of-scope cells; eligible = candidate minus out-of-scope, then eligible = accepted + rejected.

| Field | Type and rule |
|---|---|
| observation_date | Date; native Excel date or strict ISO date; no inferred missing dates |
| country_code | ISO alpha-2 in verified national mapping; unknown rejected; aggregate excluded |
| product_code | PETROL_95 or DIESEL; known other fuel out-of-scope; unknown rejected |
| tax_basis | WITH_TAX or WITHOUT_TAX; explicit source sheet mapping |
| original_value | Finite positive Decimal; missing excluded, malformed/zero/negative rejected |
| original_unit | EUR/1000 L or EUR/L in scope; other units rejected for in-scope products |
| price_eur_per_litre | Decimal; EUR/1000 L divided by 1000, EUR/L unchanged |
| source_hash, source_sheet, source_cell | SHA-256 hex and original workbook location |

No density-based conversion from mass to volume. Same country/product/date/tax basis must be unique; duplicates and revisions addressed before DB write. Tax component = with-tax minus without-tax for matching key (not a tax rate or independently reported duty); percentage of retail price = component / with-tax * 100, only for valid paired data. Do not fill missing pairs. For example, invented 1750 EUR/1000 L = 1.750 EUR/L and 950 EUR/1000 L = 0.950 EUR/L; difference 0.800 EUR/L.

Synthetic workbook: two sheets, four header rows, 6 observation rows total, 5 price columns, 14 nonblank candidates (1 known out-of-scope fuel oil, 8 accepted, 5 rejected: unknown country, zero, invalid date, malformed price, negative price); 16 blanks. Actual EC schema still unknown; no parser implemented in Day 1.
