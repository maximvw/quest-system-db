from fastapi import APIRouter, Depends, HTTPException
from typing import List
from http import HTTPStatus
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from storage import models
from storage.postgres import crud
from server import schemas
from storage.postgres.postrgres import engine, SessionLocal
from internal import tools

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/quests/get_quest_by_id/{quest_id}", response_model=schemas.Quest)
def show_quest_by_id(quest_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_quest_by_id(quest_id, db)
    except KeyError as exc:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=exc.args[0]
        )

@router.get("/quests/show_by_employer/{employer}", response_model=List[schemas.Quest])
def show_quests_by_employer(employer: str, db: Session = Depends(get_db)):
    try:
        return crud.get_quests_by_employer(employer, db)
    except KeyError as exc:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=exc.args[0]
        )


@router.get("/quests/show_by_title/{title}", response_model=schemas.Quest)
def show_quest_by_title(title: str, db: Session = Depends(get_db)):
    try:
        return crud.get_quest_by_title(title, db)
    except KeyError as exc:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=exc.args[0]
        )


@router.get("/quests/show_all", response_model=List[schemas.Quest])
def show_all_quests(db: Session = Depends(get_db)):
    return crud.get_all_quests(db)


@router.post("/quests/publish_quest", response_model=schemas.QuestId)
def publish_quest(quest: schemas.Quest, db: Session = Depends(get_db)):
    try:
        return crud.publish_quest(quest, db)
    except IntegrityError as exc:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=tools.parse_integrity_exc_msg(exc.orig.args[0])
        )


@router.put("/quests/change_quest/{title}_{quest_id}", response_model=schemas.Quest)
def change_quest(title: str, quest_id: int, new_quest: schemas.ChangesForQuest, db: Session = Depends(get_db)):
    try:
        return crud.change_quest(title, quest_id, new_quest, db)
    except KeyError as exc:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=exc.args[0]
        )


@router.delete("/quests/remove_quest/{title}_{quest_id}")
def remove_quest(title: str, quest_id: int, db: Session = Depends(get_db)):
    try:
        return crud.remove_quest(title, quest_id, db)
    except KeyError as exc:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=exc.args[0]
        )

