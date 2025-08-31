import time

# Users database
users = {
    "peter": {
        "gender": "male",
        "age": 22,
        "drink": "yes",
    },
    "john": {
        "gender": "male",
        "age": 19,
        "drink": "no",
    },
    "jean": {
        "gender": "male",
        "age": 24,
        "drink": "yes",
    },
    "maria": {
        "gender": "female",
        "age": 22,
        "drink": "yes",
    },
    "faith": {
        "gender": "female",
        "age": 35,
        "drink": "yes",
    },
    "olga": {
        "gender": "female",
        "age": 26,
        "drink": "no",
    }
}

# Welcome and user input
name = input("What is your name: ")
print(f"Hi {name}! We will do our best to find you a match")
time.sleep(1)
print("❤️")
print("Here is what we are going to do: we will ask you some questions and based on that we will get you a match")

time.sleep(3)

# Get user preferences
user_gender = input("What is your gender (male/female): ").lower().strip()
time.sleep(1)

look_gender = input("Which gender are you looking for (male/female): ").lower().strip()
time.sleep(1)

# Get age range
min_age = int(input("What is the minimum age you're looking for: "))
max_age = int(input("What is the maximum age you're looking for: "))
time.sleep(1)

drink_quest = input("Do you drink (yes/no): ").lower().strip()
time.sleep(1)

print("Thanks for your answers!")
time.sleep(1)
print("COOKING FOR YOU...")
print("LOADING.........................")
time.sleep(3)

# Matching logic
matches = []

for username, user_info in users.items():
    # Check if the user matches the criteria
    if (user_info["gender"] == look_gender and 
        min_age <= user_info["age"] <= max_age and 
        user_info["drink"] == drink_quest):
        matches.append(username)

# Display results
print("\n" + "="*50)
if matches:
    if len(matches) == 1:
        match = matches[0]
        print(f"🎉 {match.title()} is the perfect match for you, {name}!")
    else:
        print(f"🎉 Great news {name}! We found {len(matches)} potential matches:")
        for match in matches:
            user_data = users[match]
            print(f"  • {match.title()} ({user_data['age']} years old)")
        
        print(f"\nYour top match is {matches[0].title()}!")
else:
    print(f"Sorry {name}, we couldn't find a perfect match based on your criteria.")
    print("You might want to adjust your preferences and try again!")

print("="*50)
print("Thanks for using our dating app! 💕")




