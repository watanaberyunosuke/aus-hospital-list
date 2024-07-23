from typing import Optional
from pydantic import BaseModel


class Hospital(BaseModel):
    objectid: Optional[int] = None
    hsib_id: int
    hosp_name: Optional[str] = None
    category: Optional[str] = None
    street: Optional[str] = None
    pcode: Optional[str] = None
    suburb: Optional[str] = None
    state: Optional[str] = None
    xcoord: Optional[str] = None
    ycoord: Optional[str] = None
    globalid: Optional[str] = None

    class Config:
        orm_mode = True
