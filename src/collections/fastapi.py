from fastapi import FastAPI

app = FastAPI()

obj = {
    "email_id": "test@gmail.com"
}

@app.get("/users/me/{email_id}")
async def read_user_me(email_id: str):
    return obj


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}