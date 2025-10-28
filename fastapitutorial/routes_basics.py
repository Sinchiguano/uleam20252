from fastapi import FastAPI,  APIRouter, HTTPException

router = APIRouter(prefix="/basics", tags=["basics"])

@router.get("/square/{number}")
def read_root(number: int):
    return {"square": number ** 2}


@router.get("/greet")
def greet(name: str = "student", excited: bool = False):
    text = f"Hello, {name}"
    if excited:
        text += "!!!"
    return {"greeting": text}

@router.get("/divide")
def divide(a: float, b: float):
    if b==0:
        raise HTTPException(status_code=400,
                            detail="Division by zero is not allowed.")
    return {"result": a / b}

# http://127.0.0.1:5000/basics/f2c?fahrenheit=98.6
@router.get("/f2c")
def fahrenheit_to_celsius(fahrenheit: float):
    celsius = (fahrenheit - 32) * 5/9
    return {"celsius": celsius}

# http://127.0.0.1:5000/basics/c2f?celsius=37
@router.get("/c2f")
def celsius_to_fahrenheit(celsius: float):
    fahrenheit = (celsius * 9/5) + 32
    return {"fahrenheit": fahrenheit}


# http://127.0.0.1:5000/basics/is_even/10
@router.get("/is_even/{number}")
def is_even(number: int):       
    return {"is_even": number % 2 == 0}     

# curl "http://127.0.0.1:5000/basics/is_even/10"
@router.get("/check_age/{age}")
def check_age(age: int):
    if age < 0:
        raise HTTPException(status_code=422, detail="Age cannot be negative")
    return {"message": f"Age {age} is valid"}

