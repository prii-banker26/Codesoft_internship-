# Contact Book

print("=" * 40)
print("📒 Welcome to the Contact Book 📒")
print("=" * 40)

names = []
phone_numbers = []
emails = []
addresses = []

num = 3

print("\n📥 Please enter contact details:")
for i in range(num):
    print(f"\nEnter details for contact {i+1}:")
    name = input("   👉 Name         : ")
    phone_number = input("   👉 Phone Number : ")
    email = input("   👉 Email        : ")
    address = input("   👉 Address      : ")

    names.append(name)
    phone_numbers.append(phone_number)
    emails.append(email)
    addresses.append(address)

def view_contacts():
    print("\n📇 Saved Contacts")
    print("=" * 70)
    print("Name\t\tPhone Number\t\tEmail\t\t\tAddress")
    print("-" * 70)
    for i in range(len(names)):
        print(f"{names[i]}\t\t{phone_numbers[i]}\t\t{emails[i]}\t\t{addresses[i]}")

def search_contact():
    search_term = input("\n🔍 Enter name or phone number to search: ")
    found = False
    for i in range(len(names)):
        if search_term.lower() in names[i].lower() or search_term in phone_numbers[i]:
            print("\n✅ Contact Found:")
            print(f"   📛 Name    : {names[i]}")
            print(f"   📞 Phone   : {phone_numbers[i]}")
            print(f"   📧 Email   : {emails[i]}")
            print(f"   🏠 Address : {addresses[i]}")
            found = True
            break
    if not found:
        print("❌ Contact not found.")

def update_contact():
    search_term = input("\n✏️ Enter name of contact to update: ")
    if search_term in names:
        index = names.index(search_term)

        print("\n🔄 Leave blank to keep current value.")
        new_name = input("   New Name         : ") or names[index]
        new_phone = input("   New Phone Number : ") or phone_numbers[index]
        new_email = input("   New Email        : ") or emails[index]
        new_address = input("   New Address      : ") or addresses[index]

        names[index] = new_name
        phone_numbers[index] = new_phone
        emails[index] = new_email
        addresses[index] = new_address

        print("✅ Contact updated successfully!")
    else:
        print("❌ Contact not found.")

def delete_contact():
    search_term = input("\n🗑️ Enter name of contact to delete: ")
    if search_term in names:
        index = names.index(search_term)
        del names[index]
        del phone_numbers[index]
        del emails[index]
        del addresses[index]
        print("🧹 Contact deleted successfully!")
    else:
        print("❌ Contact not found.")

while True:
    print("\n========== 📌 Contact Book Menu 📌 ==========")
    print("1️⃣  View Contacts")
    print("2️⃣  Search Contact")
    print("3️⃣  Update Contact")
    print("4️⃣  Delete Contact")
    print("5️⃣  Exit")
    print("=============================================")

    choice = input("👉 Choose an option (1-5): ")

    if choice == "1":
        view_contacts()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("\n👋 Goodbye! Thank you for using the Contact Book.")
        break
    else:
        print("❗ Invalid choice! Please enter a number between 1 and 5.")

        
