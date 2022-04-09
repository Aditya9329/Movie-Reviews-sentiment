from django import forms

class GetText(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    