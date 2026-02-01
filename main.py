from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!'

@app.get('/students')
async def get_students():
    return data

@app.get('/students/{id}')
async def get_student(id: int):
    for student in data:
        if student['id'] == id:
            return student
        
@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: 
              filtered_students.append(student) 
        return filtered_students
    return data


@app.get('/stats')
async def get_stats():

    stats = {
        "Chicken": 0,
        "Fish": 0,
        "Vegetable": 0,
        "Computer Science (Special)": 0,
        "Computer Science (Major)": 0,
        "Information Technology (Special)": 0,
        "Information Technology (Major)": 0,
    }

    for students in data:
      
        pref = students.get('pref', '')
        if pref == 'Chicken':
            stats["Chicken"] += 1
        elif pref == 'Fish':
            stats["Fish"] += 1
        else:
            stats["Vegetable"] += 1

        prog = students.get('programme', '')
        if prog in ("Computer Science (Special)") == "Computer Science (Special)":
            stats["Computer Science (Special)"] += 1
        elif prog in ("Computer Science (Major)") == "Computer Science (Major)":
            stats["Computer Science (Major)"] += 1
        elif prog in ("Information Technology (Special)") == "Information Technology (Special)":
            stats["Information Technology (Special)"] += 1
        elif prog in ("Information Technology (Major)") == "Information Technology (Major)":
            stats["Information Technology (Major)"] += 1

    return stats

      

        
    
