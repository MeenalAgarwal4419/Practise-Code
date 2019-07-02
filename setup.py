import setuptools

with open("./README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="url_shortner_pm",
    version="0.1.1",
    author=["Prinzu Choudhury","Meenal Agarwal"],
    author_email="prinzupallab@gmail.com",
    description="A package to shorten the url",
    long_description="ShortStr is a Python module to generate distinct, homoglyph-less 'shortstrings' for URL shortners and similar services",
    long_description_content_type="text/markdown",
    url="https://github.com/MeenalPrinzu/url_shortner_pm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
