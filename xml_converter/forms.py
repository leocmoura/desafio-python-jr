from django import forms

class ArquivoXMLForm(forms.Form):
    arquivo = forms.FileField(label='Selecione um arquivo XML', widget=forms.ClearableFileInput(attrs={'accept': '.xml'}))
