from django import forms


class AddProductForm(forms.Form):
    제품수량 = forms.IntegerField()
    is_update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
