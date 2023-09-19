from django.http import JsonResponse
from django.shortcuts import render
from xml_converter.forms import ArquivoXMLForm
import xml.etree.ElementTree as ET

def convert_to_dict(request):
    xml_file = ArquivoXMLForm(request.POST, request.FILES)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    result = xml_to_dict(root, [])

    from pprint import pprint
    pprint(
        {root.tag: result}
    )

def xml_to_dict(xml, result: list) -> dict:
    for child in xml:
        if len(child) == 0:
            key_value = {child.tag: child.text}
            result.append(key_value)
        else:
            key_value = {child.tag: xml_to_dict(child, [])}
            result.append(key_value)

    return result

def upload_page(request):
    if request.method == 'POST':
        form = ArquivoXMLForm(request.POST, request.FILES)
        if form.is_valid():
            xml_file = request.FILES['arquivo'].read().decode('utf-8')
            try:
                json_data = convert_to_dict(xml_file)
                return JsonResponse(json_data)
            except Exception as e:
                return JsonResponse({'error': "Erro na conversão de XML para JSON: {}".format(str(e))}, status=400)    
    else:
        form = ArquivoXMLForm()
    return render(request, "upload_page.html", {'form': form})

# def xml_to_dict(element):
    
#     if len(element) == 0:
#         return element.text
#     result = {}
#     for child in element:
#         child_data = xml_to_dict(child)
#         if child.tag in result:
#             if isinstance(result[child.tag], list):
#                 result[child.tag].append(child_data)
#             else:
#                 result[child.tag] = [result[child.tag], child_data]
#         else:
#             result[child.tag] = child_data
#     return result

# def convert_xml_to_json(xml_string):
#     root = ET.fromstring(xml_string)
#     data = xml_to_dict(root, [])
#     from pprint import pprint
#     pprint(
#         {root.tag: data}
#     )
#     return json.dumps(data)
