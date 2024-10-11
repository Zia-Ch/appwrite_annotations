"""
This is the appwrite_annotations package.

It contains classes for defining and managing annotated attributes for Appwrite collections. 
Supported attribute types include strings, integers, floats, booleans, and datetimes.

Modules:
    - base: Contains the base attribute class and validation logic.
    - string_attribute: Defines the StringAttribute class for string-based attributes.
    - integer_attribute: Defines the IntegerAttribute class for integer-based attributes.
    - float_attribute: Defines the FloatAttribute class for float-based attributes.
    - boolean_attribute: Defines the BooleanAttribute class for boolean-based attributes.
    - datetime_attribute: Defines the DatetimeAttribute class for datetime-based attributes.
    - exceptions: Contains custom exceptions related to attribute validation.
"""

from .base import Attribute
from .string_attribute import StringAttribute
from .integer_attribute import IntegerAttribute
from .float_attribute import FloatAttribute
from .boolean_attribute import BooleanAttribute
from .datetime_attribute import DatetimeAttribute
from .exceptions import AttributeValidationError

__all__ = [
    "Attribute",
    "StringAttribute",
    "IntegerAttribute",
    "FloatAttribute",
    "BooleanAttribute",
    "DatetimeAttribute",
    "AttributeValidationError"
]
