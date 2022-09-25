from createQuestions import ProblemBank
from createQuestions import AnswerBank


# Define variable for values from different keys
bank = AnswerBank.get("What is 2 + 2?")

answer = input("""Select an option:
                Press A for option A
                Press B for option B
                Press C for option C
                Press D for option D""").upper()

current = False

if answer == AnswerBank.get("What is 2 + 2?"):
    current = True

print(current)






    










