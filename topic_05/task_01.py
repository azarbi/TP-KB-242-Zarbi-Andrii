import random

user_choice = input("Enter your item (stone, scissor or paper): ").lower()
system_choice = random.choice(["stone", "scissor", "paper"])
print(f"System choice: {system_choice}")

if (user_choice == system_choice):
    print("Draw.")

#if user won
elif (user_choice == "stone" and system_choice == "scissor"):
    print("User won.")

elif (user_choice == "scissor" and system_choice == "paper"):
    print("User won.")

elif (user_choice == "paper" and system_choice == "stone"):
    print("User won.")

#if system won
elif (system_choice == "stone" and user_choice == "scissor"):
    print("System won.")

elif (system_choice == "scissor" and user_choice == "paper"):
    print("System won.")

elif (system_choice == "paper" and user_choice == "stone"):
    print("System won.")

else:
    print("Error: invalid input.")