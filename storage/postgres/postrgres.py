from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from server.schemas import PgConfig

pg_config = PgConfig()

URL_DATABASE = f"postgresql://{pg_config.user}:{pg_config.password}@localhost:{pg_config.port}/{pg_config.db_name}"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
