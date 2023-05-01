from setuptools import setup

setup(
    name = 'snj_lib',
    version = '1.0.0',
    description = 'snj pip install library',
    url = 'https://github.com/Shopping-n-joy/Shopping-N-Joy.git',
    author = 'Dennis12ax',
    author_email = "test",
    license = "Dennis12ax",
    packages = ['snj_lib'],
    zip_safe = False,
    install_requires = [
        'openai==0.27.5',
        'python-dotenv == 1.0.0'
    ]
)