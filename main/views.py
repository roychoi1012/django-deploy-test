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
    # POST 요청만 처리합니다.
    if request.method == 'POST':
        click_obj = ClickCount.objects.get(id=1)
        # 카운트 1 증가
        click_obj.clicks += 1
        # 데이터베이스에 저장
        click_obj.save()
        
        # 저장 후, 새로 업데이트된 카운트 값을 JSON 형태로 반환합니다. <-- 수정된 부분
        return JsonResponse({
            'success': True,
            'new_count': click_obj.clicks
        })
        
    # POST 요청이 아니면 메인 페이지로 돌려보냅니다.
    return redirect('main:index')