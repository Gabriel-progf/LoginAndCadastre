from model import *


class UserDto(User):
    def __init__(self, user: User, passw_cryptography) -> None:
        self.name = user.name
        self.email = user.email
        self.password = passw_cryptography

    def __repr__(self) -> str:
        return {
            "Name": self.name,
            "Email": self.email,
            "Password": self.password
        }
