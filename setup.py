import hangman
import sys
from setuptools import setup

if sys.version_info.major < 3 or (sys.version_info.minor < 6
                                  and sys.version_info.major == 3):
    sys.exit('Python < 3.6 is unsupported.')

with open('README.md', encoding='utf8') as file:
    long_description = file.read()

setup(
    name='hangman',
    version=hangman.__version__,
    author=hangman.__author__,
    author_email='james@taran.biz',
    url='https://github.com/jlaguma/hangman',
    packages=['hangman'],
    package_data={},
    install_requires=[],
    license='GNU GPLv3',
    description='Hangman Game',
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={'console_scripts': ['hangman = hangman.hangman:hangman']},
)
