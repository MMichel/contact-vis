from distutils.core import setup

setup(
    name='ContactVis',
    version='0.1.1',
    author='M. Michel',
    author_email='guy.inkognito42@gmail.com',
    packages=['contactvis', 'contactvis.parsing', 'contactvis.test'],
    url='https://github.com/MMichel/contact-vis.git',
    license='LICENSE.txt',
    description='Contact map plotting for predicted protein residue-residue contacts.',
    long_description=open('README.md').read(),
    install_requires=[
        "Biopython >= 1.59",
        "matplotlib >= 1.3.1",
    ],
)
