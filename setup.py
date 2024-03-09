from setuptools import setup, find_packages

setup(
    name='weather_sdk',
    version='1.0.0',
    author="Kirill Artyukovskij",
    author_email="artyukovskiikirill7@mail.ru",
    description='SDK for accessing weather data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Indi77erence/my_weather_sdk',
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11'
    ],
)
