from random import randint
import pytest

from src.application.usecase.item_create import CreateItemUsecase
from src.controller.v1.schema.item_schema import ItemSchema


@pytest.fixture()
async def usecase(session):
    return await CreateItemUsecase(session)


def make_valid_input():
    input_dict = {
        "item_id": randint(1, 1000), 
        "name": "Test Item", 
        "email": "test@example.com"
        }
    return ItemSchema(**input_dict)

@pytest.mark.asyncio
async def test_item_creation(usecase):
    valid_input = make_valid_input()
    result = await usecase.execute(valid_input)
    assert isinstance(result, ItemSchema)
    