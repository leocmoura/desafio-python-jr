from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from xml_converter.serializer import CreateXMLtoDictAPISerializer


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # "Observe que esta não é uma API RESTful.
    # We still use DRF to assess how well you know the framework
    # Ainda usamos o DRF para avaliar o quanto você conhece bem o framework."
    serializer_class = CreateXMLtoDictAPISerializer
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        return Response({})
