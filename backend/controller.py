from fastapi import FastAPI
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from model import *
from dtos import UserDto
from secrets import token_hex
from hashlib import sha256
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

def connect_with_schema():
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5001","http://127.0.0.1:5002"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/cadastre")
def cadastre(name: str, email: str, password: str) -> dict:
    """
    return 0:
        cadastred with success
    return 1:
        password not valid
    return 2:
        User already exist
    return 3:
        Internal server error    
    """

    if len(password) < 6:
        return {"status": 1}

    session = connect_with_schema()

    user_exist = session.query(User).filter_by(name=name, email=email).all()

    if len(user_exist) > 0:
        return {"status": 2}

    try:

        user = User(name=name, email=email, password=password)
        session.add(user)
        session.commit()

        return {"status": 0}

    except Exception as e:
        return {"status": 3, "error": e}


@app.post("/login")
def login(name: str, password: str) -> dict:
    """
        return 4:
            User not found
        return 5:
            Login performed with success

    """

    session = connect_with_schema()

    exist_user = session.query(User).filter_by(
        name=name, password=password).all()

    if exist_user == 0:
        return {"status": 4}

    token = token_hex(50)
    exist_token = session.query(Token).filter_by(token=token).all()

    if len(exist_token) == 0:
        user_exist_in_token = session.query(
            Token).filter_by(user_id=exist_user[0].id).all()

        if len(user_exist_in_token) == 0:
            newToken = Token(user_id=exist_user[0].id, token=token)
            session.add(newToken)

        elif len(user_exist_in_token) > 0:
            user_exist_in_token[0].token = token

        session.commit()

    passw_cryptography = sha256(password.encode()).hexdigest()

    userDto = UserDto(exist_user[0], passw_cryptography)

    return {"status": 5,
            "user": userDto}


if __name__ == '__main__':
    uvicorn.run("controller:app", port=5000, reload=True, access_log=False)
