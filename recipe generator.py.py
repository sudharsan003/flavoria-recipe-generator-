import random
import datetime

filename = "recipes.txt"

def load_recipes():
    recipes = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, ingredients = line.strip().split(":", 1)
                recipes[name] = ingredients
    except FileNotFoundError:
        pass
    return recipes

def save_recipes():
    with open(filename, "w") as file:
        for name, ingredients in recipes.items():
            file.write(f"{name}:{ingredients}\n")

recipes = load_recipes()

def add(name, ingredients):
    recipes[name] = ingredients
    save_recipes()
    print(f"Recipe '{name}' added successfully!")

def update(name, ingredients):
    if name in recipes:
        recipes[name] = ingredients
        save_recipes()
        print(f"Recipe '{name}' updated successfully!")
    else:
        print(f"'{name}' not found in recipes. Consider adding it instead.")

def remove(name):
    if name in recipes:
        del recipes[name]
        save_recipes()
        print(f"Recipe '{name}' removed successfully!")
    else:
        print(f"'{name}' not found in recipes.")


actions = ["add", "adding", "added"]
updating = ["update", "updated", "change dish"]
random_selection = ["random", "random food", "recipe to cook"]
view_all = ["all", "view all", "view recipes", "view available"]
words = ["hello", "hi", "hey", "good morning", "good evening"]
low = ["sad", "unhappy"]
high = ["happy", "peace"]
slow = ["bad", "worst", "negative"]
removal = ["remove", "delete", "erase"]

what = ["who are you", "what can you do for me", "what are you"]
appreciation = ["thank you", "thanks"]
jokes = ["joke", "funny", "tell me a joke"]
suggestions = ["suggest", "suggestions"]
help_words = ["help", "assist"]
favorites = ["favorite", "best recipe"]
tips = ["tips", "cooking tips"]
motivation = ["motivate", "inspire me"]
weather = ["weather", "today's weather"]
ingredient_list = ["ingredients", "list ingredients"]
exit_words = ["exit", "quit", "stop"]

time_words = ["time", "exact time"]
exact = ["date and time", "time and date"]
year = ["year", "current year"]
day = ["day", "what day", "today day"]
date = ["date", "today date"]

while True:
    choice = input("--> ").strip().lower()

    if choice in actions:
        name = input("Enter dish name: ").strip()
        ingredients = input("Enter ingredients: ").strip()
        add(name, ingredients)

    elif choice in updating:
        name = input("Enter dish name: ").strip()
        ingredients = input("Enter new ingredients: ").strip()
        update(name, ingredients)

    elif choice in random_selection:
        if recipes:
            selected_dish = random.choice(list(recipes.keys()))
            print(f"Try cooking: {selected_dish}\nIngredients: {recipes[selected_dish]}")
        else:
            print("No recipes available.")

    elif choice in view_all:
        if recipes:
            print("Available recipes:")
            for dish, description in recipes.items():
                print(f"- {dish}: {description}")
        else:
            print("No recipes stored.")

    elif choice in words:
        print("Hi, I'm Flavoria... Which dish would you like to know about?")

    elif choice in high:
        print("Great to hear! Keep going.")

    elif choice in low:
        print("Why are you sad, my friend? I'm here to help you.")

    elif choice in slow:
        print("When things go bad, you're just stepping up to the next level.")

    elif choice in removal:
        name = input("Enter dish name to remove: ").strip()
        remove(name)

    elif choice in what:
        print("I am a recipe generator chatbot.")

    elif choice in appreciation:
        print("You're very welcome! Happy cooking!")

    elif choice in jokes:
        print("Why did the tomato turn red? Because it saw the salad dressing!")

    elif choice in suggestions:
        print("How about trying a pasta dish or a spicy stir-fry today?")

    elif choice in help_words:
        print("I can suggest recipes, store them, update them, and even cheer you up!")

    elif choice in favorites:
        if recipes:
            print(f"My favorite recipe is {random.choice(list(recipes.keys()))}, give it a try!")
        else:
            print("No favorite recipe yet!")

    elif choice in tips:
        print("Cooking tip: Always taste as you go, and never underestimate the power of fresh herbs!")

    elif choice in motivation:
        print("Cooking is an art—every mistake is just a step towards your masterpiece!")

    elif choice in weather:
        print("I don't check the weather, but I always say it's a great day for cooking!")

    elif choice in time_words:
        x = datetime.datetime.now()
        print(x.strftime("%X"))

    elif choice in exact:
        x = datetime.datetime.now()
        print(x.strftime("%c"))

    elif choice in year:
        x = datetime.datetime.now()
        print(x.year)

    elif choice in day:
        x = datetime.datetime.now()
        print(x.strftime("%A"))

    elif choice in date:
        x = datetime.datetime.now()
        print(x.strftime("%x"))

    elif choice in ingredient_list:
        name = input("Enter the dish name: ").strip()
        if name in recipes:
            print(f"Ingredients for '{name}': {recipes[name]}")
        else:
            print(f"'{name}' not found in recipes.")

    elif choice in exit_words:
        print("Had a great conversation with you, thank you!")
        break

    else:
        print("Sorry... I'm a recipe generator, and your input is beyond my knowledge.")
