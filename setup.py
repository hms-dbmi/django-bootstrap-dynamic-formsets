import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bootstrap-dynamic-formsets',
    version='1.0.0',
    packages=['django_bootstrap_dynamic_formsets','django_bootstrap_dynamic_formsets.templatetags'],
    install_requires=['Django','django-bootstrap3',],
    include_package_data=True,
    license='MIT License',
    description='JavaScript-enhanced dynamic formsets using Bootstrap',
    url='https://github.com/hms-dbmi/django-bootstrap-dynamic-formsets',
    author='Daniel Weis',
    author_email='weisd@th-brandenburg.de',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
