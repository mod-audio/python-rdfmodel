from setuptools import setup, find_packages
import os

setup(name = 'python-lv2',
      version = '0.1',
      description = 'Library to extract structured data from LV2 TTL files',
      long_description = open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
      author = "Luis Fagundes",
      author_email = "lhfagundes@hacklab.com.br",
      license = "The MIT License",
      packages = find_packages(),
      install_requires = ['rdflib'],
      classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Sound/Audio',
        ],
      url = 'https://github.com/portalmod/python-lv2',
      
)
