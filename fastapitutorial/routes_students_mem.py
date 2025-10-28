from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas import StudentIn, StudentOut



router = APIRouter(prefix="/students", tags=["Students (memory)"])   

_db: List[StudentOut] = []
_auto_id = 1


@router.post("/", response_model=StudentOut, status_code=status.HTTP_201_CREATED)
def create_student(payload: StudentIn):
    global _auto_id
    new_student = StudentOut(id=_auto_id, **payload.model_dump())
    _db.append(new_student) 
    _auto_id += 1
    return new_student


@router.get("/", response_model=List[StudentOut])
def list_students(q:str|None=None):
    if not q:
        return _db
    q = q.lower()
    return [student for student in _db if q in student.first_name.lower() or q in student.last_name.lower() or q in student.email.lower()]

@router.get("/{student_id}", response_model=StudentOut)
def get_student(student_id: int):
    for student in _db:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


@router.put("/{student_id}", response_model=StudentOut)
def update_student(student_id: int, payload: StudentIn):
    for index, student in enumerate(_db):
        if student.id == student_id:
            updated_student = StudentOut(id=student_id, **payload.model_dump())
            _db[index] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")        

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    for index, student in enumerate(_db):
        if student.id == student_id:
            del _db[index]
            return
    raise HTTPException(status_code=404, detail="Student not found")