"""Read-only bounded preview of a locally downloaded public XLSX."""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile
from openpyxl import load_workbook


def inspect(path: Path, rows: int = 8, columns: int = 20) -> dict:
    if not 1 <= rows <= 30 or not 1 <= columns <= 100:
        raise ValueError("Preview bounds: rows 1..30; columns 1..100")
    if path.suffix.lower() != ".xlsx" or path.stat().st_size > 25 * 1024**2:
        raise ValueError("Expected XLSX of at most 25 MiB")
    with ZipFile(path) as archive:
        if sum(item.file_size for item in archive.infolist()) > 250 * 1024**2:
            raise ValueError("Uncompressed workbook exceeds 250 MiB")
    with path.open("rb") as stream:
        checksum = hashlib.file_digest(stream, "sha256").hexdigest()
    wb = load_workbook(path, read_only=True, data_only=False, keep_links=False)
    try:
        return {"filename": path.name, "sha256": checksum,
                "sheets": [{"name": ws.title, "max_row": ws.max_row,
                            "max_column": ws.max_column,
                            "preview": list(ws.iter_rows(min_row=1, max_row=rows,
                                                         max_col=columns, values_only=True))}
                           for ws in wb.worksheets]}
    finally:
        wb.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    parser.add_argument("--rows", type=int, default=8)
    parser.add_argument("--columns", type=int, default=20)
    args = parser.parse_args()
    print(json.dumps(inspect(args.workbook, args.rows, args.columns), default=str, indent=2))


if __name__ == "__main__":
    main()
