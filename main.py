from questions import questionsMenu
from game import jugarTrivia
from scores import showScores
from users import crearusuario, iniciarsesion

def loginMenu():
    menuFlag = True
    while menuFlag:
        print("""
        MENU
        1. Login
        2. Register
        3. EXIT
        """)

        menuOption = str(input("Select an option: "))
        match menuOption:
            case "1":
                user = iniciarsesion()
                if user:
                    gameMenu(user)
                else:
                    continue
            case "2":
                user = crearusuario()
                if user:
                    gameMenu(user)
                else:
                    continue
            case "3":
                menuFlag = False
            case "ADMIN*123":
                print("Admin options")
            case _:
                print("Option not valid, use only numbers from 1 to 5")

def gameMenu(user):
    gameFlag = True
    while gameFlag:
        print("""
        GAME MENU
        1. Start game
        2. Show scores
        3. Questions management
        4. Log out
        """)

        gameOption = str(input("Select an option: "))
        match gameOption:
            case "1":
                jugarTrivia(user)
            case "2":
                showScores()
            case "3":
                questionsMenu()
            case "4":
                gameFlag = False
            case _:
                print("Option not valid, use only numbers from 1 to 5")

    return False

loginMenu()