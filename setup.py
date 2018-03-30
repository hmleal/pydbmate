from setuptools import setup


setup(
    name='pydbmate',
    author='Henrique Leal',
    author_email='hm.leal@hotmail.com',
    version='0.0.1.dev0',
    description='Another python migration tool',
    packages=['pydbmate'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    license='MIT',
    entry_points={'console_scripts': ['pydbmate = pydbmate.__main__:main']},
)
