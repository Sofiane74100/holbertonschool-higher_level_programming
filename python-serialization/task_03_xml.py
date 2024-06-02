import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    # Create the root element
    root = ET.Element("data")
    
    # Iterate through the dictionary items and add them as child elements
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)
    
    # Write the XML tree to the provided filename
    tree = ET.ElementTree(root)
    try:
        with open(filename, 'wb') as xml_file:
            tree.write(xml_file, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"Error serializing to XML: {e}")
        return False

def deserialize_from_xml(filename):
    """Deserialize an XML file to a dictionary."""
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Construct the dictionary from XML elements
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text
        
        return dictionary
    except Exception as e:
        print(f"Error deserializing from XML: {e}")
        return None
