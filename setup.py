from setuptools import setup

setup(name='pkg',
      description='A lightweight Python SVG parser that focuses on correctly layering SVG images',
      version='0.1.0',
      scripts=['pkg/pkg.py'],
      py_modules=['pkg'],
      install_requires=[
          'lxml',
          'cssutils'
      ],
      url='https://github.com/Amirh24/pkg.git',
      author='A. Hagafny',
      author_email='amirh18@gmail.com',
      license='MIT',
      )
