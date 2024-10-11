from setuptools import setup, find_packages

setup(
    name="appwrite_annotations",  # Name of your package on PyPI
    version="0.1.0",  # Initial release version
    description="A Python library for defining and annotating class attributes with custom metadata for appwrite.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Zia Ur Rahman",
    author_email="ziaurrahmanchoudhary@gmail.com",
    url="https://github.com/Zia-Ch/appwrite_annotations",  # Project URL
    packages=find_packages(),  # Automatically finds all Python modules
    install_requires=[],  # List any dependencies here
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
