from setuptools import setup

setup(
    name="secret_package2",
    install_requires=[
        "importlib-metadata; python_version < '3.8'"
    ],
)
