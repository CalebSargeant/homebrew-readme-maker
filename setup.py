from setuptools import setup, find_packages

setup(
    name="readme",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests", "pyyaml"],
    entry_points={
        "console_scripts": [
            "readme=readme.main:main",
        ]
    },
)