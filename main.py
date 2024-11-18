from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

users ={'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def register(username: Annotated[str, Path(min_length= 5, max_length=20, description='Enter username', example= 'UrbanUser')],
                       age:int = Path(ge=18, le=120, description='Enter age', example= '24')) -> dict:
    string = str(int(max(users, key=int)) +1)
    new_message = f"Имя: {username}, возраст: {age}"
    users[string] = new_message
    return {"message": f"User {string} is registered"}

@app.put('/user/{user_id}/{username}/{age}')
async def update(username: Annotated[str, Path(min_length= 5, max_length=20, description='Enter username', example= 'UrbanUser')],
                       age: int = Path(ge=18, le=120, description='Enter age', example= '24'), user_id: int = Path(ge=0)) -> dict:
    users[user_id] =f" Имя: {username}, возраст: {age}"
    return {"message": f"The user {user_id} is updated"}

@app.delete('/user/{user_id}')
async def delete_users(user_id: int = Path(ge=0)):
    if user_id in users:
        users.pop(user_id)
        return f"User {user_id} has been deleted"
    else:
        raise HTTPException(status_code=404, detail="Пользователь не найден.")
