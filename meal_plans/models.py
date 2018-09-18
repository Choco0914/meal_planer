from django.db import models

class Week(models.Model):
    """일주일을 정의한다."""
    day = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """모델에 관한 정보를 문자열 형태로 반환한다."""
        return self.day

class Meal(models.Model):
    """요일별 식단에 대해 정의하는 클래스."""
    day = models.ForeignKey(Week, on_delete = models.CASCADE)
    meal = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'contents'

    def __str__(self):
        """모델에 관한 정보를 문자열 형태로 반환한다."""
        if self.meal[:] > self.meal[:50]:
            return self.meal[:50] + "..."
        else:
            return self.meal[:]
