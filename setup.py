"""
OpenCMISS ZincWidgets

A collection of Qt widgets and utilities building on the Python bindings for the OpenCMISS-Zinc Visualisation Library.
"""
import io
import os
import re

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'src', 'opencmiss', 'utils', '__init__.py')) as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')


classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)
Programming Language :: Python
Operating System :: Microsoft :: Windows
Operating System :: Unix
Operating System :: MacOS :: MacOS X
Topic :: Scientific/Engineering :: Medical Science Apps.
Topic :: Scientific/Engineering :: Visualization
Topic :: Software Development :: Libraries :: Python Modules
"""

doc_lines = __doc__.split("\n")

requires = ['opencmiss.utils >= 0.2.0', 'PySide2']

setup(
    name='opencmiss.zincwidgets',
    version=version,
    author='H. Sorby',
    author_email='h.sorby@auckland.ac.nz',
    packages=['opencmiss', 'opencmiss.zincwidgets'],
    platforms=['any'],
    url='https://github.com/OpenCMISS-Bindings/opencmiss.zincwidgets/',
    license='Apache Software License',
    packages=find_packages("src"),
    package_dir={"": "src"},
    description=doc_lines[0],
    classifiers=filter(None, classifiers.split("\n")),
    install_requires=requires,
)
