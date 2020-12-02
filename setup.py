import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-juno',
    version='0.0.3',
    author='Alessandra Carneiro',
    author_email='alessandra@rd2.ventures',
    description='Integração da Juno com Django',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alessandrak/django-juno',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django :: 3.1',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
