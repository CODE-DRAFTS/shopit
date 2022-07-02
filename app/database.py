from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL='postgresql://postgres:root@localhost/ShopIt' #TODO env varible

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker( autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


#dependency
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()