
from setuptools import setup

setup(
    name='BitBar Worklog',
    author='Paul Traylor',
    url='http://github.com/kfdm/bitbar-worklog/',
    packages=['worklog'],
    entry_points={
        'console_scripts': [
            'worklog.5m.py = worklog:main[bitbar]',
            'open.alfred = worklog.open:main[alfred]',
            'worklog.alfred = worklog.worklog:main[alfred]',
        ]
    },
    extras_require={
        'alfred': [],
        'bitbar': [],
    },
)
