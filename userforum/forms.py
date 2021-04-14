from django import forms

class AddArticleForm(forms.Form):
    title = forms.CharField(label='Название статьи', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Текст статьи', widget=forms.TextInput(attrs={'class': 'form-control', 'row': '15'}))
    
