#Python
from email import message
import json

from typing import Optional, List

from uuid import UUID


#fastApi
from fastapi import (FastAPI, HTTPException, Path,status, Body, Form)



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
def signup(user: UserRegister = Body(...)):
    with open("users.json", "r+", encoding="utf-8" ) as f:
        result = json.loads(f.read()) # lee el archivo y lo convierte en json json.loads()
        user_dict = user.dict() #convierte en diccionario las respuesta del body
        ## confierto estos datos en json = user_id,birth_date
        user_dict["user_id"]= str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        
        result.append(user_dict)
        f.seek(0) ## lo mueve al primer bit del archivo
        f.write(json.dumps(result))
        return user
    
    
@app.post(
    path="/LoginOut",
    response_model=LoginOut, ##responde al usuario
    status_code=status.HTTP_200_OK,
    summary="Login a Uses"  ,
    tags=["Users"]
)
def login(email: EmailStr = Form(...), password: str = Form(...)):
    with open("users.json", "r+", encoding="utf-8" ) as f:
        result = json.loads(f.read())
        
        # print(result)
        for user in result:
            
            
            # print(user.values())
            
            if email in  user.values():
                
                return LoginOut(email=email, password=password, message="Login Successfully!")
            else:
                return LoginOut(email=email, password=password, message="Login Failed!")
        f.seek(0)    ## lo mueve al primer bit del archivo

@app.get(
    path="/users",
    response_model=List[User], ##responde al usuario
    status_code=status.HTTP_200_OK,
    summary="show all Uses"  ,
    tags=["Users"]
)
def show_all_user():
    with open ("users.json", "r", encoding="utf-8") as f:
        result = json.loads(f.read())
        return result
        

@app.get(
    path="/users/{user_id}",
    response_model=User, ##responde al usuario
    status_code=status.HTTP_200_OK,
    summary="show a Uses"  ,
    tags=["Users"]
)
def show_a_user(
    user_id: UUID = Path(...)
):
    
    with open ("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        # return result
        id = str(user_id)

    for d in results:
        if d["user_id"] == id:
            return d
        
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"??This user_id doesn't exist!")
        


@app.delete(
    path="/users/{user_id}/delete",
    response_model=User, ##responde al usuario
    status_code=status.HTTP_200_OK,
    summary="Delete a Uses"  ,
    tags=["Users"]
)
def delete_a_user(user_id: UUID = Path(...)
):
    with open ("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        # return result
        id = str(user_id)

    for d in results:
        if d["user_id"] == id:
            results.remove(d)
            with open("users.json", "w", encoding="utf-8") as f:
                f.seek(0)
                f.write(json.dumps(results))
            return d
        
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"??This user_id doesn't exist!")

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
     with open ("tweets.json", "r", encoding="utf-8") as f:
        result = json.loads(f.read())
        return result
    

@app.post(
    path="/post",
    response_model=Tweet, ##responde al usuario
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet"  ,
    tags=["Tweet"]
)
def post(tweet: Tweet = Body(...)):
    with open("tweets.json", "r+", encoding="utf-8" ) as f:
        result = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"]= str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["update_at"] = str(tweet_dict["update_at"])     
        tweet_dict["by"]["user_id"]= str(tweet_dict["by"]["user_id"])     
        tweet_dict["by"]["birth_date"]= str(tweet_dict["by"]["birth_date"])     
        result.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(result))
        return tweet

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



