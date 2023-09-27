from django import forms

class ArquivoXMLForm(forms.Form):
    file = forms.FileField(label='Selecione um arquivo XML', widget=forms.ClearableFileInput(attrs={'accept': '.xml'}))
