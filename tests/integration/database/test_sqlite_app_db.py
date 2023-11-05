from random import randint
import sqlite3
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.application.usecase.item_create import CreateItemUsecase
from src.controller.v1.schema.item_schema import ItemSchema
from src.infra.database.pg_adapter import Base

@pytest.fixture(scope='function')
def setup_database():

    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


def make_valid_input():
    input_dict = {
        "item_id": randint(1, 1000), 
        "name": "Test Item", 
        "email": "test@example.com"
        }
    return ItemSchema(**input_dict)

# @pytest.mark.anyio
async def test_item_creation(setup_database):
    sut: CreateItemUsecase = CreateItemUsecase(setup_database)
    valid_input = make_valid_input()
    result = await sut.execute(valid_input)
    assert isinstance(result, ItemSchema)
    