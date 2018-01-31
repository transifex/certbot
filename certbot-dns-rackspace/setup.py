import sys

from distutils.core import setup
from setuptools import find_packages

version = '0.1.dev0'

install_requires = [
    'acme=={0}'.format(version),
    'certbot=={0}'.format(version),
    'pyrax',
    # For pkg_resources. >=1.0 so pip resolves it to a version cryptography
    # will tolerate; see #2599:
    'setuptools>=1.0',
    'zope.interface',
]

test_requires = [
    'mock',
]

setup(
    name='certbot-dns-rackspace',
    version=version,
    description="Rackspace CloudDNS Authenticator plugin for Certbot",
    url='https://github.com/certbot/certbot',
    author="Certbot Project",
    author_email='client-dev@letsencrypt.org',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    keywords=['certbot', 'rackspace'],
    entry_points={
        'certbot.plugins': [
            'dns-rackspace = certbot_dns_route53.dns_rackspace:Authenticator',
            'certbot-rackspace:auth = certbot_dns_rackspace.authenticator:Authenticator'
        ],
    },
    test_suite='certbot_dns_rackspace',
    test_requires=test_requires,
)
