from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    use_from=  models.DateTimeField() # 사용 기한
    use_to = models.DateTimeField() #사용 시작일
    amount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100000)])
    #금액 할인쿠폰
    active = models.BooleanField()

    def __str__(self):
        return self.code