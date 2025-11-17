import json

import random, time
import os
import platform

with open("questions.json", "r", encoding='utf-8') as j:
    questions = json.load(j)

user = {
    "nombre": "Choklitos",
    "puntaje": {
        "tiempo": 0.0,
        "vidas": 0,
        "correctas": 0,
        "incorrectas": 0
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
            currentQuestion = questions[int(count)]["preguntas"][random.randint(0, 3)]

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
                continue
            elif answer == currentQuestion["respuesta"] and count < 3:
                print("!CORRECT¡\nNICE DONE\nCan you keep it up?")
                correctAnswers += 1
            elif answer != currentQuestion["respuesta"] and count < 3:
                print("INCORRECT\ntry better next time ;)")
                incorrectAnswers += 1
                lives -= 1

            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')

        if lives <= 0:
            print("You dont have more lives, good luck next time")
            gameRunning = False
        count += 1
        if count > 4:
            print("GAME OVER")
            gameRunning = False

    totalTime = startTime - time.time()
    activeUser["puntaje"]["tiempo"] = totalTime
    activeUser["puntaje"]["vidas"] = lives
    activeUser["puntaje"]["correctas"] = correctAnswers
    activeUser["puntaje"]["incorrectas"] = incorrectAnswers

    return activeUser

print(jugarTrivia())