from typing import List
from uuid import UUID, uuid4

import uvicorn
from fastapi import FastAPI, HTTPException

from models import Gender, Role, UpdateUser, User

app = FastAPI()
db: List[User] = [
    User(
        id=uuid4(),
        first_name="Thomas",
        last_name="Anderson",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Elizabeth",
        last_name="Carter",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Simon",
        last_name="Bennet",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Gabrielle",
        last_name="Taylor",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Michael",
        last_name="Davis",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
]


@app.get("/")
async def root():
    return {"greeting": "Hello World!"}


@app.get("/api/v1/users")
async def get_users():
    return db


@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
        raise HTTPException(
            status_code=404, detail=f"Delete user failed, id {id} not found."
        )


@app.put("/api/v1/users/{id}")
async def update_user(user_update: UpdateUser, id: UUID):
    for user in db:
        if user.id == id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user.id
        raise HTTPException(status_code=404, detail=f"Couldn't find user with id: {id}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
