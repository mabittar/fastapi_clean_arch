from datetime import datetime

import pytest
from fastapi import HTTPException

from src.application.domain.email import Email
from src.application.domain.item import Item, ItemModel

valid_item = {"item_id": 0, "name": "test", "email": "test@test.com"}


def test_should_return_valid_item_without_optional_params():
    result = Item(**valid_item)
    assert isinstance(result, Item)
    assert isinstance(result.email, Email)
    assert result.email.to_value() == valid_item.get("email")
    assert result.name == valid_item.get("name")


def test_should_return_valid_item_with_all_optional_params():
    valid_item_sut = valid_item.copy()
    valid_item_sut["updated_at"] = datetime.now()
    valid_item_sut["created_at"] = datetime.now()
    result = Item(**valid_item_sut)
    assert isinstance(result, Item)
    assert result.email.to_value() == valid_item_sut.get("email")
    assert result.name == valid_item_sut.get("name")
    assert hasattr(result, "created_at")
    assert hasattr(result, "updated_at")


def test_should_return_valid_ItemModel():
    valid_item_sut = valid_item.copy()
    valid_item_sut["updated_at"] = datetime.now()
    valid_item_sut["created_at"] = datetime.now()
    item = Item(**valid_item_sut)
    result = item.to_model()
    assert isinstance(result, ItemModel)
    assert result.email == valid_item_sut.get("email")
    assert result.name == valid_item_sut.get("name")
    assert hasattr(result, "created_at")
    assert hasattr(result, "updated_at")


@pytest.mark.parametrize("invalid_input", ["test", "test@", "@test", "@test.com", "test.com"])
def test_invalid_email_input_must_raise_error(invalid_input):
    invalid_item_sut = valid_item.copy()
    invalid_item_sut["email"] = invalid_input
    with pytest.raises(HTTPException) as ex:
        Item(**invalid_item_sut)
        assert ex.status_code == 422
        assert ex.detail == "Item invalid email body"
