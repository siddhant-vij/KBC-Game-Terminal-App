import random
import os

lifelines = {"1": "50/50", "2": "Phone a Friend", "3": "Ask the Audience"}

correct_answers = 0

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Rome", "Paris"],
        "answer": "4",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Who wrote the Harry Potter series?",
        "options": [
            "J.K. Rowling",
            "Stephen King",
            "George R.R. Martin",
            "J.R.R. Tolkien",
        ],
        "answer": "1",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": [
            "Vincent Van Gogh",
            "Michelangelo",
            "Leonardo Da Vinci",
            "Pablo Picasso",
        ],
        "answer": "3",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Who discovered penicillin?",
        "options": [
            "Marie Curie",
            "Alexander Fleming",
            "Louis Pasteur",
            "Isaac Newton",
        ],
        "answer": "2",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Mercury", "Jupiter"],
        "answer": "1",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["K2", "Everest", "Kangchenjunga", "Lhotse"],
        "answer": "2",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Who wrote 'War and Peace'?",
        "options": [
            "Leo Tolstoy",
            "Fyodor Dostoevsky",
            "Anton Chekhov",
            "Nikolai Gogol",
        ],
        "answer": "1",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Who is the author of 'The Theory of Relativity'?",
        "options": [
            "Isaac Newton",
            "Nikola Tesla",
            "Albert Einstein",
            "Stephen Hawking",
        ],
        "answer": "3",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Which chemical element has the symbol Au?",
        "options": ["Silver", "Aluminum", "Gold", "Copper"],
        "answer": "3",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Perth", "Canberra"],
        "answer": "4",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Who composed the Four Seasons?",
        "options": [
            "Johann Sebastian Bach",
            "Wolfgang Amadeus Mozart",
            "Ludwig van Beethoven",
            "Antonio Vivaldi",
        ],
        "answer": "4",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "What is the square root of 225?",
        "options": ["15", "25", "20", "12"],
        "answer": "1",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "What is the name of the world's largest coral reef system?",
        "options": [
            "Red Sea Coral Reef",
            "New Caledonia Barrier Reef",
            "Florida Reef",
            "Great Barrier Reef",
        ],
        "answer": "4",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "In what year did World War I begin?",
        "options": ["1921", "1914", "1901", "1939"],
        "answer": "2",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "What is the distance in miles from Earth to the Moon?",
        "options": ["238,855", "120,000", "500,000", "1,000,000"],
        "answer": "1",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Who wrote the Iliad?",
        "options": ["Socrates", "Homer", "Aristotle", "Plato"],
        "answer": "2",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "What is the chemical formula for table salt?",
        "options": ["H2O", "C6H12O6", "CO2", "NaCl"],
        "answer": "4",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Which language has the most native speakers worldwide?",
        "options": ["English", "Mandarin Chinese", "Spanish", "Hindi"],
        "answer": "2",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "What is the fastest land animal?",
        "options": ["Lion", "Cheetah", "Gazelle", "Horse"],
        "answer": "2",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Which is the only planet not named after a god?",
        "options": ["Mars", "Venus", "Mercury", "Earth"],
        "answer": "4",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Which of these is not a planet in our solar system?",
        "options": ["Mars", "Jupiter", "Pluto", "Mercury"],
        "answer": "3",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Which of these rivers is the longest?",
        "options": ["Amazon", "Yangtze", "Mississippi", "Nile"],
        "answer": "4",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Who was the first president of the United States?",
        "options": [
            "George Washington",
            "Thomas Jefferson",
            "Abraham Lincoln",
            "John Adams",
        ],
        "answer": "1",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Who developed the theory of evolution?",
        "options": [
            "Isaac Newton",
            "Charles Darwin",
            "Albert Einstein",
            "Galileo Galilei",
        ],
        "answer": "2",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "What is the world's largest ocean?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "4",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Which country has the largest population in the world?",
        "options": ["India", "United States", "China", "Indonesia"],
        "answer": "3",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Which of these elements is a noble gas?",
        "options": ["Nitrogen", "Oxygen", "Argon", "Carbon"],
        "answer": "3",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Which country is the largest (by area) in the world?",
        "options": ["United States", "China", "Canada", "Russia"],
        "answer": "4",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Who is known as the Father of Computer Science?",
        "options": [
            "Charles Babbage",
            "Alan Turing",
            "John von Neumann",
            "Ada Lovelace",
        ],
        "answer": "2",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "In which year did man first walk on the moon?",
        "options": ["1972", "1965", "1969", "1970"],
        "answer": "3",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Who is the all-time leading scorer in NBA history?",
        "options": [
            "Michael Jordan",
            "LeBron James",
            "Kareem Abdul-Jabbar",
            "Kobe Bryant",
        ],
        "answer": "3",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Which book series is the best-selling of all time?",
        "options": [
            "Harry Potter",
            "The Lord of the Rings",
            "A Song of Ice and Fire",
            "The Twilight Saga",
        ],
        "answer": "1",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Who was the ancient Egyptian queen who had a love affair with Julius Caesar?",
        "options": ["Nefertiti", "Cleopatra", "Hatshepsut", "Ankhesenamun"],
        "answer": "2",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Which planet in our solar system has the most moons?",
        "options": ["Saturn", "Jupiter", "Uranus", "Mars"],
        "answer": "1",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Won", "Yen", "Ruble", "Rupee"],
        "answer": "2",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Which composer wrote The Magic Flute?",
        "options": [
            "Wolfgang Amadeus Mozart",
            "Johann Sebastian Bach",
            "Ludwig van Beethoven",
            "Franz Schubert",
        ],
        "answer": "1",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "What is the capital of Canada?",
        "options": ["Toronto", "Montreal", "Ottawa", "Vancouver"],
        "answer": "3",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "What is the primary ingredient in hummus?",
        "options": ["Lentils", "Chickpeas", "Black Beans", "Almonds"],
        "answer": "2",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "In what country would you find the Great Pyramids of Giza?",
        "options": ["Greece", "Egypt", "Mexico", "China"],
        "answer": "2",
        "visible_options": [1, 2, 3, 4],
    },
    {
        "question": "Who was the Greek god of war?",
        "options": ["Ares", "Apollo", "Zeus", "Hermes"],
        "answer": "1",
        "visible_options": [1, 2, 3, 4],
    },
]

questions = random.sample(questions, 20)

winnings = [
    1000,
    2000,
    3000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,
    320000,
    640000,
    1250000,
    2500000,
    5000000,
    10000000,
    20000000,
    30000000,
    40000000,
    50000000,
    100000000,
]


def shuffle_options_and_update_answer(question):
    options_with_indices = list(enumerate(question["options"], start=1))
    random.shuffle(options_with_indices)
    question["options"] = [option for _, option in options_with_indices]
    question["visible_options"] = list(range(1, len(question["options"]) + 1))

    for i, (index, option) in enumerate(options_with_indices):
        if index == int(question["answer"]):
            question["answer"] = i + 1
            break


def display_question_and_options(question):
    print(question["question"])
    for i in question["visible_options"]:
        print(f"{i}. {question['options'][i-1]}")
    print("\n")


def valid_input_for_lifeline(question, question_num):
    while True:
        user_input = input("Choose your option: ")
        if user_input.lower() == "quit":
            calculate_winnings(question_num)
            quit_game()
        elif (
            user_input.isdigit()
            and int(user_input) in question["visible_options"]
        ):
            return user_input
        else:
            print("Invalid input! Please try again")


def lifeline_50_50(question, question_num):
    incorrect_options = list(
        set(question["visible_options"]) - set([question["answer"]]))
    removed_options = random.sample(
        incorrect_options, min(2, len(incorrect_options)))
    for option in removed_options:
        question["visible_options"].remove(option)

    display_question_and_options(question)
    return valid_input_for_lifeline(question, question_num)


def lifeline_phone_a_friend(question, question_num):
    suggested_option = random.choice(question["options"])
    print(f"A friend suggests: {suggested_option}")

    display_question_and_options(question)
    return valid_input_for_lifeline(question, question_num)


def lifeline_ask_the_audience(question, question_num):
    suggested_option = random.choice(question["options"])
    print(f"The audience suggests: {suggested_option}")

    display_question_and_options(question)
    return valid_input_for_lifeline(question, question_num)


def check_answer(user_input, question, question_num):
    global correct_answers
    if int(user_input) == question["answer"]:
        print("That's correct!")
        correct_answers += 1
    else:
        print("That's incorrect!")
        print(
            "The correct answer was: "
            + question["options"][question["answer"] - 1]
        )
        calculate_winnings(question_num)
        quit_game()


def handle_lifeline(question, question_num):
    if len(lifelines) == 0:
        print("Sorry, you have used all your lifelines!")
        return input("Choose your option: ")

    print("Lifelines:")
    for num, name in lifelines.items():
        print(f"{num}: {name}")
    lifeline = input("Choose a lifeline or type 'quit' to quit the game: ")

    if lifeline == "quit":
        calculate_winnings(question_num)
        quit_game()
    elif lifeline not in lifelines:
        print("Sorry, that's not a valid lifeline!")
        return handle_lifeline(question, question_num)
    else:
        del lifelines[lifeline]
        if lifeline == "1":
            return lifeline_50_50(question, question_num)
        elif lifeline == "2":
            return lifeline_phone_a_friend(question, question_num)
        elif lifeline == "3":
            return lifeline_ask_the_audience(question, question_num)


def calculate_winnings(question_num):
    global correct_answers
    if question_num < 5:
        winning = 0
    elif question_num < 10:
        winning = 10000
    elif question_num < 15:
        winning = 320000
    else:
        winning = 10000000
    print(
        f"You answered {correct_answers} questions correctly. Your total winnings are: {winning}"
    )


def handle_user_input(question, question_num):
    user_input = input(
        "Choose your option or type 'lifeline' to use a lifeline: ")

    if isinstance(user_input, str):
        if user_input.lower() == "quit":
            calculate_winnings(question_num)
            quit_game()
        elif user_input.lower() == "lifeline":
            user_input = handle_lifeline(question, question_num)
            check_answer(user_input, question, question_num)
        elif user_input in ["1", "2", "3", "4"]:
            check_answer(user_input, question, question_num)
        else:
            print("Invalid input! Please try again.")
            handle_user_input(question, question_num)
    else:
        print("Invalid input! Please try again.")
        handle_user_input(question, question_num)


def instructions():
    print("\nInstructions:")
    print("You will be given a series of questions.")
    print("Each question will have four options, only one of which is correct.")
    print("Enter the number corresponding to your choice.")
    print("You can quit the game anytime by typing 'quit'.")
    print("Type 'lifeline' to use a lifeline.")


def start_game():
    print("Welcome to the Game!")
    print("1. Start Game")
    print("2. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        play_game()
    elif choice == "2":
        quit_game()
    else:
        print("Invalid choice. Please try again.")
        start_game()


def play_game():
    instructions()
    question_num = 0
    global correct_answers
    random.shuffle(questions)
    for question in questions:
        os.system("clear")
        shuffle_options_and_update_answer(question)
        display_question_and_options(question)
        handle_user_input(question, question_num)
        question_num += 1
    if question_num == len(questions):
        print(
            f"Congratulations! You've answered all questions correctly. Your total winnings are: {winnings[-1]}"
        )


def quit_game():
    print("Thank you for playing. Goodbye!")
    exit()  # This line terminates the program


start_game()
