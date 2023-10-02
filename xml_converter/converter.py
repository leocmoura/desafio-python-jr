from xml.etree import ElementTree
from xml.etree import ElementTree as ET

def convert_to_dict(file):
    try:
        tree = ElementTree.parse(file)
        root = tree.getroot()
        result = xml_to_dict(root, [])
        return {root.tag: result} if result else {'Root': ''}
    except ET.ParseError as e:
        return {'error': 'converter XML invalido.'}

def xml_to_dict(xml, result: list) -> dict:
    for child in xml:
        if len(child) == 0:
            key_value = {child.tag: child.text}
            result.append(key_value)
        else:
            key_value = {child.tag: xml_to_dict(child, [])}
            result.append(key_value)

    return result if result else ""
