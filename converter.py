from xml.etree import ElementTree

def convert_to_dict():
    tree = ElementTree.parse("addresses.xml")
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