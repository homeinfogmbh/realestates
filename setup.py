#! /usr/bin/env python3

from setuptools import setup


setup(
    name="realestates",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    python_requires=">=3.8",
    author="HOMEINFO - Digitale Informationssysteme GmbH",
    author_email="<info@homeinfo.de>",
    maintainer="Richard Neumann",
    maintainer_email="<r.neumann@homeinfo.de>",
    install_requires=["flask", "mdb", "openimmodb", "wsgilib"],
    py_modules=["realestates"],
    description="Real estates API.",
)
