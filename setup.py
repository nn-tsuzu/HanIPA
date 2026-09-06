from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="HanIPA",
    version="1.0",
    description="Hangul to IPA convertor",
    author="nn-tsuzu",
    url="https://github.com/nn-tsuzu/HanIPA.git",
    packages=find_packages("hanipa"),
    package_dir={"": "hanipa"},
    py_modules=[splitext(basename(path))[0] for path in glob('hanipa/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt')
)

