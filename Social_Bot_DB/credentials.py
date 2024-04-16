from sqlalchemy import create_engine, Column, ForeignKey, String, Integer, CHAR, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Base_Cred(Base):
    __tablename__ = 'BotCred'

    id = Column(Integer, primary_key=True)
    company_name = Column(String)
    proxy_ip = Column(String, nullable=True)
    start_time = Column(Time)
    end_time = Column(Time)
    cookie = Column(String, nullable=True)
    cookie_exp = Column(String, nullable=True)
    username = Column(String, nullable=True)
    password = Column(String, nullable=True)
