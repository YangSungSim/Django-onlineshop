from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product
from coupon.forms import AddCouponForm
from .forms import AddProductForm
from .cart import Cart

# 노출될 제품들은 카트 자체로부터 가져오는데 제품수량 수정을 위해서 addproduct래그을 제품마다 하나씩 추가
# Create your views here.

@require_POST
def add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)

    form = AddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],is_update=cd['is_update'])

    return redirect('cart:detail')

def remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart:detail')


def detail(request):
    cart = Cart(request)
    add_coupon = AddCouponForm()
    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'quantity':product['quantity'],'is_update':True})
    return render(request,'cart/detail.html',{'cart':cart, 'add_coupon':add_coupon})

