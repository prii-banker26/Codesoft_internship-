# 🧮 Simple Calculator

print("=" * 40)
print("🧠 Welcome to the Simple Calculator! 🧠".center(40))
print("=" * 40)

num1 = input("🔢 Enter the first number: ")
num2 = input("🔢 Enter the second number: ")

num1 = float(num1)
num2 = float(num2)

print("\n➕ Choose an operation:")
print("1️⃣  Addition")
print("2️⃣  Subtraction")
print("3️⃣  Multiplication")
print("4️⃣  Division")

choice = input("👉 Enter your choice (1/2/3/4): ")

if choice == '1':
    result = num1 + num2
    print(f"\n✅ Result: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"\n✅ Result: {num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"\n✅ Result: {num1} × {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"\n✅ Result: {num1} ÷ {num2} = {result}")
    else:
        print("\n❌ Error: Division by zero is not allowed.")
else:
    print("\n⚠️ Invalid choice. Please enter 1, 2, 3, or 4.")

print("\n🙏 Thank you for using the calculator!")
print("=" * 40)
