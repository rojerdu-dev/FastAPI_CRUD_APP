from typing import List
from uuid import uuid4

import uvicorn
from fastapi import FastAPI

from models import Gender, Role, User

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
        roles=[Role.user]
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
