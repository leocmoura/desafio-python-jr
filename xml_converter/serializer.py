from rest_framework import serializers
from rest_framework.serializers import  FileField, JSONField 
from xml_converter.models import ArquivoXML
from xml_converter.converter import convert_to_dict

class CreateXMLtoDictAPISerializer(serializers.Serializer):
    file = FileField()
    converted_data = JSONField(read_only=True)

    def create(self, validated_data):
        file = validated_data.pop("file")
        converted_data = convert_to_dict(file)
        validated_data['converted_data'] = converted_data
        return validated_data

