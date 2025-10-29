import tkinter as tk
import random # This is the built-in module that allows you to generate random numbers

# It makes the main application window
root = tk.Tk()
root.title("Math Quiz")
root.geometry("500x450")
root.config(bg="#add8e6")

# The stat line to track the game scores
score = 0        # Players score
question_num = 1 # Question Number
difficulty= 1    # The difficulty level from Easy, Moderate, and Advanced
num1 = 0         # First number in the math quiz
num2 = 0         # Second number for the quiz   
op = ""          # operations like + -
entry_answer = None # Reference to the answer entry widget

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def displayMenu():
    global score, question_num
    clear_screen()
    # Resets the game stats
    score = 0
    question_num = 1 
    
    # Creates the display title label
    lbl_title  = tk.Label(root, text="MATH QUIZ \nCHOOSE A DIFFICULTY LEVEL",
                         font=("Arial", 20), bg="#add8e6", fg="white")
    lbl_title .pack(pady=20)
         
    # Creates the difficulty button section and starts the quiz with the appropriate level
    tk.Button(root, text="EASY", width=15, command=lambda: start_quiz(1),
              bg="#8690c2", fg="white").pack(pady=10)
    tk.Button(root, text="MODERATE", width=15, command=lambda: start_quiz(2),
              bg="#8690c2", fg="white").pack(pady=10)
    tk.Button(root, text="ADVANCED", width=15, command=lambda: start_quiz(3),
              bg="#8690c2", fg="white").pack(pady=10)
    
def randomInt(difficulty):
    # If difficulty is 1 (Easy) it returns the number between 0-99
    if difficulty == 1:
        return random.randint(0,99)
    # If difficulty is 2 (Moderate) it returns the number between 100-999
    elif difficulty == 2:
        return random.randint(100,999)
    # If difficulty is 3 (Advanced) it returns the number between 1000-9999
    else: 
        return random.randint(1000, 9999)
    
# It randomly chooses if it is either add (+) or subtract (-) for the operation    
def decideOperation():
    return random.choice(['+', '-'])    
    
def start_quiz(level):
    global difficulty
    difficulty = level 
    ask_question()
    
def ask_question():
    global num1, num2, op, entry_answer, question_num

    clear_screen()

    # Checks if the quiz has ended after 10 questions
    if question_num > 10:
        displayResults()
        return
    
    # Generates random numbers and operation for the question
    num1 = randomInt(difficulty) # Generates the first number based on difficulty
    num2 = randomInt(difficulty) # Generates the second number
    op = decideOperation() # Randomly chooses + or - 
    
    lbl_q = tk.Label(root, text=f"Question {question_num} of 10",
                     font=("Arial", 18), bg="#add8e6", fg="white")
    lbl_q.pack(pady=10)
    
    # Displays the math problem
    lbl_problem = tk.Label(root, text=f"{num1} {op} {num2} = ?",
                     font=("Arial", 28, "bold"), bg="#add8e6", fg="white")
    lbl_problem.pack(pady=20)
    
    # Creates the input field for the user's answer 
    entry_answer = tk.Entry(root, font=("Arial", 18), justify="center")
    entry_answer.pack(pady=10) # Sets focus to the entry field for immediate typing
    
    # Submit button to check the answer
    tk.Button(root, text="Submit Answer",
             command=check_answer,
             bg="#8690c2", fg="white", width=15).pack(pady=10)
    
def check_answer():
    global score, question_num

    try:
        user_answer = int(entry_answer.get())
    except ValueError:
        tk.Label(root, text="Enter a valid number!!!",
                 font=("Arial", 14), bg="#add8e6", fg="red").pack(pady=5)
        return
    
    # It calculates the correct answer based on the operation 
    correct_answer = num1 + num2 if op == '+' else num1 - num2 
    
    if user_answer == correct_answer:
        score += 10 # It adds 10 points for the correct answer 
        feedback = "KACHING CORRECT WONDERFUL"
        color = "green"
    else: 
        feedback = f"BUM INCORRECT! \nCorrect Answer is: {correct_answer}"
        color = "red"
      
    # Display feedback to user
    tk.Label(root, text=feedback, 
             font=("Arial", 16), bg="#add8e6", fg=color).pack(pady=10)
    # Makes it move to the next question
    question_num += 1 
    
    # The button to proceed to the next question 
    tk.Button(root, text="Next Question",
              command=ask_question,
              bg="#8690C2", fg="white", width=15).pack(pady=10)    
             
def displayResults():
    clear_screen()
    
    # Displays the final score 
    tk.Label(root, text=f"Your final score is: {score}/100",
             font=("Arial", 18, "bold"), bg="#add8e6", fg="white").pack(pady=20)
    
    # It determines the grade based on the score 
    if score > 90:
        grade = "A+"
    elif score > 80:
        grade = "A"
    elif score > 70:
        grade = "B"
    elif score > 60:
        grade = "C"      
    elif score > 50:
        grade = "D"
    else:
        grade = "F" # If the scores below 50 then it's a fail         
    
    # Displays the score and the grade after the quiz
    tk.Label(root, text=f"Your final score: {score}/100",
             font=("Arial", 18), bg="#add8e6", fg="white").pack(pady=10)
    tk.Label(root, text=f"Your final grade: {grade}",
             font=("Arial", 18), bg="#add8e6", fg="white").pack(pady=10)
    
    # It is the option to play again or quit the quiz
    tk.Button(root, text="Play Again?", command=displayMenu,
              bg="#8690c2", fg="white", width=15).pack(pady=5)
    tk.Button(root, text="Quit", command=root.destroy,
              bg="#8690c2", fg="white", width=15).pack(pady=5)

# Starts the application by displaying the main menu at the start    
displayMenu()

# Starts the Tkinter event loop
root.mainloop()    
    
    
    
    