from setuptools import setup, find_packages

setup(
    name="iqoption_auto",
    version="0.1.0",
    description="Unofficial Python library for automating trades on IQ Option.",
    author="riadh-BNB",
    author_email="riadhbnb250@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "iqoptionapi"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
