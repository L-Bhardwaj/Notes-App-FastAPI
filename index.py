from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.note import note 


app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")  # mounts static folder


app.include_router(note)

# to run this project, run the following command in the terminal:
# uvicorn index:app --reload

# to activate virtual environment: 
#  & '.venv\Scripts\Activate.ps1'

# to create virtual environment:
# python3 -m venv .venv