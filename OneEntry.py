BYTE_LENGTH = 8

def konica_to_canon(konica_decimal: int) -> int:
    le_bytes = konica_decimal.to_bytes(BYTE_LENGTH, byteorder="little", signed=False)
    result = int.from_bytes(le_bytes, byteorder="big", signed=False)
    return result

print("Type a number and press Enter. Type 'q' to quit.\n")

while True:
    user_input = input("Konica number: ").strip()

    if user_input.lower() == "q":
        break

    try:
        konica_decimal = int(user_input.replace(",", ""))
        canon_decimal = konica_to_canon(konica_decimal)
        print(f"Canon number:  {canon_decimal}\n")
    except ValueError:
        print("  Invalid input — please enter a number.\n")