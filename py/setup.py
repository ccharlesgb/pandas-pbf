from pathlib import Path

from importlib.machinery import SourceFileLoader
from setuptools import setup

description = "DataFrame to protobuf serialisation"
readme = Path(__file__).parent / "README.md"
if readme.exists():
    long_description = readme.read_text()
else:
    long_description = description
# avoid loading the package before requirements are installed:
version = SourceFileLoader("version", "arq/version.py").load_module()

setup(
    name="arq",
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
    author="Samuel Colvin",
    author_email="s@muelcolvin.com",
    url="https://github.com/samuelcolvin/arq",
    license="MIT",
    packages=["arq"],
    package_data={"arq": ["py.typed"]},
    zip_safe=True,
    entry_points="""
        [console_scripts]
        arq=arq.cli:cli
    """,
    install_requires=[
        "async-timeout>=3.0.0",
        "aioredis>=1.1.0",
        "click>=6.7",
        "pydantic>=1",
        'dataclasses>=0.6;python_version == "3.6"',
        'typing-extensions>=3.7;python_version < "3.8"',
    ],
    extras_require={"watch": ["watchgod>=0.4"]},
)
