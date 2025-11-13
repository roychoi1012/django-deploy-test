from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import ClickCount


def index(request):
    click_obj, _created = ClickCount.objects.get_or_create(id=1)
    context = {
        "click_count": click_obj.clicks,
    }
    return render(request, "main/index.html", context)


@require_POST
def add_click(request):
    click_obj, _created = ClickCount.objects.get_or_create(id=1)
    click_obj.clicks += 1
    click_obj.save()

    return JsonResponse({"success": True, "new_count": click_obj.clicks})