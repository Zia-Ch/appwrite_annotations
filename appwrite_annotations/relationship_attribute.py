from dataclasses import dataclass
from typing import Optional
from .base import Attribute
from .exceptions import AttributeValidationError

@dataclass
class RelationshipAttribute(Attribute):
    """
    Class representing a relationship attribute, defining relationships between two collections.

    Inherits from:
        Attribute: The base attribute class.

    Attributes:
        related_collection_id (str): The ID of the related collection.
        type (str): The type of relationship (e.g., 'one-to-one', 'one-to-many', 'many-to-one', or 'many-to-many').
        two_way (bool): Indicates whether the relationship is two-way (bidirectional).
        two_way_key (Optional[str]): The attribute key for the two-way relationship, if applicable.
        on_delete (Optional[str]): Specifies behavior when the related record is deleted (e.g., 'cascade', 'restrict', 'set-null').
    """
    
    related_collection_id: str  # The ID of the related collection
    type: str  # Type of relationship
    two_way: bool = False  # Indicates if the relationship is two-way
    two_way_key: Optional[str] = None  # Attribute key for two-way relationship, if applicable
    on_delete: Optional[str] = None  # Behavior on deletion of related record

    def __post_init__(self):
        """
        Post-initialization validation for the relationship attribute.

        Ensures the relationship type is valid and checks the constraints on `two_way_key` and `on_delete` fields.

        Raises:
            AttributeValidationError: If the relationship type is invalid or if constraints are violated.
        """
        super().__post_init__()
        valid_types = ['one-to-one', 'one-to-many', 'many-to-one', 'many-to-many']
        valid_on_delete = ['cascade', 'restrict', 'set-null']

        # Validate the type of relationship
        if self.type not in valid_types:
            raise AttributeValidationError(f"Invalid relationship type: '{self.type}'. Must be one of {valid_types}.")
        
        # Validate the on_delete behavior
        if self.on_delete and self.on_delete not in valid_on_delete:
            raise AttributeValidationError(f"Invalid on_delete behavior: '{self.on_delete}'. Must be one of {valid_on_delete}.")
        
        # If two-way relationship, two_way_key must be provided
        if self.two_way and not self.two_way_key:
            raise AttributeValidationError(f"Two-way relationship requires 'two_way_key' to be defined.")
