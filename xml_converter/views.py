from django.http import JsonResponse
from django.shortcuts import render
from xml_converter.forms import ArquivoXMLForm
from xml_converter.converter import *
import json
from xml.etree import ElementTree


def upload_page(request):
    form = ArquivoXMLForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            file = form.cleaned_data['arquivo'].read().decode('utf-8')
            xml_converted = convert_to_dict(file)

            return JsonResponse(xml_converted, safe=False, json_dumps_params={'indent': 4})
    
    return render(request, "upload_page.html", {'form': form})
