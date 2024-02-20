from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

# Dictionary
students_db = {}

class Student:
    def __init__(self, id: int, name: str, age: int, sex: str, height: float):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height

@app.post("/students/", response_model=Student)
def create_student(id: int, name: str, age: int, sex: str, height: float):
    if id in students_db:
        raise HTTPException(status_code=400, detail="Student with this ID already exists")

    student = Student(id=id, name=name, age=age, sex=sex, height=height)
    students_db[id] = student
    return student

@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int):
    student = students_db.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student.__dict__

@app.get("/students/", response_model=List[Student])
def read_students():
    return [student.__dict__ for student in students_db.values()]

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, name: str, age: int, sex: str, height: float):
    student = students_db.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    student.name = name
    student.age = age
    student.sex = sex
    student.height = height

    return student.__dict__

@app.delete("/students/{student_id}", response_model=Student)
def delete_student(student_id: int):
    student = students_db.pop(student_id, None)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student.__dict__
