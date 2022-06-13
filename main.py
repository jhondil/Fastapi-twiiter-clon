#Python
from typing import Optional, List

#fastApi
from fastapi import (FastAPI,status)

#Models
from models import *

app = FastAPI()


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


@app.get(
    path="/",
    response_model=List[Tweet],
     status_code=status.HTTP_200_OK,
    summary="Show all Tweets"  ,
    tags=["Tweet"]
)
def home():
    return{"Api": "Twitter"}

@app.post(
    path="/post",
    response_model=Tweet, ##responde al usuario
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet"  ,
    tags=["Tweet"]
)
def post():
    pass

@app.get(
    path="/post/{tweet_id}",
    response_model=Tweet, ##responde al usuario
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet"  ,
    tags=["Tweet"]
)
def show_a_tweet():
    pass

@app.delete(
    path="/post/{tweet_id}/delete",
    response_model=Tweet, ##responde al usuario
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet"  ,
    tags=["Tweet"]
)
def delete_a_tweet():
    pass

@app.put(
    path="/post/{tweet_id}/update",
    response_model=Tweet, ##responde al usuario
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet"  ,
    tags=["Tweet"]
)
def update_a_tweet():
    pass



