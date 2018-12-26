import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyUtils",
    version="0.0.1",
    author="Anderson Paschoalon",
    author_email="anderson.paschoalon@gmail.com",
    description="This simple package was made to simplify and turn some frequent tasks easier and less verbose.",
    long_description="This simple package was made to simplify and turn some frequent tasks easier and less verbose.",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
)