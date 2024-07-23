from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from hospital import Hospital as HospitalModel
import schemas

router = APIRouter(prefix="/api/v1", tags=["hospital"])


@router.get("/hospitals", response_model=list[schemas.Hospital])
def get_all_hospitals(db: Session = Depends(get_db)):
    hospitals = db.query(HospitalModel).all()
    return hospitals
