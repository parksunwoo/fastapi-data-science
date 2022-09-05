from datetime import date
from enum import Enum
from typing import List

from pydantic import BaseModel, ValidationError


class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]



try:
    Person(
        first_name="John",
        last_name="Doe",
        gender="INVALID_VALUE",
        birthdate="1991-01-01",
        interests=["travel", "sports"],
        address={
            "street_address": "12 Squirell Street",
            "postal_code": "424242",
            "city": "woodtown",
            # Missing country
        }
    )
except ValidationError as e:
    print(str(e))



# try:
#     Person(
#         first_name="John",
#         last_name="Doe",
#         gender=Gender.MALE,
#         birthdate="1991-13-42",
#         interests=["travel", "sports"],
#     )
# except ValidationError as e:
#     print(str(e))


person = Person(
        first_name="John",
        last_name="Doe",
        gender=Gender.MALE,
        birthdate="1991-01-01",
        interests=["travel", "sports"],
        address={
            "street_address": "12 Squirell Street",
            "postal_code": "424242",
            "city": "woodtown",
            "country": "US",
        }
    )
print(person)













