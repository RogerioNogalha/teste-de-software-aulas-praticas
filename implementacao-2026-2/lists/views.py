from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .models import Item


def home_page(request: HttpRequest) -> HttpResponse:
    error = ""
    if request.method == "POST":
        item = Item(text=request.POST.get("item_text", ""))
        try:
            item.save()
        except Exception as exc:  # exercício: substituir por exceção específica
            error = str(exc)
        else:
            return redirect("home")

    return render(request, "lists/home.html", {"items": Item.objects.all(), "error": error})

