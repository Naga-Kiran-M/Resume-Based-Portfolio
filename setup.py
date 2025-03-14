# setup.py: Package Setup File

from setuptools import setup, find_packages

setup(
    name='resume_based_portfolio',
    version='1.0.0',
    author='Naga Kiran Machiraju',
    author_email='nagakiranm2021@gmail.com',
    description='A portfolio project showcasing ML & Signal Processing expertise.',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'tensorflow',
        'torch',
        'opencv-python',
        'scikit-learn',
        'seaborn',
        'wfdb',
        'ultralytics'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
