
from setuptools import setup

setup(
    name="BitBar Worklog",
    author="Paul Traylor",
    url="http://github.com/kfdm/bitbar-worklog/",
    packages=["worklog"],
    install_requires=["python-frontmatter"],
    entry_points={
        "console_scripts": [
            "worklog.bitbar = worklog.bitbar:main",
            "open.alfred = worklog.open:main",
            "worklog.alfred = worklog.worklog:main",
            "worklog.jekyll = worklog.import.jekyll:main",
        ]
    },
)
