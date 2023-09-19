import xml.etree.ElementTree as ET
import json

# Carregue o arquivo XML
tree = ET.parse('addresses.xml')  # Substitua 'seuarquivo.xml' pelo nome do seu arquivo XML
root = tree.getroot()

# Função para converter elemento XML em dicionário
def element_to_dict(element):
    result = {}
    if len(element) == 0:
        return element.text
    for child in element:
        child_data = element_to_dict(child)
        if child.tag in result:
            if isinstance(result[child.tag], list):
                result[child.tag].append(child_data)
            else:
                result[child.tag] = [result[child.tag], child_data]
        else:
            result[child.tag] = child_data
    if not result:
        return element.text
    return result

# Converte o elemento raiz (root) em um dicionário
json_data = element_to_dict(root)

# Converte o dicionário em uma string JSON
json_string = json.dumps(json_data, indent=4)  # Indent é opcional para formatação

# Imprime a string JSON
print(json_string)
