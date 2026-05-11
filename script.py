import csv

BYTE_LENGTH = 16 # Konica cards are 16 bytes (128-bit)

def konica_to_canon(konica_decimal: int) -> int:
    # Decimal → little-endian (16 bytes)
    le_bytes = konica_decimal.to_bytes(BYTE_LENGTH, byteorder="little", signed=False)

    # Little endian → Big endian
    be_bytes = le_bytes[::-1]

    # Big endian → Decimal
    return int.from_bytes(be_bytes, byteorder="big", signed=False)

rows_out = []

with open("input.csv", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    for row in reader:
        raw_primary = row.get("Primary Card Number", "").strip()

        if raw_primary:
            # Remove commas and whitespace just in case
            cleaned = raw_primary.replace(",", "").strip()
            try:
                konica_decimal = int(cleaned)
                canon_decimal = konica_to_canon(konica_decimal)
                row["Secondary Card Number"] = str(canon_decimal)
            except ValueError:
                # Leave secondary blank if conversion fails
                row["Secondary Card Number"] = ""
        else:
            row["Secondary Card Number"] = ""

            rows_out.append(row)

# Ensure output header includes the secondary column
fieldnames = list(reader.fieldnames)
if "Secondary Card Number" not in fieldnames:
    fieldnames.append("Secondary Card Number")

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_out)

print("output.csv written successfully")