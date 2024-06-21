from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import internal
from server import schemas
from storage import models


def get_quest_by_id(quest_id: int, db: Session):
    quest_out = db.query(models.Quests_DB).filter(models.Quests_DB.id == quest_id).first()
    if not quest_out:
        raise KeyError(f"quest with id={quest_id} not found")
    return quest_out


def get_quests_by_employer(employer: str, db: Session):
    quest_out = db.query(models.Quests_DB).filter(models.Quests_DB.employer == employer).all()
    if not quest_out:
        raise KeyError(f"{employer} does not supply quests yet")
    return quest_out


def get_quest_by_title(title: str, db: Session):
    quest_out = db.query(models.Quests_DB).filter(models.Quests_DB.title == title).first()
    if not quest_out:
        raise KeyError(f"{title} - quest does not exist")
    return quest_out


def get_all_quests(db: Session):
    return sorted(db.query(models.Quests_DB).all(), key=lambda x: x.award)


def publish_quest(quest: schemas.Quest, db: Session):
    if quest.award < 0:
        raise KeyError("award must be positive number")
    try:
        db_quest = models.Quests_DB(employer=quest.employer, title=quest.title,
                                    description=quest.description, award=quest.award)

        db.add(db_quest)
        db.commit()
        db.refresh(db_quest)
    except IntegrityError as exc:
        raise KeyError(internal.tools.parse_integrity_exc_msg(exc.orig.args[0]))
    return schemas.QuestId(quest_id=db_quest.id)


def change_quest(title: str, quest_id: int, new_quest: schemas.ChangesForQuest, db: Session):
    if new_quest.award < 0:
        raise KeyError("new award must be positive number")

    quest = db.query(models.Quests_DB).filter(and_(models.Quests_DB.title == title,
                                                   models.Quests_DB.id == quest_id)).first()
    if not quest:
        raise KeyError(f"quest with id={quest_id} and title={title} does not exist")

    quest.employer = new_quest.employer
    db.flush()

    quest.description = new_quest.description
    db.flush()

    quest.award = new_quest.award
    db.commit()

    return quest


def remove_quest(title: str, quest_id: int, db: Session):
    quest = db.get(models.Quests_DB, quest_id)

    if not quest:
        raise KeyError(f"quest with id={quest_id} and title={title} does not exist")

    db.delete(quest)
    db.commit()

    return {"ok": True}
