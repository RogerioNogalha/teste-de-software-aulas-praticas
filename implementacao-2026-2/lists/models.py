from django.core.exceptions import ValidationError
from django.db import models


class Item(models.Model):
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at", "id"]

    def clean(self) -> None:
        self.text = self.text.strip()
        if not self.text:
            raise ValidationError({"text": "A tarefa não pode ficar vazia."})

    def save(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.text

