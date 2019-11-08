from django.shortcuts import render,redirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Coupon
from .forms import AddCouponForm

# Create your views here.

@require_POST
def add_coupon(request):
    now = timezone.now()
    form = AddCouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']

        try:
            #iexact 대소문자 구분없이 일치시킴. get filter를 이용해 데이터를 찾을 때는
            #각 필드명__ 옵션 형태로 질의.
            coupon = Coupon.objects.get(code__iexact=code,use_from__lte=now,use_to__gte=now,active=True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
        return redirect('cart:detail')
