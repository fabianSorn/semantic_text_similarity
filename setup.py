#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

# Not pinning tensorflow package versions might lead to incompatibilities
requirements = ["tensorflow==2.2.0rc3",
                "tensorflow_text==2.2.0rc2",
                "tensorflow_hub==0.8.0",
                "numpy",
                "matplotlib",
                "seaborn"]

setup_requirements = ["pytest-runner", ]

test_requirements = ["pytest>=3", ]

setup(
    author="Fabian Sorn",
    author_email="fabian.sorn@icloud.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Some Project for testing the semantic similarity between two sentences.",
    entry_points={
        "console_scripts": [
            "semtextsim=semtextsim.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords="semtextsim",
    name="semtextsim",
    packages=find_packages(include=["semtextsim", "semtextsim.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/fabianSorn/semtextsim",
    version="0.1.0",
    zip_safe=False,
)
