from setuptools import setup

setup(
    name="roulette_selector",
    version="0.0.1",
    author="Eric Musa",
    author_email="eric.musa17@gmail.com",
    description="A small roulette-style random selector of weighted options",
    url="https://bitbucket.org/Eric-Musa/roulette/",
    py_modules=['roulette_selector'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
