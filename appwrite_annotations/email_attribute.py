from dataclasses import dataclass
from typing import Optional

from .exceptions import AttributeValidationError
from .base import Attribute

@dataclass
class EmailAttribute(Attribute):
    """
    Class representing an email attribute, enforcing a valid email format.

    Inherits from:
        Attribute: The base attribute class.

    Attributes:
        default (Optional[str]): Default email address for the attribute.
    """
    
    default: Optional[str] = None  # Default email value for the attribute

    def __post_init__(self):
        """
        Post-initialization validation for email format.

        Ensures that if a default value is provided, it follows the basic email format.

        Raises:
            ValueError: If the default email does not match a basic email format.
        """
        super().__post_init__()
        if self.default and not self._is_valid_email(self.default):
            raise AttributeValidationError(f"Invalid default email format: '{self.default}'.")

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """
        Validates the email format using a simple regex pattern.
        
        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email format is valid, False otherwise.
        """
        import re
        email_pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(email_pattern, email) is not None
