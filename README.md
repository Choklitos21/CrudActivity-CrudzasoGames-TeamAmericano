# CrudActivity-CrudasoGames-TeamAmericano - Trivia

---

### Explanation:
Trivia-style game project made in Python. This project shows a Trivia-style game where there are two questions per 
category, 6 categories in total, 12 questions.

The categories are: Science, Art, Music, Geography, Sports and History.

Each player will answer a total of 12 questions, or until they got the wrong 3 questions, meaning that each player had 
3 lives, each incorrect answer takes a life off.

When the players end their turn, they will have the option to record the result in the system. The score will show the 
best player by time and lives.

To play each person has to complete a registration before they can play.
Each user can play the game and also add new questions to the game

---

### 1. How to run the game:
Use this code to run the game

+ On Linux
```bash
python3 main.py
```

+ On Windows
```bash
py main.py
```

---

## 2. External libraries

+ ### "os" Library
The "os" library in Python acts as an interface to the underlying operating system, allowing you to perform file system 
operations like creating/deleting folders (os.mkdir()), manipulating file paths (os.path), and accessing environment variables, making it essential for system-level interaction
```py
import os
```

+ ### "json" Library
The "json" library serves as a translator for the universally accepted JSON (JavaScript Object Notation) data format, 
enabling serialization (converting Python objects like dictionaries into JSON strings via json.dumps()) and deserialization (converting JSON strings back into Python objects via json.loads()), which is critical for data exchange over the web and saving structured data
```py
import json
```

---

## 3. Description of the information management system implemented

We manage information using JSON documents, where we store user information, scores, and stored questions, each in 
separate files.

## 4. Members of the project
+ Diego Alejandro Morales Montoya
+ Anderson Guzman
+ Edwin
+ Toro

