#!/usr/bin/python3
"""
Module task_03_xml
Contains functions to serialize and deserialize dictionaries using XML
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file
    Args:
        dictionary (dict): Data to serialize
        filename (str): Name of the output file
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary
    Args:
        filename (str): Name of the input file
    Returns:
        dict: The reconstructed dictionary
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text
            
        return result_dict
    except Exception:
        return None
