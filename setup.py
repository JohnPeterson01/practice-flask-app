from setuptools import setup, find_packages

setup(
    name="example-pkg-jp-flask1",
    version="0.0.1",
    author="John Peterson",
    author_email="example@gmail.com",
    description="A small flask package",
    url="https://github.com/JohnPeterson01/practice-flask-app",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'dependency-injector==4.5.1',
        'Flask==1.1.2',
        'Flask-SQLAlchemy==2.4.1',
        'psycopg2==2.8.4',
        'redis==3.5.3',
        'SQLAlchemy==1.3.20',
    ],
    python_requires='>=3.6',
    tests_require=[
        'coverage>=4.0.3',
        'PyHamcrest>=1.9.0',
    ],
    setup_requires=[
        'nose>=1.3.7',
    ],
    entry_points={
        'console_scripts': [
            'runserver = src.main:runserver',
            'create-all = src.main:createall',
            'drop-all = src.main:dropall'
        ],
    },
)