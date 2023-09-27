from xml.etree import ElementTree

def convert_to_dict(arquivo):
    # xml_file = io.StringIO(arquivo) # objeto de arquivo temporário a partir do conteúdo XML
    tree = ElementTree.parse(arquivo)
    root = tree.getroot()
    result = xml_to_dict(root, [])
    return {root.tag: result}

def xml_to_dict(xml, result: list) -> dict:
    for child in xml:
        if len(child) == 0:
            key_value = {child.tag: child.text}
            result.append(key_value)
        else:
            key_value = {child.tag: xml_to_dict(child, [])}
            result.append(key_value)

    return result if result else ""
