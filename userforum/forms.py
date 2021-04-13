from django import forms

class AddArticleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': '15'}))
    
