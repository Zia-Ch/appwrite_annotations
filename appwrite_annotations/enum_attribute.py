from dataclasses import dataclass
from typing import List, Optional
from .base import Attribute
from .exceptions import AttributeValidationError

@dataclass
class EnumAttribute(Attribute):
    """
    Class representing an enumeration attribute, allowing only predefined values.

    Inherits from:
        Attribute: The base attribute class.

    Attributes:
        elements (List[str]): A list of allowed elements (whitelisted values) for this attribute.
                              Maximum of 100 elements, each 255 characters long.
        default (Optional[str]): Default value for the enum attribute. Cannot be set if required is True.
    """
    
    elements: List[str]  # Array of allowed elements for enumeration
    default: Optional[str] = None  # Default value for the enum attribute, must be within elements

    def __post_init__(self):
        """
        Post-initialization processing to validate the enum elements.

        Ensures that the list of elements does not exceed the allowed size and length constraints.

        Raises:
            AttributeValidationError: If the elements list exceeds the limit of 100 or if an element is longer than 255 characters.
        """
        super().__post_init__()
        if len(self.elements) > 100:
            raise AttributeValidationError("The 'elements' list can have a maximum of 100 elements.")
        if any(len(element) > 255 for element in self.elements):
            raise AttributeValidationError("Each element in 'elements' can have a maximum length of 255 characters.")
        if self.default and self.default not in self.elements:
            raise AttributeValidationError(f"The default value '{self.default}' is not in the list of allowed elements.")
