from dataclasses import dataclass
from typing import Optional
from .base import Attribute
from .exceptions import AttributeValidationError

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
    
    Raises:
        AttributeValidationError: If a default value is provided while the attribute is required.
    """
    
    min: Optional[int] = None  # Minimum value for the integer attribute
    max: Optional[int] = None  # Maximum value for the integer attribute
    default: Optional[int] = None  # Default value for the integer attribute

    def __post_init__(self):
        """
        Post-initialization validation for the integer attribute.
        
        Ensures that the default value is not provided if the attribute is marked as required.
        
        Raises:
            AttributeValidationError: If a default value is provided when the attribute is required.
        """
        super().__post_init__()
        
        # If the attribute is required, it should not have a default value.
        if self.required and self.default is not None:
            raise AttributeValidationError("A default value cannot be provided when the attribute is required.")
