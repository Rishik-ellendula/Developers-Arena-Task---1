print("======================================")
print("      PERSONAL INFORMATION MANAGER     ")
print("======================================\n")

name = input("Enter your full name: ").strip().title()

age_input = input("Enter your age: ").strip()
if age_input.isdigit():
    age = int(age_input)
else:
    print("Invalid age! Setting age to 0.")
    age = 0

city = input("Enter your city: ").strip().title()

hobbies_raw = input("Enter your hobbies (comma-separated): ").strip()

hobbies_list = [h.strip().capitalize() for h in hobbies_raw.split(",") if h.strip()]

hobbies_final = " | ".join(hobbies_list) if hobbies_list else "No hobbies added"

if age < 13:
    age_group = "Child"
elif 13 <= age < 18:
    age_group = "Teenager"
elif 18 <= age < 45:
    age_group = "Young Adult"
elif 45 <= age < 60:
    age_group = "Adult"
else:
    age_group = "Senior Citizen"

if len(name) <= 4:
    greet = f"Hi {name}!"
else:
    greet = f"Hello {name}!"
print("\n======================================")
print("              YOUR PROFILE             ")
print("======================================")

print(f"Name       : {name}")
print(f"Age        : {age} ({age_group})")
print(f"City       : {city}")
print(f"Hobbies    : {hobbies_final}")

print("======================================")

print("\n✨ Personalized Message ✨")
if age < 18:
    print(f"{greet} You're young and full of potential! Keep learning and exploring 😊")
elif 18 <= age < 40:
    print(f"{greet} You're in the most productive phase — keep pushing forward 🚀")
else:
    print(f"{greet} Your experience is your strength. Keep inspiring others 🌟")
