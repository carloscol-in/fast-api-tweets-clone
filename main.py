import json
from typing import List

from fastapi import FastAPI
from fastapi import status
from fastapi import Body
from fastapi import HTTPException

from models import User, Tweet, UserRegister

app = FastAPI()


# Path operations

## Users

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(user: UserRegister = Body(...)):
    """
    # Create a user

    This path operation is used to create a user in the app.

    Parameters:
        - Request Body parameter
            - user: UserRegister
    
    Returns a json object with the basic user information:
    * user_id: UUID
    * email: EmailStr
    * first_name: str
    * last_name: str
    * birth_date: date
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user


@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented"
    )

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    """This path operation shows all users in the app.

    Parameters:
        -

    Returns a JSON list with all the users in the app, with the following keys:
    * user_id: UUID
    * email: EmailStr
    * first_name: str
    * last_name: str
    * birth_date: date
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results

@app.delete(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["Users"]
)
def delete_user():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented"
    )

@app.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["Users"]
)
def update_user():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented"
    )

## Tweets

@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
)
def home():
    return {"Twitter API": "Working"}

@app.get(
    path="/tweet/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_tweet():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented"
    )

@app.post(
    path="/tweet",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post_tweet():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented"
    )

@app.delete(
    path="/tweet/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def post_tweet():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented"
    )

@app.put(
    path="/tweet/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def post_tweet():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Method not implemented"
    )