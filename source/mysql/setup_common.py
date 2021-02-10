import os
import sys
import ast
from pathlib import Path
from setuptools import find_packages

ORG = "intel"
NAME = "dffml-source-mysql"
DESCRIPTION = "DFFML Source for MySQL Protocol"
AUTHOR_NAME = "Sudharsana K J L"
AUTHOR_EMAIL = "kjlsudharsana@gmail.com"

IMPORT_NAME = (
    NAME
    if "replace_package_name".upper() != NAME
    else "replace_import_package_name".upper()
).replace("-", "_")

SELF_PATH = Path(sys.argv[0]).parent.resolve()
if not (SELF_PATH / Path(IMPORT_NAME, "version.py")).is_file():
    SELF_PATH = os.path.dirname(os.path.realpath(__file__))

VERSION = ast.literal_eval(
    Path(SELF_PATH, IMPORT_NAME, "version.py")
    .read_text()
    .split("=")[-1]
    .strip()
)

README = Path(SELF_PATH, "README.md").read_text()

KWARGS = dict(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    maintainer="John Andersen",
    maintainer_email="johnandersenpdx@gmail.com",
    url=f"https://github.com/{ORG}/dffml/blob/master/source/{NAME}/README.md",
    license="MIT",
    keywords=["dffml"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
