#Python
from typing import Optional, List

#fastApi
from fastapi import (FastAPI,status)

#Models
from models import *

app = FastAPI()


@app.get(
    path="/",
    
)
def home():
    return{"Api": "Twitter"}


#path operation 

##User

@app.post(
    path="/signup",
    response_model=User, ##responde al usuario
    status_code=status.HTTP_201_CREATED,
    summary="Register a Uses"  ,
    tags=["Users"]
)
def signup():
    pass

@app.post(
    path="/login",
    response_model=User, ##responde al usuario
    status_code=status.HTTP_200_OK,
    summary="Login a Uses"  ,
    tags=["Users"]
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User], ##responde al usuario
    status_code=status.HTTP_200_OK,
    summary="show all Uses"  ,
    tags=["Users"]
)
def show_all_user():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User, ##responde al usuario
    status_code=status.HTTP_200_OK,
    summary="show a Uses"  ,
    tags=["Users"]
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User, ##responde al usuario
    status_code=status.HTTP_200_OK,
    summary="Delete a Uses"  ,
    tags=["Users"]
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User, ##responde al usuario
    status_code=status.HTTP_200_OK,
    summary="update a Uses"  ,
    tags=["Users"]
)
def update_a_user():
    pass


##Tweet
