from pathlib import Path

from importlib.machinery import SourceFileLoader
from setuptools import setup

description = "DataFrame to protobuf serialisation"
readme = Path(__file__).parent.parent / "README.md"
if readme.exists():
    long_description = readme.read_text()
else:
    long_description = description
# avoid loading the package before requirements are installed:
version = SourceFileLoader("version", "pandas_pbf/version.py").load_module()

setup(
    name="pandas_pbf",
    version=version.VERSION,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
    author="Connor Charles",
    author_email="",
    url="https://github.com/ccharlesgb/pandas-pbf",
    license="MIT",
    packages=["pandas_pbf"],
    zip_safe=True,
    entry_points=None,
    install_requires=["click>=6.7", "pandas>1.0"],
    extras_require={"watch": ["watchgod>=0.4"]},
)
