import os
from setuptools import setup, find_packages

HERE = os.path.dirname(os.path.abspath(__file__))
DESCRIPTION = 'This Django application simplifies adding a captcha to a model or form using Recaptcha'
LONG_DESCRIPTION = open(os.path.join(HERE, 'README.md')).read()

setup(
    name='recaptchapp',
    version='0.1',
    packages=find_packages(),
    author='Potato London',
    url='https://github.com/potatolondon/Recaptchapp',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    install_requires=[],
)