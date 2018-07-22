from setuptools import setup

setup(name='SVGAppender',
      description='A lightweight Python SVG parser that focuses on correctly layering SVG images',
      version='0.1.0',
      scripts=['SVGAppender/SVGAppender.py'],
      py_modules=['SVGAppender'],
      install_requires=[
          'lxml',
          'cssutils'
      ],
      url='https://github.com/Amirh24/SVGAppender.git',
      author='A. Hagafny',
      author_email='amirh18@gmail.com',
      license='MIT',
      )
