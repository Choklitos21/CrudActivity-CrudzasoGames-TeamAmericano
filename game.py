import json
from scores import saveScoreMenu
import random, time
import os

if os.path.getsize("questions.json") == 0:
    data = []
else:
    with open("questions.json", 'r', encoding="utf-8") as old_json:
        questions = json.load(old_json)

def jugarTrivia(user):
    print("WELCOME TO TRIVIA")
    activeUser = user
    count = 0
    correctAnswers = 0
    incorrectAnswers = 0
    startTime = time.time()
    totalTime = 0
    lives = 3

    gameRunning = True
    while gameRunning:
        numbers = range(4)
        randomNumbers = random.sample(numbers, 4)
        #print(randomNumbers)
        for i in range(0,2):
            flag = True
            while flag:
                currentQuestion = questions[int(count)]["questions"][randomNumbers[i]]

                #Borrar luego de hacer pruebas
                #print("here",currentQuestion)

                print(f"""
                CATEGORIA: {questions[int(count)]["category"]}
                Current lives: {lives}{" *Careful, it's your last life*" if lives == 1 else ""}
                This is your question
                {currentQuestion["question"]}
                
                Your options are:
                A. {currentQuestion["options"][0]}           B. {currentQuestion["options"][1]}
                C. {currentQuestion["options"][2]}           D. {currentQuestion["options"][3]} 
                """)
                answer = str(input("\nWhat's your answer?: ")).strip().lower()

                if not answer.isalpha():
                    print("Option not valid, try again")
                elif answer != "a" and answer != "b" and answer != "c" and answer != "d":
                    print("Option not valid, try with A, B, C or D")
                elif answer == currentQuestion["answer"]:
                    print("!CORRECT¡\nNICE DONE\nCan you keep it up?")
                    correctAnswers += 1
                    flag = False
                elif answer != currentQuestion["answer"]:
                    print("INCORRECT\ntry better next time ;)")
                    incorrectAnswers += 1
                    lives -= 1
                    flag = False

                if lives == 0:
                    gameRunning = False
                    flag = False

                time.sleep(1.5)

            if lives == 0:
                break

        if lives == 0:
            print("You dont have more lives, good luck next time")
            gameRunning = False
        count += 1
        if count > 4:
            print("GAME OVER")
            gameRunning = False

    totalTime = time.time() - startTime
    activeUser["score"]["time"] = totalTime
    activeUser["score"]["lives"] = lives
    activeUser["score"]["correct"] = correctAnswers
    activeUser["score"]["incorrect"] = incorrectAnswers

    saveScoreMenu(activeUser)

    return activeUser