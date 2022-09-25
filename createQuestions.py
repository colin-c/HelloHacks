# A dictionary of problems and their potential answers

from operator import truediv
from re import X


ProblemBank = {
    "What is 2 + 2?": ["4", "7", "0", "9"]
}


# A dictionary of problems and their correct answer only

ProblemMatch = {
    "What is 2 + 2?": "4"
}


# Add the question to the Problem Bank
def addProblem(question, correctAnswer, randomB, randomC, randomD):
    ProblemBank[question] = [correctAnswer, randomB, randomC, randomD]
    ProblemMatch[question] = correctAnswer
    print("Your question has been successfully added!")

proceed = True

while proceed:
    answer = input("""Add a new question?
    Press A to added new question
    Press D to delete an existing question
    Press X to if not more questions to add""").upper()

    if answer == "A":
        (addProblem(input("What is the Question?: "), input("What is the CORRECT Answer?: "), 
            input("Include WRONG Answer 1: "),
            input("Include WRONG Answer 2: "),
            input("Include WRONG Answer 3: ")))
    
    elif answer == "D":
        key = input("Type in question you want to delete")
        
        if key in ProblemBank and ProblemMatch:
            del ProblemBank[key]
            del ProblemMatch[key] 
        

    elif answer == "X":
        proceed = False

    else: ("Oops! Something went wrong... try again.")