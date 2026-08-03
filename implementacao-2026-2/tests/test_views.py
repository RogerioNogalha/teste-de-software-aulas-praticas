import pytest
from django.urls import reverse

from lists.models import Item


@pytest.mark.integration
@pytest.mark.django_db
def test_home_displays_saved_items(client) -> None:  # type: ignore[no-untyped-def]
    Item.objects.create(text="Estudar TDD")

    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert "Estudar TDD" in response.content.decode()


@pytest.mark.integration
@pytest.mark.django_db
def test_post_creates_item_and_redirects(client) -> None:  # type: ignore[no-untyped-def]
    response = client.post(reverse("home"), {"item_text": "Criar teste vermelho"})

    assert response.status_code == 302
    assert Item.objects.get().text == "Criar teste vermelho"


@pytest.mark.integration
@pytest.mark.django_db
def test_post_does_not_create_blank_item(client) -> None:  # type: ignore[no-untyped-def]
    response = client.post(reverse("home"), {"item_text": "   "})

    assert response.status_code == 200
    assert Item.objects.count() == 0
    assert "alert" in response.content.decode()

