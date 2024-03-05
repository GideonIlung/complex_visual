from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt', 'r') as req:
        return [line.strip() for line in req.readlines() if line.strip()]

setup(
    name='complex_visual',
    version='0.1',
    packages=find_packages(),
    install_requires=read_requirements(),
    author='Gideon Ilung',
    author_email='ilunggideon@gmail.com',
    description='libary of tools that can be used to visualise complex functions and transformations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/GideonIlung/complex_visual',
    license='MIT'
)
