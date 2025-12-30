# User Profile Analyzer

name = input("Enter your name : ")
age = int(input("Enter your age : "))
height = float(input("Enter your height (in feet): "))

print("\n--- Profile Summary ---")
print("Name:", name)

if age < 18:
    print("Status: Minor")
else:
    print("Status: Adult")

if height >= 5.3:
    print("Height Category: Tall")
else:
    print("Height Category: Short")
