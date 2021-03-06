"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['nat20.py']
DATA_FILES = ['sheet.yaml', 'd20.gif']
OPTIONS = {'argv_emulation': True, 'iconfile': 'nat20.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
