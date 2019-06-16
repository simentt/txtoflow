import setuptools

setuptools.setup(
    name="txtoflow",
    version="0.1.0",
    author="Krishna",
    author_email="krishna.vijay4444@gmail.com",
    description="Library to generate flowcharts from pseudo code",
    long_description=open('README.md').read(),
    platforms=['any'],
    license='MIT License',
    long_description_content_type="text/markdown",
    url="https://krishkasula.github.io/txtoflow",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
