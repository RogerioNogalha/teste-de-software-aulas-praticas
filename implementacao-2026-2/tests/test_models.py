import pytest
from django.core.exceptions import ValidationError

from lists.models import Item


@pytest.mark.unit
@pytest.mark.django_db
def test_item_removes_surrounding_spaces() -> None:
    item = Item.objects.create(text="  estudar PyTest  ")

    assert item.text == "estudar PyTest"


@pytest.mark.unit
@pytest.mark.django_db
def test_item_rejects_blank_text() -> None:
    with pytest.raises(ValidationError):
        Item.objects.create(text="   ")

