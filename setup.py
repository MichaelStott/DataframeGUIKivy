import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdfkivygui",
    version="0.1.0",
    author="Jeffrey Padfield",
    author_email="",
    description="Package that enables the user to use Pandas Dataframe inside Kivy Apps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jefpadfi/PandasDataframeGUIKivy",
    keywords=["Kivy", "Pandas DataFrame", "Graphs"],
    packages=setuptools.find_packages(),
    install_requires=[
        "certifi",
        "chardet",
        "cycler",
        "docutils",
        "idna",
        "Kivy",
        "Kivy-Garden",
        "kiwisolver",
        "matplotlib",
        "numpy",
        "pandas",
        "Pillow",
        "Pygments",
        "pyparsing",
        "python-dateutil",
        "pytz",
        "requests",
        "six",
        "urllib3",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
