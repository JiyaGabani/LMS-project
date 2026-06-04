#collection mainipulator

print("welcom to Interactive Personal Data Collection program")

name=input("please enter your name:")
age=int(input("please enter your age:"))
height=float(input("please enter your height:"))
favourite=int(input("please enter your favourite number:"))

print("\nThank you! for your information.")
print("here is your information we collect")
print("\n")
print(f"Name: {name}(Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age}(Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height}(Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite: {favourite}(Tyoe: {type(favourite)}, Memory Address: {id(favourite)})")

birth_year= 2026 - age

print(f"your birth year is approximately ({birth_year}(based on your age of{age}))")
print("\n")
print("Thank you for using the personal Data collector. Goodbye!")
