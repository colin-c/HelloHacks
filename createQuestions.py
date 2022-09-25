from operator import truediv
from re import X


# A dictionary of problems and their potential answers
ProblemBank = {
    "What is 2 + 2?": ["4", "7", "0", "9"],
    "What is 5 + 3?": ["4", "8", "5", "9"]
}

# A dictionary of problems and their true answer
AnswerBank = {
    "What is 2 + 2?": "A",
    "What is 5 + 3?": "B"
}



# Add the question to the Problem Bank
def addProblem(question, answerA, answerB, answerC, answerD):
    ProblemBank[question] = [answerA, answerB, answerC, answerD]
    print("Your question has been successfully added!")

# Add the question to the AnswerBank with correct multiple choice option
def addAnswer(question, answer):
    AnswerBank[question] = answer
    print("Correct answer and letter pairing has been confirmed")

proceed = True


def addQ(proceed):
# Input a button to produce a certain output
    while proceed:
        answer = input("""Add a new question?
        Press A to added new question
        Press D to delete an existing question
        Press V to view current existing questions
        Press X to if not more questions to add""").upper()

    # To add a question to ProblemBank and Problem Dictionary
        if answer == "A":
            question = input("Question: ")
            (addProblem((question), 
                        input("Answer (A): "), 
                        input("Answer (B): "),
                        input("Answer (C): "),
                        input("Answer (D): ")))
        # To add a character that matches with the CORRECT value
            (addAnswer((question),
                        input("Choose correct letter as true answer")))

            proceed = False

    # To delete an existing question to ProblemBank and Problem Dictionary   
        elif answer == "D":
            key = input("Type in question you want to delete")
            
            if key in ProblemBank:
                del ProblemBank[key] 
                ("The question has been successful deleted")

    # To view current questions, correct answers, and wrong answers from the ProblemBank
        elif answer == "V":
            print(ProblemBank)

    # To end the session and return to previous screen
        elif answer == "X":
            proceed = False

    # Inputing any other key will result in not but an error message
        else: ("Oops! Something went wrong... try again.")

if __name__ == "__main__":
    addQ(proceed)


