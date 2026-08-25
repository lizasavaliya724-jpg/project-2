# project1.py
print("Welcome to the Interactive Personal Data Collector!\n")

# Collect user inputs
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favourite number: "))

# Display collected information
print("\nThank you! Here is the information we collected:\n")
print(f"Name : {name} {type(name)} Memory Address : {id(name)}")
print(f"Age : {age} {type(age)} Memory Address : {id(age)}")
print(f"Height : {height} {type(height)} Memory Address : {id(height)}")
print(f"Favourite Number : {fav_number} {type(fav_number)} Memory Address : {id(fav_number)}")

# Calculate birth year
birth_year = 2026 - age
print(f"\nYour birth year is approximately : {birth_year} (Based on your age {age})")

print("\nThank you for using the Personal Data Collector. Goodbye!")
