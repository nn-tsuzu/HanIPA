from setuptools import setup

DESCRIPTION = 'Hangul-to-IPA: Hangul to IPA convertor'
NAME = 'Hangul-to-IPA'
AUTHOR = 'nn-tsuzu'
URL = 'https://github.com/nn-tsuzu/Hangul-to-IPA'
LICENSE = 'apache2.0'
DOWNLOAD_URL = URL
VERSION = '1.0'
PYTHON_REQUIRES = '>=3.10'
INSTALL_REQUIRES = [
    "g2pk2",
    "jamo"
]
PACKAGES = [
    'Hangul-to-IPA'
]
KEYWORDS = 'hangul ipa nlp'
CLASSIFIERS=[
    'License :: OSI Approved :: Apache 2.0 License',
    'Programming Language :: Python :: 3.10'
]
with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    maintainer=AUTHOR,
    url=URL,
    download_url=URL,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    keywords=KEYWORDS,
    install_requires=INSTALL_REQUIRES
)