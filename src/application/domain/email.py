import re

from fastapi import HTTPException, status


class Email:
    def __init__(self, email):
        if not self.is_valid(email):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Item invalid email body",
            )
        self.email = email

    @staticmethod
    def is_valid(email):
        # Use uma expressão regular para validar o formato do e-mail
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None

    def to_value(self) -> str:
        return self.email
