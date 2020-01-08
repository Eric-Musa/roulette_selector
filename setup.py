from setuptools import setup

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name="roulette",
    version="0.0.1",
    author="Eric Musa",
    author_email="eric.musa17@gmail.com",
    description="A small roulette-style random selector of weighted options",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)