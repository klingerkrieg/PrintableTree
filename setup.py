from setuptools import setup, find_packages
 
setup(name='PrintableTree',
      packages=['src'],
      version='0.4',
      url='https://github.com/klingerkrieg/PrintableTree',
      download_url='https://github.com/klingerkrieg/PrintableTree/archive/refs/tags/0.4.tar.gz',
      license='MIT',
      author='Alan Klinger',
      author_email='klingerkrieg@gmail.com',
      description='It has an implementation of a tree in python and methods that print the tree to an image through OpenCV / É uma implementação de uma árvore em python com métodos que permitem imprimir a árvore através do OpenCV',
      long_description=open('README.md').read(),
      zip_safe=False,
      install_requires=[            # I get to this in a second
          'opencv-python',
          'numpy',
          'matplotlib',
      ])