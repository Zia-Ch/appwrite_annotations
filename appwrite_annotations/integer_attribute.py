# attribute_annotations/integer_attribute.py
from dataclasses import dataclass
from typing import Optional
from .base import Attribute

@dataclass
class IntegerAttribute(Attribute):
    """
    Class representing an integer attribute with optional min, max, and default values.
    
    Inherits from:
        Attribute: The base attribute class.
    
    Attributes:
        min (Optional[int]): Minimum value for the integer data.
        max (Optional[int]): Maximum value for the integer data.
        default (Optional[int]): Default integer value for the attribute.
    """
    
    min: Optional[int] = None  # Minimum value for the integer attribute
    max: Optional[int] = None  # Maximum value for the integer attribute
    default: Optional[int] = None  # Default value for the integer attribute
