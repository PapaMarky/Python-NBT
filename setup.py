from setuptools import setup
from python_nbt import VERSION

setup(
  name             = 'Python-NBT',
  version          = ".".join(str(x) for x in VERSION),
  description      = 'Named Binary Tag Reader/Writer',
  author           = 'TowardtheStars',
  author_email     = 'hty16@mail.ustc.edu.cn',
  url              = 'https://github.com/TowardtheStars/Python-NBT',
  license          = open("LICENSE").read(),
  long_description = open("README.txt").read(),
  packages         = ['python_nbt'],
  classifiers      = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: Python Modules"
  ]
)
