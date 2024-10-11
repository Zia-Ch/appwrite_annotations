# attribute_annotations/base.py
from dataclasses import dataclass
import re

# Custom exception for validation
from .exceptions import AttributeValidationError

# Regular expression to validate the attribute key
ATTRIBUTE_KEY_PATTERN = re.compile(r"^[a-zA-Z0-9._-]+$")

# Base Attribute class with common fields
@dataclass
class Attribute:
    """
    Base class representing a generic attribute with common metadata.
    
    Attributes:
        attribute_key (str): The unique key for this attribute, must follow naming conventions.
        required (bool): Indicates whether this attribute is mandatory. Defaults to False.
        array (bool): Indicates whether this attribute should act as an array. Defaults to False.
    """
    
    
    attribute_key: str  # Unique identifier for the attribute
    required: bool = False  # Indicates if the attribute is mandatory
    array: bool = False  # Indicates if the attribute should act as an array

    def __post_init__(self):
        """
        Post-initialization processing to validate the attribute key after object creation.
        
        Raises:
            AttributeValidationError: If the attribute key does not match the required pattern.
        """
        
        if not ATTRIBUTE_KEY_PATTERN.match(self.attribute_key):
            raise AttributeValidationError(f"Invalid attribute key: '{self.attribute_key}'. "
                                           "Allowed characters: alphanumeric, hyphen, non-leading underscore, period.")
