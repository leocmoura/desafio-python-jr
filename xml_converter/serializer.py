from rest_framework import serializers
from xml_converter.models import ArquivoXML

class ArquivoXMLSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = ArquivoXML
        fields = '__all__'
