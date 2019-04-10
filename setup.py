from setuptools import setup, find_packages


install_requires = ['django>=1.7', 'django-easysettings>=1.0,<2.0']

setup(
    name='django-password-policies-iplweb',
    version=__import__('password_policies').__version__,
    description='A Django application to implent password policies.',
    long_description="""\
django-password-policies is an application for the Django framework that
provides unicode-aware password policies on password changes and resets
and a mechanism to force password changes.
""",
    author='Michal Pasternak',
    author_email='michal.dtz@gmail.com',
    url='https://github.com/iplweb/django-password-policies-iplweb',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    install_requires=install_requires,
    test_suite='tests.runtests',
)
