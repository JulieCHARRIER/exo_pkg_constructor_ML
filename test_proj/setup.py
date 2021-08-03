from setuptools import setup, find_packages

setup(
    name='test_proj',
    version='0.0.1',
    packages=find_packages(),
    scripts=['scripts/test_script'],
    requirements=['numpy', 'pandas', 'matplotlib', 'seaborn', 'scikit-learn', 'fastapi', 'pytest']
    )