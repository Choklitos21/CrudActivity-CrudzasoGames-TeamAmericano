import os
import json

scoreTest = {
    "score": {
        "time": 0.0,
        "lives": 0,
        "correct": 0,
        "incorrect": 0
    }
}

def saveScore(score):
    if os.path.getsize("scores.json") == 0:
        data = []
    else:
        with open("scores.json", 'r') as old_json:
            data = json.load(old_json)

    #Remove after testing
    print(data)
    data.append(score)
    print(data)

    with open("scores.json", "w", encoding="utf-8") as new_json:
        json.dump(data, new_json, indent=4)

#Remove after testing
#saveScore()

def saveScoreMenu(score):
    flag = True
    while flag:
        option = str(input("Would you like to save your score? y/n: ")).strip().lower()

        if option == "y" or option == "yes":
            saveScore(score)
            print("SCORE SAVED")
            flag = False
        elif option == "n" or option == "no":
            flag = False
        else:
            print("Option not valid, try again")