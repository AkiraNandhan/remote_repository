from django import forms


class InsertingDataForm(forms.Form):
    product_id=forms.IntegerField(
        label="Enter your product Id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your product Id'
            }
        )
    )
    product_name=forms.CharField(
        label="Enter your product Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your product Name'
            }
        )
    )
    product_cost=forms.IntegerField(
        label="Enter your product cost",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your product Cost'
            }
        )
    )
    product_color=forms.CharField(
        label="Enter your product color",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your product color'
            }
        )

    )
    product_class=forms.CharField(
        label="Enter your product class",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your product class'
            }
        )
    )
    customer_name=forms.CharField(
        label="Enter your customer name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'customer name'
            }
        )
    )
    customer_mobile=forms.IntegerField(
        label="Enter your customer mobile number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'customer mobile'
            }
        )
    )
    customer_email=forms.EmailField(
        label="customer email id",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'customer email'
            }
        )
    )
class UpdatingDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter your product Id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your product Id'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter your product cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your product Cost'
            }
        )
    )

class DeletingDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter your product Id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your product Id'
            }
        )
    )





























