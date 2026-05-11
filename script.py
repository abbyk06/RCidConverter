import csv

BYTE_LENGTH = 8

def konica_to_canon(konica_decimal: int) -> int:
    le_bytes = konica_decimal.to_bytes(BYTE_LENGTH, byteorder="little", signed=False)
    result = int.from_bytes(le_bytes, byteorder="big", signed=False)
    return result

rows_out = []
fieldnames = []

with open("input.csv", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    for row in reader:
        row.pop(None, None)

        raw_primary = row.get("Primary Card Number", "").strip()

        if not raw_primary:
            print(f"  Skipping row (no primary card number): {row}")
            row["Secondary Card Number"] = ""
            rows_out.append(row)
            continue

        try:
            konica_decimal = int(raw_primary.replace(",", ""))
            print(f"\nConverting: {raw_primary}")
            canon_decimal = konica_to_canon(konica_decimal)
            row["Secondary Card Number"] = str(canon_decimal)
        except ValueError:
            print(f"  Skipped (not a number): {raw_primary}")
            row["Secondary Card Number"] = ""

        rows_out.append(row)

    fieldnames = list(reader.fieldnames)

if "Secondary Card Number" not in fieldnames:
    fieldnames.append("Secondary Card Number")

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_out)

print("\noutput.csv written successfully")