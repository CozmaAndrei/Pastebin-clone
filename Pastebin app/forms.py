from django import forms
from .models import Text
       
class TextForm(forms.ModelForm): #clasa TextForm mosteneste clasa ModelForm din modulul forms
    '''Aceasta clasa construieste un formular pentru a putea introduce textul in coloana content din tabelul nostru'''
    class Meta:
        model = Text
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your text here...'})
        }