contacts = {
    "Alice": "9876543210",
    "Aman": "9123456780",
    "Neha": "9988776655"
}

contacts["Rahul"] = "9012345678"

contacts["Aman"] = "9111111111"

print("Lookup existing contact:")
print("Alice:", contacts.get("Alice", "Contact not found"))

print("\nLookup non-existing contact:")
print("Riya:", contacts.get("Riya", "Contact not found"))

print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")