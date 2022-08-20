from setuptools import setup
import subprocess

setup(name='secret_package2',
      version='1.0.0',
      description='package desc',
      url='package url',
      author='package Author',
      author_email='package Author email',
      license='MIT',
      packages=['secret_package2'],
      zip_safe=False)
