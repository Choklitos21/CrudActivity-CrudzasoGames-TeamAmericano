import json
from scores import *
import random, time
import os
import platform

with open("questions.json", "r", encoding='utf-8') as json_file:
    questions = json.load(json_file)

user = {
    "name": "Choklitos",
    "score": {
        "time": 0.0,
        "lives": 0,
        "correct": 0,
        "incorrect": 0
    }
}

def jugarTrivia():
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
        for i in range(1,3):
            flag = True
            randomOption = random.randint(0, 3)
            while flag:
                currentQuestion = questions[int(count)]["preguntas"][randomOption]

                #Borrar luego de hacer pruebas
                print("here",currentQuestion)

                print(f"""
                CATEGORIA: {questions[int(count)]["categoria"]}
                Current lives: {lives}{" *Careful, it's your last life*" if lives == 1 else ""}
                This is your question
                {currentQuestion["pregunta"]}
                
                Your options are:
                A. {currentQuestion["opciones"][0]}           B. {currentQuestion["opciones"][1]}
                C. {currentQuestion["opciones"][2]}           D. {currentQuestion["opciones"][3]} 
                """)
                answer = str(input("\nWhat's your answer?: ")).strip().lower()

                if not answer.isalpha():
                    print("Option not valid, try again")
                elif answer != "a" and answer != "b" and answer != "c" and answer != "d":
                    print("Option not valid, try with A, B, C or D")
                elif answer == currentQuestion["respuesta"]:
                    print("!CORRECT¡\nNICE DONE\nCan you keep it up?")
                    correctAnswers += 1
                    flag = False
                elif answer != currentQuestion["respuesta"]:
                    print("INCORRECT\ntry better next time ;)")
                    incorrectAnswers += 1
                    lives -= 1
                    flag = False

                if lives == 0:
                    break

                time.sleep(1.5)

        if lives == 0:
            print("You dont have more lives, good luck next time")
            gameRunning = False
        count += 1
        if count > 4:
            print("GAME OVER")
            gameRunning = False

    totalTime = startTime - time.time()
    activeUser["score"]["time"] = totalTime
    activeUser["score"]["lives"] = lives
    activeUser["score"]["correct"] = correctAnswers
    activeUser["score"]["incorrect"] = incorrectAnswers

    saveScoreMenu(activeUser)

    return activeUser

print(jugarTrivia())