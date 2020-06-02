from django import forms
class ProductInsertForm(forms.Form):
    pid=forms.IntegerField(
        label='Enter ID:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'ID'
            }
        )
    )
    pname=forms.CharField(
        label='Enter Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )
    pcost=forms.IntegerField(
        label='Enter Cost:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )
    pcolor=forms.CharField(
        label='Enter Color:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )
    pclass=forms.CharField(
        label='Enter Class:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )
    cname=forms.CharField(
        label='Customer Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Name'
            }
        )
    )
    cmob=forms.IntegerField(
        label='Mobile Number:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Mobile'
            }
        )
    )
    cemail=forms.EmailField(
        label='Email:',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Email'
            }
        )
    )
class ProductUpdateForm(forms.Form):
    pid = forms.IntegerField(
        label='Enter ID:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ID'
            }
        )
    )
    pcost = forms.IntegerField(
        label='Enter Cost:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Cost'
            }
        )
    )
class ProductDeleteForm(forms.Form):
    pid = forms.IntegerField(
        label='Enter ID:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ID'
            }
        )
    )

