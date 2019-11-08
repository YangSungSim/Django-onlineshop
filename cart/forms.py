from django import forms

class AddProductForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
    #상세페이지에서 추가할 때(false)와 장바구니(true)
    #에서 수량을 바꿀 때 동작하는 방식을 달리함.
