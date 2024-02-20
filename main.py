from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

#dictionary
students_db = {}
class Student(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    height: float

@app.post("/students/", response_model=Student)
def create_student(student: Student):
    if student.id in students_db:
        raise HTTPException(status_code=400, detail="Student with this ID already exists")
    students_db[student.id] = student
    return student

@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int):
    student = students_db.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.get("/students/", response_model=List[Student])
def read_students():
    return list(students_db.values())

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_student: Student):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    students_db[student_id] = updated_student
    return updated_student

@app.delete("/students/{student_id}", response_model=Student)
def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    deleted_student = students_db.pop(student_id)
    return deleted_student
