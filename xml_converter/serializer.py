from rest_framework import serializers
from rest_framework.serializers import  FileField, JSONField 
from xml_converter.converter import convert_to_dict

class CreateXMLtoDictAPISerializer(serializers.Serializer):
    class Meta:
        fields = ['file']
        
    file = FileField()
    converted_data = JSONField(read_only=True)

    def create(self, validated_data):
        validated_data["converted_data"] = convert_to_dict(validated_data["file"])
        return validated_data