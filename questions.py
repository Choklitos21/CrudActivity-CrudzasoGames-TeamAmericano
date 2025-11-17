import json
import os
from sys import flags

# if os.path.getsize("questions.json") == 0:
#     data = []
# else:
#     with open("scores.json", 'r') as old_json:
#         oldQuestions = json.load(old_json)


newQuestion = []

def createQuestion():
    categoryFlag = True
    while categoryFlag:
        print("""
        Categories to add a question
        1. Science
        2. Art
        3. Music
        4. Geography
        5. Sports
        6. History
        pass
        """)
        category = str(input("Select a category: ")).strip().lower()
        if category != "science" and category != "science" and category != "science" and category != "science" and category != "geography" and category != "history":
            print("That's not a valid category, try again\n")
        else:
            categoryFlag = False

    questionFlag = True
    while questionFlag:
        question = str(input("Write your question: ")).strip()
        confirm = str(input("Want to continue or change something? y: to continue | n: to try again: ")).strip().lower()
        if confirm == "y" or confirm == "yes":
            questionFlag = False
        elif confirm == "n" or confirm == "no":
            continue
        else:
            print("Option not valid, use y/yes or n/no only\n")

    options = []
    optionsFlag = True
    while optionsFlag:
        options.append(str(input("Write the option A. -> ")).strip())
        options.append(str(input("Write the option B. -> ")).strip())
        options.append(str(input("Write the option C. -> ")).strip())
        options.append(str(input("Write the option D. -> ")).strip())

        confirm = str(input("Want to continue or change something? y: to continue | n: to try again: ")).strip().lower()
        if confirm == "y" or confirm == "yes":
            optionsFlag = False
        elif confirm == "n" or confirm == "no":
            continue
        else:
            print("Option not valid, use y/yes or n/no only\n")

    correctFlag = True
    while correctFlag:
        correctAnswer = str(input("What's the correct answer? A, B, C or D: ")).strip().lower()
        if correctAnswer != "a" and correctAnswer != "b" and correctAnswer != "c" and correctAnswer != "d":
            print("Option not valid, please put only A, B, C or D")
            continue

        confirm = str(input("Want to continue or change something? y: to continue | n: to try again: ")).strip().lower()
        if confirm == "y" or confirm == "yes":
            correctFlag = False
        elif confirm == "n" or confirm == "no":
            continue
        else:
            print("Option not valid, use y/yes or n/no only\n")

    if os.path.getsize("questions.json") == 0:
        data = []
    else:
        with open("questions.json", 'r', encoding="utf-8") as old_json:
            oldQuestions = json.load(old_json)

    for i in oldQuestions:
        if i["category"] == category:
            i["questions"].append({
                "question": question,
                "answer": correctAnswer,
                "options": options
            })

    with open("questions.json", "w", encoding="utf-8") as new_json:
        json.dump(oldQuestions, new_json, indent=4)

    print("Your question was added, thanks for making our game better")

def deleteQuestion():
    pass

def modifyQuestion():
    pass

def listQuestions():
    if os.path.getsize("questions.json") == 0:
        data = []
    else:
        with open("questions.json", 'r', encoding="utf-8") as old_json:
            oldQuestions = json.load(old_json)

    #               Categoria        preguntas[]         pregunta #
    #oldQuestions      [0]          ["preguntas"]          [0]
    print("Questions until now")
    for i in oldQuestions:
        print(i, "\n")

def questionsMenu():
    print("""
    QUESTIONS MENU
    1. List all questions until now
    2. Create a new question
    3. Update a current question
    4. Remove a question
    5. Previous menu
    """)

    option = str(print("Select an option: "))
    match option:
        case "1":
            print("list")
        case "2":
            print("list")
        case "3":
            print("list")
        case "4":
            print("list")
        case "5":
            print("list")
        case _:
            print("Option not valid, select between 1 to 5")
    pass


#createQuestion()
listQuestions()


#También requiero la categoria para saber donde almacenarla
# question = {"preguntas": [
#     {
#         "pregunta": "¿Cual es el símbolo de PLATA en la tabla periódica?",
#         "respuesta": "b",
#         "opciones": [
#             "P", "Ag", "B", "As"
#         ]
#     }
# ]}
