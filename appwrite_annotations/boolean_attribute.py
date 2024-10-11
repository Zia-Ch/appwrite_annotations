# attribute_annotations/boolean_attribute.py
from dataclasses import dataclass
from typing import Optional
from .base import Attribute

@dataclass
class BooleanAttribute(Attribute):
    """
    Class representing a boolean attribute with an optional default value.
    
    Inherits from:
        Attribute: The base attribute class.
    
    Attributes:
        default (Optional[bool]): Default boolean value for the attribute.
    """
    default: Optional[bool] = None  # Default value for the boolean attribute
