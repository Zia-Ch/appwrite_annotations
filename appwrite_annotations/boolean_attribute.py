from dataclasses import dataclass
from typing import Optional
from .base import Attribute
from .exceptions import AttributeValidationError

@dataclass
class BooleanAttribute(Attribute):
    """
    Class representing a boolean attribute with an optional default value.
    
    Inherits from:
        Attribute: The base attribute class.
    
    Attributes:
        default (Optional[bool]): Default boolean value for the attribute.
    
    Raises:
        AttributeValidationError: If a default value is provided while the attribute is required.
    """
    
    default: Optional[bool] = None  # Default boolean value for the attribute

    def __post_init__(self):
        """
        Post-initialization validation for the boolean attribute.
        
        Ensures that the default value is not provided if the attribute is marked as required.
        
        Raises:
            AttributeValidationError: If a default value is provided when the attribute is required.
        """
        super().__post_init__()
        
        # If the attribute is required, it should not have a default value.
        if self.required and self.default is not None:
            raise AttributeValidationError("A default value cannot be provided when the attribute is required.")
