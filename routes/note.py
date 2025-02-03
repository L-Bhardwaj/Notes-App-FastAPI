from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from models.note import Note
from typing import Union

from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.responses import HTMLResponse


note=APIRouter()
templates=Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.notes.notes.find({})
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc":doc["desc"],
            
        })
    return templates.TemplateResponse(
        "index.html", {"request":request, "newDocs":newDocs}
    )
    
    
@note.post("/")
async def create_item(request:Request):
    form=await request.form()
    print(form)
    dict_form=dict(form)
    dict_form["important"]=True if dict_form.get("important")=="on" else False
    note=conn.notes.notes.insert_one(dict_form)
    return {"Success": True}

# @note.post("/")
# def add_note(note:Note):
#     print(note)
#     inserted_note=conn.notes.notes.insert_one(dict(note))
#     return noteEntity(inserted_note)
    
@note.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    