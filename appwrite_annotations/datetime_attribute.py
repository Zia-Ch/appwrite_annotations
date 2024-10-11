# attribute_annotations/datetime_attribute.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from .base import Attribute

@dataclass
class DatetimeAttribute(Attribute):
    """
    Class representing a datetime attribute with an optional default value.
    
    Inherits from:
        Attribute: The base attribute class.
    
    Attributes:
        default (Optional[str]): Default datetime value for the attribute in ISO 8601 format.
    """
    default: Optional[str] = None  # Default datetime value for the attribute
