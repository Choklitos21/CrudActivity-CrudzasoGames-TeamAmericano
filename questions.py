import json
import os

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
    categoryFlag = True
    while categoryFlag:
        print("""
            Categories
            1. Science
            2. Art
            3. Music
            4. Geography
            5. Sports
            6. History
            pass
            """)
        category = str(input("Select a category first: ")).strip().lower()
        if category != "science" and category != "science" and category != "science" and category != "science" and category != "geography" and category != "history":
            print("That's not a valid category, try again\n")
        else:
            categoryFlag = False

        if os.path.getsize("questions.json") == 0:
            data = []
        else:
            with open("questions.json", 'r', encoding="utf-8") as old_json:
                oldQuestions = json.load(old_json)

        count = 1
        for i in oldQuestions:
            if i["category"] == category:
                for j in i["questions"]:
                    print(f"""
                    Question #{count}
                    Text: {j["question"]}
                    Options: {j["options"]}
                    Answer: {j["answer"]}
                    """)
                    count +=1

        optionFlag = True
        while optionFlag:
            option = input("Select a # of the question you want to delete: ")
            if option.isalpha():
                print(f"Invalid option, select only numbers from 1 to {count}\n")
            elif int(option) <= 0 or (int(option) + 1) > count:
                print(f"Invalid option, select only numbers from 1 to {count}\n")
            else:
                optionFlag = False

        for i in oldQuestions:
            if i["category"] == category:
                i["questions"].pop(int(option) - 1)

        with open("questions.json", "w", encoding="utf-8") as new_json:
            json.dump(oldQuestions, new_json, indent=4)

        print("Question removed")

def modifyQuestion():
    categoryFlag = True
    while categoryFlag:
        print("""
                Categories
                1. Science
                2. Art
                3. Music
                4. Geography
                5. Sports
                6. History
                pass
                """)
        category = str(input("Select a category first: ")).strip().lower()
        if category != "science" and category != "science" and category != "science" and category != "science" and category != "geography" and category != "history":
            print("That's not a valid category, try again\n")
        else:
            categoryFlag = False

        if os.path.getsize("questions.json") == 0:
            data = []
        else:
            with open("questions.json", 'r', encoding="utf-8") as old_json:
                oldQuestions = json.load(old_json)

        count = 1
        for i in oldQuestions:
            if i["category"] == category:
                for j in i["questions"]:
                    print(f"""
                        Question #{count}
                        Text: {j["question"]}
                        Options: {j["options"]}
                        Answer: {j["answer"]}
                        """)
                    count += 1

        optionFlag = True
        while optionFlag:
            option = input("Select a # of the question you want to update: ")
            if option.isalpha():
                print(f"Invalid option, select only numbers from 1 to {count}\n")
            elif int(option) <= 0 or (int(option) + 1) > count:
                print(f"Invalid option, select only numbers from 1 to {count}\n")
            else:
                optionFlag = False

    #--------------------
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

    for i in oldQuestions:
        if i["category"] == category:
            print(i["questions"])
            print(count)
            i["questions"][count - 2] = {
                "question": question,
                "answer": correctAnswer,
                "options": options
            }

    with open("questions.json", "w", encoding="utf-8") as new_json:
        json.dump(oldQuestions, new_json, indent=4)

    print("Question updated")

def listQuestions():
    if os.path.getsize("questions.json") == 0:
        data = []
    else:
        with open("questions.json", 'r', encoding="utf-8") as old_json:
            oldQuestions = json.load(old_json)

    print("Questions until now\n")
    index = 1
    for i in oldQuestions:
        for j in i["questions"]:
            print(f"""
        Questions #{index}
        Category: {i["category"].capitalize()}
        Question: {j["question"]}
        Options: A. {j["options"][0]} | B. {j["options"][1]} | C. {j["options"][2]} | D. {j["options"][3]}
        Answer: {j["answer"].capitalize()}\n
        """)
            index += 1

def questionsMenu():
    menuQuestionsFlag = True
    while menuQuestionsFlag:
        print("""
        QUESTIONS MENU
        1. List all questions until now
        2. Create a new question
        3. Update a current question
        4. Remove a question
        5. Previous menu
        """)

        option = str(input("Select an option: "))
        match option:
            case "1":
                listQuestions()
            case "2":
                createQuestion()
            case "3":
                modifyQuestion()
            case "4":
                deleteQuestion()
            case "5":
                menuQuestionsFlag = False
            case _:
                print("Option not valid, select between 1 to 5")

