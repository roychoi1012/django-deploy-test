from django.db import models

# 카운트 값을 저장할 모델 정의
class ClickCount(models.Model):
    # 'clicks' 필드는 정수형으로, 0을 기본값으로 설정
    clicks = models.IntegerField(default=0)

    # Django 관리자 페이지에서 객체를 알아보기 쉽게 표시하는 메서드
    def __str__(self):
        return f"Current Clicks: {self.clicks}"