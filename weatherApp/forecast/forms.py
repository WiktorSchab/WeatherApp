from django import forms


class LocationForm(forms.Form):
    location = forms.CharField(
        max_length=64,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'City'})
    )
