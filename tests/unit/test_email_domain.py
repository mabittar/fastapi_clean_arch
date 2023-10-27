import pytest
from fastapi import HTTPException

from src.application.domain.email import Email


def test_should_return_valid_email():
    result = Email("test@test.com")
    assert result.to_value() == "test@test.com"


@pytest.mark.parametrize("invalid_input", ["test", "test@", "@test", "@test.com", "test.com"])
def test_invalid_email_input_must_raise_error(invalid_input):
    with pytest.raises(HTTPException) as ex:
        Email(invalid_input)
        assert ex.status_code == 422
        assert ex.detail == "Item invalid email body"
