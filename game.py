import random, time
import os
import platform

preguntas = [
        {
            "categoria": "Ciencia",
            "preguntas": [
                {
                    "pregunta": "Primera pregunta 'a'",
                    "respuesta": "a",
                    "opciones":[
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "segunda a",
                    "respuesta": "a",
                    "opciones":[
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "segunda b",
                    "respuesta": "a",
                    "opciones":[
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta a",
                    "respuesta": "a",
                    "opciones":[
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                }

            ]
        },
        {
            "categoria": "Arte",
            "preguntas": [
                {
                    "pregunta": "Prefunta b",
                    "respuesta": "b",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta b",
                    "respuesta": "b",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta b",
                    "respuesta": "b",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta b",
                    "respuesta": "b",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                }

            ]
        },
        {
            "categoria": "Musica",
            "preguntas": [
                {
                    "pregunta": "Prefunta c",
                    "respuesta": "c",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta c",
                    "respuesta": "c",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta c",
                    "respuesta": "c",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta b",
                    "respuesta": "c",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                }

            ]
        },
        {
            "categoria": "Geografía",
            "preguntas": [
                {
                    "pregunta": "Prefunta d",
                    "respuesta": "d",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta d",
                    "respuesta": "d",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta d",
                    "respuesta": "d",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta d",
                    "respuesta": "d",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                }

            ]
        },
        {
            "categoria": "Deportes",
            "preguntas": [
                {
                    "pregunta": "Prefunta a",
                    "respuesta": "a",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta a",
                    "respuesta": "a",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta a",
                    "respuesta": "a",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta a",
                    "respuesta": "a",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                }

            ]
        },
        {
            "categoria": "Historia",
            "preguntas": [
                {
                    "pregunta": "Prefunta b",
                    "respuesta": "b",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta b",
                    "respuesta": "b",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta b",
                    "respuesta": "b",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                },
                {
                    "pregunta": "Prefunta b",
                    "respuesta": "b",
                    "opciones": [
                        "opcion1", "opcion2", "opcion3", "opcion4"
                    ]
                }

            ]
        },
    ]

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
            currentQuestion = preguntas[count]["preguntas"][random.randint(0,3)]
            print(f"""
            CATEGORIA: {preguntas[count]["categoria"]}a
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
            elif answer == currentQuestion["respuesta"]:
                print("!CORRECT¡\nNICE DONE\nCan you keep it up?")
                correctAnswers += 1
            else:
                print("INCORRECT\ntry better next time ;)")
                incorrectAnswers += 1
                lives -= 1

            time.sleep(2)
            print(os.name)
            if os.name == "Windows":
                os.system('cls')
            else:
                os.system('clear')


        if lives <= 0:
            print("You dont have more lives, good luck next time")
            gameRunning = False
        count += 1
        if count > 4:
            gameRunning = False

    totalTime = startTime - time.time()
    activeUser["puntaje"]["tiempo"] = totalTime
    activeUser["puntaje"]["vidas"] = lives
    activeUser["puntaje"]["correctas"] = correctAnswers
    activeUser["puntaje"]["incorrectas"] = incorrectAnswers

    return activeUser

print(jugarTrivia())