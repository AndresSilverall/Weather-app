from django import forms


class SearchCity(forms.Form):
    city = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"class": "form"}))
    