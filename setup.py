from setuptools import setup

setup(
    name="secret_package",
    install_requires=[
        "importlib-metadata; python_version < '3.8'",
        "subprocess.run"
    ],
)
