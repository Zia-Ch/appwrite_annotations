# attribute_annotations/string_attribute.py
from dataclasses import dataclass
from typing import Optional
from .base import Attribute

@dataclass
class StringAttribute(Attribute):
    """
    Class representing a string attribute with optional size and default value.
    
    Inherits from:
        Attribute: The base attribute class.
    
    Attributes:
        size (Optional[int]): Optional size constraint for the string data.
        default (Optional[str]): Default string value for the attribute.
    """
    
    
    size: Optional[int] = None  # Optional size constraint for the string
    default: Optional[str] = None  # Default value for the string attribute
