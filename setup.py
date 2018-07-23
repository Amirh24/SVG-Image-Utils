from setuptools import setup

setup(name='svgappender',
      description='A lightweight Python SVG parser that focuses on correctly layering SVG images',
      long_description='When appending SVGs, the name selectors in the style tag and class paths are the same in both the base template and the appended SVG images. '
                       'As a result, an abnormal looking SVG image will be created. '
                       ''
                       'SVG Appender modifies attributes that contradict each other between all the appended SVGs and thus outputs a'
                       'new, intuitive looking layered SVG image.',
      version='0.1.2',
      py_modules=['svgappender'],
      install_requires=[
          'lxml',
          'cssutils'
      ],
      url='https://github.com/Amirh24/SVG-Appender.git',
      author='A. Hagafny',
      author_email='amirh18@gmail.com',
      license='MIT',
      )
