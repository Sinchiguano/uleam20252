from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List
from models import Student
from schemas import StudentIn, StudentOut
from db import get_session

router = APIRouter(prefix="/students-db", tags=["Students (SQLite)"])

@router.post("/", response_model=StudentOut, status_code=status.HTTP_201_CREATED)
def create_student(payload: StudentIn, session: Session = Depends(get_session)):
    # unique email check
    if session.exec(select(Student).where(Student.email == payload.email)).first():
        raise HTTPException(status_code=409, detail="Email already exists")
    student = Student(**payload.model_dump())
    session.add(student)
    session.commit()
    session.refresh(student)
    return StudentOut(**student.model_dump())

@router.get("/", response_model=List[StudentOut])
def list_students(q: str | None = None, skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    stmt = select(Student)
    if q:
        like = f"%{q}%"
        stmt = stmt.where(
            (Student.first_name.ilike(like)) |
            (Student.last_name.ilike(like)) |
            (Student.email.ilike(like))
        )
    results = session.exec(stmt.offset(skip).limit(limit)).all()
    return [StudentOut(**s.model_dump()) for s in results]

@router.get("/{student_id}", response_model=StudentOut)
def get_student(student_id: int, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return StudentOut(**student.model_dump())

@router.put("/{student_id}", response_model=StudentOut)
def update_student(student_id: int, payload: StudentIn, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # unique email
    existing = session.exec(select(Student).where(Student.email == payload.email, Student.id != student_id)).first()
    if existing:
        raise HTTPException(status_code=409, detail="Email already exists")

    for k, v in payload.model_dump().items():
        setattr(student, k, v)
    session.add(student)
    session.commit()
    session.refresh(student)
    return StudentOut(**student.model_dump())

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    session.delete(student)
    session.commit()
