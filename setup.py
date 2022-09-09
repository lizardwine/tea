from setuptools import setup

from pie import __version__

with open('README.md', 'r') as reader:
    readme = reader.read()

setup(
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    name='pie-cli',
    description='Pie, a complete version control.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/jaedsonpys/pie',
    license='GPL v3.0',
    version=__version__,
    packages=['pie'],
    python_requires='>=3.7',
    install_requires=['utokeniz'],
    keywords=['version', 'control', 'versioning', 'file'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Software Development :: Version Control'
    ]
)
