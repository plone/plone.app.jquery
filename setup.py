from setuptools import setup, find_packages

version = '1.11.2'

setup(
    name='plone.app.jquery',
    version=version,
    description="jQuery integration for Plone",
    long_description="%s%s" % (
        open("README.rst").read() + "\n",
        open("CHANGES.rst").read(),
    ),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Plone jQuery',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='http://pypi.python.org/pypi/plone.app.jquery',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone', 'plone.app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFCore',
        'Products.GenericSetup',
    ],
    entry_points="""
        [z3c.autoinclude.plugin]
        target = plone
    """,
    extras_require={'test': ['plone.app.testing']},
)
