from fastapi import status, HTTPException, Depends, APIRouter, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, models, utils, oauth2, schemas

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
  # user_credentials.username & user_credentials.password
  user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
  if not user or not utils.verify(user_credentials.password, user.password):
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")

  # create and return a token
  access_token = oauth2.create_access_token({"user_id": user.id})
  return {"access_token": access_token, "token_type": "bearer"}
  