from sqlalchemy import CheckConstraint, Column, Float, Integer, String

from storage.postgres.postrgres import Base


class Quests_DB(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True, index=True)
    employer = Column(String)
    title = Column(String, index=True, unique=True)
    description = Column(String)
    award = Column(Float(precision=16))

    __table_args__ = (
        CheckConstraint(award >= 0, name="check_award_positive"),
        {})
