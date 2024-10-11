from dataclasses import dataclass
from typing import Optional
from .base import Attribute
from .exceptions import AttributeValidationError

@dataclass
class IPAddressAttribute(Attribute):
    """
    Class representing an IP address attribute, supporting both IPv4 and IPv6 formats.

    Inherits from:
        Attribute: The base attribute class.

    Attributes:
        default (Optional[str]): Default IP address for the attribute.
    """
    
    default: Optional[str] = None  # Default IP address for the attribute

    def __post_init__(self):
        """
        Post-initialization validation for IP address format.

        Ensures that if a default value is provided, it follows either IPv4 or IPv6 format.

        Raises:
            ValueError: If the default IP does not match a valid IPv4 or IPv6 format.
        """
        super().__post_init__()
        if self.default and not self._is_valid_ip(self.default):
            raise AttributeValidationError(f"Invalid default IP address format: '{self.default}'.")

    @staticmethod
    def _is_valid_ip(ip: str) -> bool:
        """
        Validates the IP address format (both IPv4 and IPv6).

        Args:
            ip (str): The IP address to validate.

        Returns:
            bool: True if the IP address is valid, False otherwise.
        """
        import re
        ipv4_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4}|:)$"
        return re.match(ipv4_pattern, ip) is not None or re.match(ipv6_pattern, ip) is not None
