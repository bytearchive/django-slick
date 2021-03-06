import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-slick',
    version=__import__('slick').VERSION,
    description='Slick responsive theme for Django.',
    long_description=read('README.rst'),
    author='Sjoerd Arendsen',
    author_email='subscribe@optixdesigns.com',
    packages=['slick', 'slick.templatetags'],
    url='https://github.com/docc/django-slick/',
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'License :: Free for non-commercial use',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Environment :: Web Environment',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ],
    zip_safe=False,
    install_requires=[
        "django-classy-tags",
        #"https://bitbucket.org/freakypie/django-viewsets/get/master.zip"
    ],
)