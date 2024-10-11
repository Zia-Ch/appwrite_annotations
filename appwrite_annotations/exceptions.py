# attribute_annotations/exceptions.py
class AttributeValidationError(Exception):
    """
    Custom exception raised when an attribute key does not match the required validation pattern.
    
    This is typically raised during the initialization of an Attribute object if the attribute key
    does not meet the allowed character constraints.
    """
    
    pass
