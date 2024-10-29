# All our database related operations go here

from enum import Enum
from peewee import (
    MySQLDatabase,
    Model,
    FloatField,
    IntegerField,
    CharField,
    ForeignKeyField,
)

db = MySQLDatabase(
    "defaultdb",
    user="<your_db_admin>",
    password="<your_db_password>",
    host="<your_host_here>",
    port=26979,
)


class Sex(Enum):
    MALE = 1
    FEMALE = 2


class Education(Enum):
    GRADUATE = 1
    UNIVERSITY = 2
    HIGH_SCHOOL = 3
    OTHERS = 4


class MaritalStatus(Enum):
    MARRIED = 1
    SINGLE = 2
    OTHERS = 3


class PaymentDefault(Enum):
    YES = 1
    NO = 0


class User(Model):
    class Meta:
        database = db


class PaymentData(Model):
    class Meta:
        database = db
