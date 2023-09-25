import random


# Define lifelines and their finction
def fifty_fifty(options, correct_answer):
    wrong_options = [opt for opt in options if opt != correct_answer]
    random.shuffle(wrong_options)
    two_wrong_options = random.sample(wrong_options, 2)
    remaining_options = [opt for opt in options if opt not in two_wrong_options]
    return remaining_options

def phone_a_friend(question_data):
    print("You decided to use the Phone-a-Friend lifeline.")
    print("Your friend suggests the answer is:", question_data["answer"])


# Get the user's name
user_name = input("Welcome to KBC! Please enter your name: ")


# Define a list of questions, answers and price amounts for each levels.
level1_questions = [
    {
        "question": "On Which Day Is World Elephant Day Celebrated?",
        "options": ["A. August 9th", "B. August 10th", "C. August 11th", "D. August 12th"],
        "answer": "D",
        "price": 1000
    },
     {
        "question": "Which State Launched India's First Agricultural Data Exchange?",
        "options": ["A. Maharashtra", "B. Telangana", "C. Punjab", "D. Karnataka"],
        "answer": "B",
        "price": 2000
    },
     {
        "question": "Where Was The India Startup Festival 2023 Held?",
        "options": ["A. Mumbai", "B. Hyderabad", "C. Bangalore", "D. Chennai"],
        "answer": "C",
        "price": 3000
    },
     {
        "question": "Who Won The Lifetime Achievement Award At RICS South Asia Awards In August 2023?",
        "options": ["A. Sundar Pichai", "B. Mukesh Ambani", "C. Subhash Runwal", "D. Adi Godrej"],
        "answer": "C",
        "price": 5000
    },
     {
        "question": "Who Was Honored With The Strong Women Icon Award By The UK House Of Lords?",
        "options": ["A. Mayra Grover", "B. Aishwarya Rai", "C. Indira Nooyi", "D. Malala Yousafzai"],
        "answer": "A",
        "price": 10000
    }
    
]

level2_questions = [
    {
        "question": "What Is The Rank Of India In The Internet Resilience Index?",
        "options": ["A. First", "B. Second", "C. Fifth", "D. Sixth"],
        "answer": "D",
        "price": 20000
    },
    {
        "question": "Who Is The Asian Celebrity With The Highest Earnings, According To Hopper Headquarters In August 2023?",
        "options": ["A. Shah Rukh Khan", "B. Aamir Khan", "C. Salman Khan", "D. Virat Kohli"],
        "answer": "D",
        "price": 40000
    },
    {
        "question": "In The World Athletics Championship, Who Will Lead The Indian Team?",
        "options": ["A. Neeraj Chopra", "B. Neeraj Chopra", "C. P. V. Sindhu", "D.P. V. Sindhu"],
        "answer": "A",
        "price": 80000
    },
    {
        "question": "Which Of These Battles Took Place Last?",
        "options": ["A. First Battle Of Panipat", "B. Battle Of Haldighati", "C. Battle Of Chausa", "D. Battle Of Saraighat"],
        "answer": "D",
        "price": 160000
    },
    {
        "question": "Bleaching Powder Is A Compound Of Which Chemical Element?",
        "options": ["A. Sodium", "B. Potassium", "C. Potassium", "D. v"],
        "answer": "C",
        "price": 320000
    }
]

level3_questions = [
    {
        "question": "Which Of These States Does Not Border Maharashtra?",
        "options": ["A. Gujarat", "B. Andhra Pradesh", "C. Chhattisgarh", "D. Karnataka"],
        "answer": "B",
        "price": 640000
    },
    {
        "question": "Which Of These Colors Was Not Used To Mark The Safety Of A Zone During COVID-19 In India?",
        "options": ["A. Red", "B. Green", "C. Orange", "D. Blue"],
        "answer": "D",
        "price": 1250000
    },
    {
        "question": "Who Among The Following Was The First Resident At The Shaniwar Wada In Pune?",
        "options": ["A. Peshwa Baji Rao I", "B. Peshwa Balaji Vishwanath", "C. Nanasaheb Peshwa", "D. Nanasaheb Peshwa"],
        "answer": "A",
        "price": 2500000
    },
    {
        "question": "Out Of The Shaddarsanas (Six Systems) Of Hindu Philosophy, If Sankhya, Nyaya, Vaishehika, Mimamsa And Vedantaare Five, Which Is The Sixth?",
        "options": ["A. Jyotish", "B. Natya", "C. Dharma", "D. Yoga"],
        "answer": "D",
        "price": 5000000
    },
    {
        "question": "If The P In The Pincode Of A Place Stands For Postal Then What Does The P In The PIN Of ATM Banking Stand For?",
        "options": ["A. Population", "B. Personal", "C. Personal", "D. Permanent"],
        "answer": "B",
        "price": 10000000
    }
]

# Function to display questions, get user's choice, and update the score.
def ask_question(question_data, current_prize):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)

    while True:
        user_choice = input("Enter your answer (A/B/C/D) or use a lifeline (F for 50-50, P for Phone-a-Friend): ").upper()
        if user_choice in ["A", "B", "C", "D"]:
            if user_choice == question_data["answer"]:
                print(f"Correct answer! You won ${current_prize}")
                return True
            else:
                print("Wrong answer! The correct answer is", question_data["answer"])
                return False
        elif user_choice == "F":
            if "50-50"  not in question_data:
                question_data["50-50"] = True
                remaining_options = fifty_fifty(question_data["options"], question_data["answer"])
                print("50-50 lifeline: The remaining options are:", remaining_options)
            else:
                print("You have already used the 50-50 lifeline for this question.")
                break
        elif user_choice == "P":
            if "Phone-a-friend" not in question_data:
                question_data["Phone-a-Friend"] = True
                phone_a_friend(question_data)
            else:
                print("You have already used the Phone-a-Friend lifeline for this question.")
                break
        else:
            print("Invalid choice! Please enter A, B, C, D, F for 50-50, or P for Phone-a-Friend.")

# Function to play specific level of the game.
def play_level(level, level_questions):
    score = 0
    print(f"\nlevel {level} - {user_name}, let's begin!")

    for i, question_data in enumerate(level1_questions):
        current_prize = question_data["price"]
        if ask_question(question_data, current_prize):
            score += current_prize 
            if i < len(level_questions):
                print("Your total prize money so far is ${}".format(score))
            else:
                print(f"Congratulations, {user_name}! you have completed level {level} and won ${score}")
        else:
            print(f"Game Over, {user_name}! You won ${score}.")          

# Main game loop
def main():
    print(f"Hello, {user_name}! Let's play KBC.")

    play_level(1, level1_questions)
    play_level(2, level2_questions)
    play_level(3, level3_questions)

    print(f"Congratulaion, {user_name}! you have completed all the levels!")

if __name__ == "__main__":
    main()    

         