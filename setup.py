'''
https://github.com/1hef001/Pypack/blob/master/README.md
'''

from setuptools import setup

dependencies = []
setup(
    name='mera_photo',
    version='0.1.6',
    url='https://github.com/1hef001/Pypack',
    license='MIT',
    author='S Ashwin',
    author_email='ashwins1211@gmail.com',
    description='pip clone with migration facility',
    long_description=__doc__,
    packages=['pypack'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    scripts=['pypack/main.py'],
    install_requires=dependencies,
    

    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)