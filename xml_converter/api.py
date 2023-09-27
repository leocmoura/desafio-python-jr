from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from xml_converter.serializer import CreateXMLtoDictAPISerializer


class ConverterViewSet(ViewSet):
    parser_classes = [MultiPartParser]
    serializer_class = CreateXMLtoDictAPISerializer

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        return Response({})
