import random
from pet import Pet

def get_mood_emoji(happiness, energy, hunger):
    if happiness >= 8 and energy >= 7 and hunger <= 3:
        return "😄"
    elif hunger >= 8:
        return "🍽️"
    elif energy <= 3:
        return "😴"
    elif happiness <= 3:
        return "😢"
    else:
        return "🙂"

# Create  pet
pet_name = input("Name your digital pet: ")
my_pet = Pet(pet_name)

# Game loop
while True:
    print("\nWhat would you like to do?")
    print("1. Feed 🍗")
    print("2. Sleep 😴")
    print("3. Play 🎾")
    print("4. Train 🎓")
    print("5. Show Tricks 🧠")
    print("6. Show Status 📋")
    print("7. Exit 🚪")
    
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        my_pet.eat()
    elif choice == "2":
        my_pet.sleep()
    elif choice == "3":
        my_pet.play()
    elif choice == "4":
        trick = input("What trick do you want to teach? 🧠: ")
        my_pet.train(trick)
    elif choice == "5":
        my_pet.show_tricks()
    elif choice == "6":
        emoji = get_mood_emoji(my_pet.happiness, my_pet.energy, my_pet.hunger)
        my_pet.get_status()
        print(f"{my_pet.name}'s Mood: {emoji}")
    elif choice == "7":
        print(f"Goodbye! {my_pet.name} will miss you! 🐾")
        break
    else:
        print("Invalid choice. Try again.")

    # 🌟 Random event (just for fun!)
    if random.random() < 0.2:
        surprise = random.choice(["found a toy 🎁", "met a friend 🐕", "had a weird dream 😴", "got a little sick 🤧"])
        print(f"Random Event: {my_pet.name} {surprise}!")

