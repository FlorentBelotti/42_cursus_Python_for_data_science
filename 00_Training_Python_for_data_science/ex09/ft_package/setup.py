from setuptools import setup, find_packages


setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/eagle/ft_package",
    author="FlorentBelotti",
    author_email="fbelotti@student.42perpignan.fr",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
