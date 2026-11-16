from decimal import Decimal, InvalidOperation

def total_mess_bill(filename):
    total = Decimal("0")
    report = []
    rejected = []

    with open(filename, "r", encoding="utf-8") as file:
        for line_no, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    raise ValueError("expected 3 fields")
                amount = Decimal(parts[2].strip())
                if amount < 0:
                    raise ValueError("amount cannot be negative")
                report.append(f"{parts[1].strip()} - Rs. {amount:.2f}")
                total += amount
            except (ValueError, InvalidOperation) as error:
                rejected.append((line_no, line.strip(), str(error)))

    print("\\n".join(report))
    print(f"Total: Rs. {total:.2f}")
    print("Rejected:", rejected)
    return total, rejected

if __name__ == "__main__":
    total_mess_bill("mess_oct.txt")
