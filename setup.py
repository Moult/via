from setuptools import setup

setup(
    name = 'via',
    version = '0.1',
    description = 'Experimental roguelike',
    packages = ['via', 'via.test'],
    entry_points = {
        'console_scripts': ['via = via.app:main']
    }
)
