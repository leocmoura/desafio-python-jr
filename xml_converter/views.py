from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from xml_converter.forms import ArquivoXMLForm
from xml_converter.converter import *
from xml_converter.serializer import CreateXMLtoDictAPISerializer

def upload_page(request):
    form = ArquivoXMLForm(request.POST, request.FILES)
    if request.method == 'POST':
        try:
            if form.is_valid():
                file = form.cleaned_data['file']
                xml_converted = convert_to_dict(file)
                return JsonResponse(xml_converted)
        except Exception as e:
            return JsonResponse({'error': 'Arquivo XML invalido.'}, status=HTTP_400_BAD_REQUEST)
    
    return render(request, "upload_page.html", {'form': form})

# def upload_page(request):
#     form = ArquivoXMLForm(request.POST, request.FILES)
#     if request.method == 'POST':
#         if form.is_valid():
#             file = form.cleaned_data['file']
#             xml_converted = convert_to_dict(file)

#             if 'error' in xml_converted:
#                 return JsonResponse(xml_converted, status=HTTP_400_BAD_REQUEST)
#             else:
#                 return JsonResponse(xml_converted)
    
#     return render(request, "upload_page.html", {'form': form})

class CreateXMLtoDictAPI(CreateAPIView):
    serializer_class = CreateXMLtoDictAPISerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(None, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data["converted_data"], status=HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Arquivo XML invalido.'}, status=HTTP_400_BAD_REQUEST)
