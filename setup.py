from setuptools import setup, find_packages

setup(
    name = "pythonpackagetemplate",
    version = "0.0.1", 
    author = "kurapaty",
    author_email = "akshaykurpaaty@gmail.com",
    description = "Template to Package Python Code",
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # List your package dependencies here
        "setuptools",
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11.8"

)