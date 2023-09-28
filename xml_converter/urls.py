from django.urls import path
from xml_converter.views import CreateXMLtoDictAPI

urlpatterns = [
    path('converter/convert/', CreateXMLtoDictAPI.as_view()),
]