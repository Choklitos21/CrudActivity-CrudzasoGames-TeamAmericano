import os
import json

def saveScore(score):
    if os.path.getsize("scores.json") == 0:
        data = []
    else:
        with open("scores.json", 'r') as old_json:
            data = json.load(old_json)

    data.append(score)

    with open("scores.json", "w", encoding="utf-8") as new_json:
        json.dump(data, new_json, indent=4)

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

def showScores():
    if os.path.getsize("scores.json") == 0:
        data = []
    else:
        with open("scores.json", 'r') as old_json:
            data = json.load(old_json)

    if not data:
        print("No scores saved yet")
        return
    else:
        print("SCORES")
        count = 1
        if len(data) == 1:
            print(f"""
            #{count} {data[0]["name"]}
            Time: {(data[0]["score"]["time"] / 60):.2f}:{data[0]["score"]["time"]:.2f}
            Lives: {data[0]["score"]["lives"]}
            Correct: {data[0]["score"]["correct"]} / Incorrect: {data[0]["score"]["incorrect"]}
            """)
        else:
            for i in data:
                for j in data:
                    if i["score"]["time"] > j["score"]["time"]:
                        print(f"""
                        #{count} {i["name"]}
                        Time: {(i["score"]["time"] / 60):.2f}:{i["score"]["time"]:.2f}
                        Lives: {i["score"]["lives"]}
                        Correct: {i["score"]["correct"]} / Incorrect: {i["score"]["incorrect"]}
                        """)
                        count += 1