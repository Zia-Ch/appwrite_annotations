from dataclasses import dataclass
from typing import Optional
from .base import Attribute
from .exceptions import AttributeValidationError

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
    
    Raises:
        AttributeValidationError: If a default value is provided while the attribute is required.
    """
    
    min: Optional[float] = None  # Minimum value for the float attribute
    max: Optional[float] = None  # Maximum value for the float attribute
    default: Optional[float] = None  # Default value for the float attribute

    def __post_init__(self):
        """
        Post-initialization validation for the float attribute.
        
        Ensures that the default value is not provided if the attribute is marked as required.
        
        Raises:
            AttributeValidationError: If a default value is provided when the attribute is required.
        """
        super().__post_init__()
        
        # If the attribute is required, it should not have a default value.
        if self.required and self.default is not None:
            raise AttributeValidationError("A default value cannot be provided when the attribute is required.")
