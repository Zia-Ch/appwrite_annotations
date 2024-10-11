# attribute_annotations/float_attribute.py
from dataclasses import dataclass
from typing import Optional
from .base import Attribute

@dataclass
class FloatAttribute(Attribute):
    """
    Class representing a float attribute with optional min, max, and default values.
    
    Inherits from:
        Attribute: The base attribute class.
    
    Attributes:
        min (Optional[float]): Minimum value for the float data.
        max (Optional[float]): Maximum value for the float data.
        default (Optional[float]): Default float value for the attribute.
    """
    
    min: Optional[float] = None  # Minimum value for the float attribute
    max: Optional[float] = None  # Maximum value for the float attribute
    default: Optional[float] = None  # Default value for the float attribute
