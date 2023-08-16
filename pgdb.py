from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

from config import PG_HOST, PG_NAME, PG_PASS, PG_PORT, PG_USER


PG_URL = f'postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_NAME}'

Base: DeclarativeMeta = declarative_base()

engine = create_engine(PG_URL)

SessionPg = sessionmaker(autoflush=False, bind=engine)

