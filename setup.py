import re
from pathlib import Path

from setuptools import find_packages, setup

with open(Path("correios") / "__init__.py", encoding="utf-8") as fh:
    version = re.search(r'__version__ = "(.*?)"', fh.read(), re.M).group(1)


setup(
    name="Rastreio Correios",
    version=version,
    url="https://github.com/rennancockles/rastreio-correios",
    project_urls={
        "Source Code": "https://github.com/rennancockles/rastreio-correios",
        "Documentation": "https://rastreio-correios.r3ck.com.br",
    },
    license="MIT",
    author="Rennan Cockles",
    author_email="rcdev@hotmail.com.br",
    description="Rastreamento de pacotes do correio",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.8",
    install_requires=["fastapi", "requests"],
    keywords=["correios", "ect", "rastreio", "rastreamento", "track"],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development",
        "Typing :: Typed",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
