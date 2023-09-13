from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Person(BaseModel):
    name: str


@app.get("/")
def root():
    return {"message": "Welcome to Person Resource by jjxavier"}

@app.post("/api", status_code=status.HTTP_201_CREATED)
def create_person(person: Person, db: Session = Depends(get_db)):
    check_person = db.query(models.Person).filter(models.Person.name == person.name).first()
    if check_person:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=f"Person with Name: {person.name} already exists. Try a different name")
    new_person = models.Person(**person.model_dump())
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return {"data": new_person}

@app.get("/api/{user_id}")
def get_person(user_id: int, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.user_id == user_id).first()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Person with User ID: {user_id} was not found. Try a different User ID")
    return {"data": person}

@app.put("/api/{user_id}")
def update_person(user_id: int, updated_person: Person, db: Session = Depends(get_db)):
    person_query = db.query(models.Person).filter(models.Person.user_id == user_id)
    person = person_query.first()
    if person == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"No User with ID: {user_id} was found. Try a different User ID")
    
    person_query.update(updated_person.model_dump(), synchronize_session=False)
    db.commit()
    return {"data": person_query.first()}

@app.delete("/api/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_person(user_id: int, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.user_id == user_id)
    if person.first() ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"No User with ID: {user_id} was found. Try a different User ID")
    
    person.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)