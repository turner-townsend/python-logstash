from distutils.core import setup
setup(
    name='python-logstash',
    packages=['logstash'],
    version='0.4.7',
    description='Python logging handler for Logstash.',
    long_description=open('README.rst').read(),
    author='Chris Gearing/Robert Young',
    author_email='chris.gearing@turntown.com/robert.young@turntown.com',
    url='https://github.com/turner-townsend/python-logstash',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Logging',
    ]
)
