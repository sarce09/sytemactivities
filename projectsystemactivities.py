import random

PUPPY_NAMES = [
    "Buddy", "Bella", "Max", "Luna", "Charlie", "Daisy", "Rocky", "Milo", "Lucy", "Bailey",
    "Cooper", "Sadie", "Tucker", "Molly", "Bear", "Zoey", "Duke", "Lola", "Oliver", "Rosie",
    "Leo", "Ruby", "Jack", "Penny", "Finn", "Nala", "Winston", "Roxy", "Bentley", "Coco",
    "Oscar", "Willow", "Murphy", "Hazel", "Buster", "Ivy", "Louie", "Stella", "Henry", "Olive",
    "Zeus", "Peaches", "Theo", "Honey", "Bruno", "Maple", "Ace", "Cleo", "Jasper", "Piper",
    "Shadow", "Ginger", "Apollo", "Mocha", "Scout", "Sasha", "Blue", "Maggie", "Remy", "Millie",
    "Ollie", "Nova", "Ranger", "Freya", "Simba", "Chloe", "Boomer", "Annie", "Atlas", "Minnie",
    "Arlo", "Skye", "Cash", "Elsie", "Diesel", "Harper", "Koda", "Juniper", "Bandit", "Marley",
    "Thor", "Sunny", "Hank", "Bonnie", "Prince", "Autumn", "Ziggy", "Layla", "George", "Tilly",
    "Echo", "Blossom", "Dexter", "Pearl", "Rufus", "Snowy", "Axel", "Poppy", "Bruce", "Lily",
    "Cosmo", "Bean", "Moose", "Dolly", "Rocket", "Fiona", "Nico", "Waffles", "Benny", "Pumpkin",
    "Otis", "Sienna", "Alfie", "Mabel", "Monty", "Birdie", "Rowan", "Cinnamon", "Frankie", "Toffee",
    "Percy", "Clover", "Yoshi", "Bluebell", "Samson", "Cupcake", "Basil", "Sprout", "Noodle", "Pebbles",
]

USED_PUPPY_NAMES = set()

CAPITALS_POOL = [
    ("Argentina", "Buenos Aires"),
    ("Australia", "Canberra"),
    ("Austria", "Vienna"),
    ("Belgium", "Brussels"),
    ("Brazil", "Brasilia"),
    ("Canada", "Ottawa"),
    ("Chile", "Santiago"),
    ("China", "Beijing"),
    ("Colombia", "Bogota"),
    ("Costa Rica", "San Jose"),
    ("Croatia", "Zagreb"),
    ("Cuba", "Havana"),
    ("Czech Republic", "Prague"),
    ("Denmark", "Copenhagen"),
    ("Dominican Republic", "Santo Domingo"),
    ("Egypt", "Cairo"),
    ("Finland", "Helsinki"),
    ("France", "Paris"),
    ("Germany", "Berlin"),
    ("Greece", "Athens"),
    ("Hungary", "Budapest"),
    ("Iceland", "Reykjavik"),
    ("India", "New Delhi"),
    ("Indonesia", "Jakarta"),
    ("Ireland", "Dublin"),
    ("Israel", "Jerusalem"),
    ("Italy", "Rome"),
    ("Japan", "Tokyo"),
    ("Kenya", "Nairobi"),
    ("Malaysia", "Kuala Lumpur"),
    ("Mexico", "Mexico City"),
    ("Morocco", "Rabat"),
    ("Netherlands", "Amsterdam"),
    ("New Zealand", "Wellington"),
    ("Norway", "Oslo"),
    ("Peru", "Lima"),
    ("Philippines", "Manila"),
    ("Poland", "Warsaw"),
    ("Portugal", "Lisbon"),
    ("Romania", "Bucharest"),
    ("Saudi Arabia", "Riyadh"),
    ("Singapore", "Singapore"),
    ("South Africa", "Pretoria"),
    ("South Korea", "Seoul"),
    ("Spain", "Madrid"),
    ("Sweden", "Stockholm"),
    ("Switzerland", "Bern"),
    ("Thailand", "Bangkok"),
    ("Turkey", "Ankara"),
    ("England", "London"),
]

OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def ask_float(prompt: str) -> float:
    while True:
        raw_value = input(prompt).strip()
        try:
            return float(raw_value)
        except ValueError:
            print("Invalid input. Please enter a numeric value and try again.")


def ask_yes_no(prompt: str) -> str:
    while True:
        response = input(prompt).strip().lower()
        if response in {"yes", "no"}:
            return response
        print("Please answer with 'yes' or 'no'.")


def run_calculator() -> None:
    print("Welcome to the Calculator!")
    first_number = ask_float("Enter a number: ")
    second_number = ask_float("Enter another number: ")

    while True:
        operation = input("Enter an operation (+, -, *, /): ").strip()
        if operation not in OPERATIONS:
            print("Invalid operation. Please enter one of the following: +, -, *, /.")
            continue

        if operation == "/" and second_number == 0:
            print("Error: Division by zero is not allowed.")
            second_number = ask_float("Enter another number (not 0): ")
            continue
        break

    result = OPERATIONS[operation](first_number, second_number)
    print(f"The result of {first_number} {operation} {second_number} is: {result}")
    print("Nice work using the calculator!")


def run_capitals_quiz() -> None:
    print("Welcome to the Capitals Quiz!")
    score = 0
    quiz_questions = random.sample(CAPITALS_POOL, 10)

    for country, capital in quiz_questions:
        answer = input(f"What is the capital of {country}? ").strip().lower()
        if answer == capital.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {capital}.")

    print(f"Your final score is: {score} / {len(quiz_questions)}")
    print("Thanks for playing the Capitals Quiz!")


def run_puppy_name_generator() -> None:
    print("Welcome to the Puppy Name Generator!")
    while True:
        remaining_names = [name for name in PUPPY_NAMES if name not in USED_PUPPY_NAMES]
        if not remaining_names:
            print("All puppy names have already been used.")
            print("Thanks for using the Puppy Name Generator!")
            return

        generated_name = random.choice(remaining_names)
        USED_PUPPY_NAMES.add(generated_name)
        print("Your randomly generated puppy name is:", generated_name)
        like = ask_yes_no("Do you like the name? (yes/no) ")
        if like == "yes":
            print("Great! I'm glad you like the name.")
            break
        print("No worries! Let's generate another name for you.")

    print("Thanks for using the Puppy Name Generator!")


def run_activity(activity: str) -> None:
    if activity == "1":
        run_calculator()
    elif activity == "2":
        run_capitals_quiz()
    else:
        run_puppy_name_generator()


def ask_activity() -> str:
    while True:
        activity = input(
            "What activity would you like to do? (1. Calculator, 2. Capitals Quiz, 3. Puppy Name Generator): "
        ).strip()
        if activity in {"1", "2", "3"}:
            return activity
        print("Invalid activity. Please choose 1, 2, or 3.")


def main() -> None:
    username = input("Enter username: ")
    print("Welcome to the system", username)

    while True:
        activity = ask_activity()
        run_activity(activity)

        new_activity = ask_yes_no("Would you like to try another activity? (yes/no) ")
        if new_activity == "no":
            print("Thank you for using the system. Goodbye!")
            break


if __name__ == "__main__":
    main()