from django import forms


class NewsForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    category = forms.CharField(max_length=50)

