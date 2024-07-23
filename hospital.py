from sqlalchemy import Column, Integer, String
from database import Base

class Hospital(Base):
    __tablename__ = "Australia_Hospital"
    objectid = Column(Integer)
    hsib_id = Column(Integer, primary_key=True)
    hosp_name = Column(String)
    category = Column(String)
    street = Column(String)
    pcode = Column(String)
    suburb = Column(String)
    state = Column(String)
    xcoord = Column(String)
    ycoord = Column(String)
    globalid = Column(String)
