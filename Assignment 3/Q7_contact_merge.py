# Q7: Contact Merging from First Principles
import re, time

contacts_a = [
    {"name": "Dr. Ravi", "phone": "+91 98400 12345", "email": "ravi@mail.com"},
    {"name": "Anu", "phone": "9876543210", "email": ""},
]
contacts_b = [
    {"name": "ravi kumar", "phone": "9840012345", "email": "ravi.work@mail.com"},
    {"name": "Anu", "phone": "+91-9876543210", "email": "anu@mail.com"},
    {"name": "Sam", "phone": "", "email": "sam@mail.com"},
]

def normalize_phone(phone):
    digits = re.sub(r"\D", "", phone or "")
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return digits

def merge_contacts(*groups):
    merged = {}
    for contact in (c for group in groups for c in group):
        phone = normalize_phone(contact.get("phone", ""))
        email = (contact.get("email") or "").strip().lower()
        name = (contact.get("name") or "").strip()
        key = phone or email or name.lower()
        if not key:
            continue
        if key not in merged:
            merged[key] = {"name": name, "numbers": set(), "emails": set()}
        if name and not merged[key]["name"]:
            merged[key]["name"] = name
        if phone:
            merged[key]["numbers"].add(phone)
        if email:
            merged[key]["emails"].add(email)
    return list(merged.values())

result = merge_contacts(contacts_a, contacts_b)
for item in result:
    item["numbers"] = sorted(item["numbers"])
    item["emails"] = sorted(item["emails"])
print("Merged contacts:")
for item in result:
    print(item)
