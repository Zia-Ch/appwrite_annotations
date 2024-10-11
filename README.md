# Appwrite Annotations
A Python library for defining and annotating class attributes with custom metadata for appwrite.

**Appwrite Annotations** is a Python package that simplifies the creation of collections and attributes in Appwrite. Instead of manually creating collections and attributes through the Appwrite dashboard, users can now simply write Python model classes with custom annotations. This package allows users to define collections and attributes in their code, and with a single script execution, all the collections and attributes will be automatically created in Appwrite.

## Why Use Appwrite Annotations?

When building an app with Appwrite, defining collections and their attributes is a time-consuming process. Typically, developers:
- Write the front-end data model classes.
- Then, they navigate to the Appwrite dashboard to manually create collections and add attributes.

This package eliminates that repetitive process. With **Appwrite Annotations**, you only need to annotate your Python model classes, and the package will handle the rest, creating the corresponding collections and attributes in Appwrite.
You just need to run a script as given below:

### Key Features
- Automatically create collections and attributes in Appwrite based on Python class annotations.
- Support for a variety of attribute types, including `String`, `Integer`, `Float`, `Boolean`, `Datetime`, `Enum`, `Relationship`, `Email`, and `IP Address`.
- Define validation rules, default values, and constraints directly in your model classes.
- Handle both simple and complex attributes like arrays and relationships between collections.
  
## Installation

```bash
pip install appwrite_annotations

```
## How It Works

 **1. Define Your Model Classes**

Write your model classes in Python and annotate their attributes using the provided classes from Appwrite Annotations.

**2. Run the Script**

Once the model classes are written, run the provided script to automatically sync your data models with Appwrite. The script will create collections and attributes based on the annotations in your Python classes.

## Example Usage
**1. Define Your Model Classe**

```python
from appwrite_annotations import StringAttribute, IntegerAttribute, BooleanAttribute

@dataclass
class Student:
    student_id: IntegerAttribute = IntegerAttribute(attribute_key="studentId", required=True)
    name: StringAttribute = StringAttribute(attribute_key="name", required=True, size=100)
    age: IntegerAttribute = IntegerAttribute(attribute_key="age", required=True, min=18, max=100)
    is_active: BooleanAttribute = BooleanAttribute(attribute_key="isActive", default=True)

```

Developed by [Zia Ur Rahman](https://www.linkedin.com/in/zia-ur-rahman-ch/)

Email: [ziaurrahmanchoudhary@gmail.com](mailto:ziaurrahmanchoudhary@gmail.com)

