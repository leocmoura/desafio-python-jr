from rest_framework import serializers
from models import ArquivoXML

class ArquivoXMLSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = ArquivoXML
