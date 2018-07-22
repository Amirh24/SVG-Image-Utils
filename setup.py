from setuptools import setup

setup(name='svgappender',
      description='A lightweight Python SVG parser that focuses on correctly layering SVG images',
      long_description='When appending SVGs, a contradiction soon follows at the form of same name selectors in the style tag and class paths. SVG Appender modifies attributes that contradict each other between all the appended SVGs and as a result generates a new layered SVG image.',
      version='0.1.1',
      py_modules=['svgappender'],
      install_requires=[
          'lxml',
          'cssutils'
      ],
      url='https://github.com/Amirh24/SVGAppender.git',
      author='A. Hagafny',
      author_email='amirh18@gmail.com',
      license='MIT',
      )
