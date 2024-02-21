from fastapi import FastAPI
from typing import Optional

app = FastAPI()

#dictionary
students = {}

#defining the student class
class Student:
    def __init__(self, id: int, name: str, age: int, sex: str, height: float):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height

#creating a student resource
@app.post("/students/")
async def create_student(student: dict):
    new_student = Student(**student)
    if new_student.id in students:
        return {"error": "Student already exists"}
    students[new_student.id] = new_student.__dict__
    return new_student.__dict__

#retrieving a student resource
@app.get("/students/{student_id}")
async def read_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    return students[student_id]

#retrieving many students
@app.get("/students/")
async def read_students():
    return list(students.values())

#updating a student resource
@app.put("/students/{student_id}")
async def update_student(student_id: int, student: dict):
    new_student = Student(**student)
    if student_id not in students:
        return {"error": "Student not found"}
    students[student_id] = new_student.__dict__
    return students[student_id]

#deleting a student resource
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    del students[student_id]
    return {"message": "Student deleted"}