from setuptools import setup

setup(
    name='bv-syndication-dr',
    version='0.1',
    py_modules=['bv-syndication-dr'],
    install_requires=[
        'Click', 'SQLAlchemy',
    ],
    entry_points='''
        [console_scripts]
        bv-syndication-dr=investigate:cli
    ''',
)