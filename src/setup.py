import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LoggyLogger",
    version="1.0.1",
    author="Eric Shih",
    author_email="eric12345566@gmail.com",
    description="Convenient, friendly and clean logger for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eric12345566/loggy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Logging"
    ],
    python_requires='>=3',
)