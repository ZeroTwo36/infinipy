from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='infinipy',
  version='0.0.2',
  description='A very basic API Wrapper around IBL\'s API',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='ZeroTwo36',
  author_email='zerotwo36@protonmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['ibl','infinipy','infinity','dbl','discord','discord-botlist'], 
  packages=find_packages(),
  install_requires=[''] 
)
