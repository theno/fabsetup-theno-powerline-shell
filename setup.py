"""Setup and install termdown

Addon for fabsetup (https://github.com/theno/fabsetup).
"""

import os
import os.path
from setuptools import setup, find_packages
from codecs import open


def create_readme_with_long_description():
    '''Try to convert content of README.md into rst format using pypandoc,
    write it into README and return it.

    If pypandoc cannot be imported write content of README.md unchanged into
    README and return it.
    '''
    this_dir = os.path.abspath(os.path.dirname(__file__))

    readme_md = os.path.join(this_dir, 'README.md')
    readme = os.path.join(this_dir, 'README')

    if os.path.exists(readme_md):
        # this is the case when running `python setup.py sdist`
        if os.path.exists(readme):
            os.remove(readme)

        try:
            import pypandoc
            long_description = pypandoc.convert(readme_md, 'rst', format='md')
        except(ImportError):
            with open(readme_md, encoding='utf-8') as in_:
                long_description = in_.read()

        with open(readme, 'w') as out:
            out.write(long_description)
    else:
        # this is in case of `pip install fabsetup-x.y.z.tar.gz`
        with open(readme, encoding='utf-8') as in_:
            long_description = in_.read()

    return long_description


this_dir = os.path.abspath(os.path.dirname(__file__))
filename = os.path.join(this_dir, 'fabsetup_theno_termdown', '_version.py')
with open(filename, 'rt') as fh:
    version = fh.read().split('"')[1]

description = __doc__.split('\n')[0]
long_description = create_readme_with_long_description()

setup(
    name='fabsetup-theno-powerline-shell',
    version=version,
    description=description,
    long_description=long_description,
    url='https://github.com/theno/fabsetup-theno-powerline-shell',
    author='Theodor Nolte',
    author_email='fabsetup@theno.eu',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='python development utilities library',
    packages=find_packages(exclude=[
        'contrib',
        'docs',
        'tests',
    ]),
    include_package_data=True,
    install_requires=[
        'fabric',
        'fabsetup',
    ],
    extras_require={
        'dev': ['pypandoc'],
    }
)
