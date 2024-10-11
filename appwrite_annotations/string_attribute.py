from dataclasses import dataclass
from typing import Optional
from .base import Attribute
from .exceptions import AttributeValidationError

@dataclass
class StringAttribute(Attribute):
    """
    Class representing a string attribute with optional size, default value, and encryption option.
    
    Inherits from:
        Attribute: The base attribute class.
    
    Attributes:
        size (int): Attribute size for text attributes, in number of characters.
        default (Optional[str]): Default string value for the attribute.
        encrypt (Optional[bool]): Toggle encryption for the attribute. 
                                   Encryption enhances security by not storing any plain text values in the database.
                                   However, encrypted attributes cannot be queried.
    
    Raises:
        AttributeValidationError: If a default value is provided while the attribute is required.
    """
    
    size: int  # Attribute size for text attributes, in number of characters.
    default: Optional[str] = None  # Default value for the string attribute
    encrypt: Optional[bool] = False  # Toggle encryption for the attribute

    def __post_init__(self):
        """
        Post-initialization validation for the string attribute.
        
        Ensures that the default value is not provided if the attribute is marked as required.
        
        Raises:
            AttributeValidationError: If a default value is provided when the attribute is required.
        """
        super().__post_init__()

        # If the attribute is required, it should not have a default value.
        if self.required and self.default is not None:
            raise AttributeValidationError("A default value cannot be provided when the attribute is required.")
        
        # Ensure the size is positive
        if self.size <= 0:
            raise AttributeValidationError("Size must be a positive integer.")
