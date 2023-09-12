from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:adminadmin@localhost/person-resource"
SQLALCHEMY_DATABASE_URL = "postgresql://resource_db_instance_user:lEEp3bH46uYJ0Tlsn3PdsAhuN8qjFxHi@dpg-ck07ado21fec73dghss0-a.oregon-postgres.render.com/resource_db_instance"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
