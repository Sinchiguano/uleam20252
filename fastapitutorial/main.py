# from fastapi import FastAPI
# import uvicorn

# # app=FastAPI(title='FastAPI New Tutorial', version='2.0.0')
# app=FastAPI()

# @app.get('/')
# def root():
#     return {"message":"Hello, FastAPI"}

# @app.get('/ping')
# def root():
#     return {"status":"ok"}

    
    
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=5000)



from fastapi import FastAPI
from routes_basics import router as basics_router
from routes_students_mem import router as students_mem_router
from routes_students_db import router as students_db_router
from db import init_db
import uvicorn
from fastapi.templating import Jinja2Templates

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from routes_basics import router as basics_router
from routes_students_mem import router as students_mem_router
from routes_students_db import router as students_db_router
from db import init_db

templates = Jinja2Templates(directory="templates")




app = FastAPI(title="FastAPI Tutorial", version="1.0.0")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(basics_router)
app.include_router(students_mem_router)
app.include_router(students_db_router)


@app.get("/ui/students", response_class=HTMLResponse)
def ui_students(request: Request):
    return templates.TemplateResponse("students_form.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)