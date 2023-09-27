from django.http import JsonResponse
from django.shortcuts import render
from xml_converter.forms import ArquivoXMLForm
from xml_converter.converter import *
from rest_framework.generics import CreateAPIView
from xml_converter.serializer import CreateXMLtoDictAPISerializer

def upload_page(request):
    form = ArquivoXMLForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            file = form.cleaned_data['file']
            xml_converted = convert_to_dict(file)

            return JsonResponse(xml_converted)
    
    return render(request, "upload_page.html", {'form': form})

class CreateXMLtoDictAPI(CreateAPIView):
    serializer_class = CreateXMLtoDictAPISerializer
