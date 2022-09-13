# from https://docs.python.org/3/distutils/setupscript.html
# from distutils.core import setup
# setup(
#     packages=['code']
#     )

# from https://setuptools.pypa.io/en/latest/userguide/entry_point.html
from setuptools import setup

setup(
    name="csv",
    version="1.0.0",
    packages=["code", "test"],
    # entry_points={
    #     'console_scripts': [
    #       'code = code.cli:main',  
    #       'tests = test.text_csv:main'
    #     ]
    # }
)
