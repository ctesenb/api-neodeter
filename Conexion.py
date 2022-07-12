from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "mysql+mysqlconnector://root:infoplus1234@localhost:3306/crudfastapi"
DATABASE_URL = "mysql+mysqlconnector://admin:adbO1NJG@mysql-43314-0.cloudclusters.net:19751/neodeter"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()