from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Sentence(Base):
    __tablename__ = "sentences"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    parse_amr = Column(String)
    parse_ucca  = Column(String)
    parse_drs = Column(String)
    parse_uds_brief = Column(String)
    parse_uds = Column(String)

    def __repr__(self):
        return f"<Sentence id={self.id} text={self.text}"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)


class Evaluation(Base):
    __tablename__ =  "evaluations"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    evaluation = Column(Float)
    
