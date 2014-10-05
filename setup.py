from setuptools import setup


setup(name = 'mist',
      version = '0.1.0',
      author = 'Connor Hudson',
      author_email = 'pypi@tekhne-blog.appspotmail.com',
      url = 'https://github.com/technoboy10/mist',
      description = 'A simple Python wrapper for the littleBits Cloud API',
      license = 'MIT',
      packages = ['mist'],
      install_requires = [
          'requests == 2.4.x',
      ],
      classifiers = [
        "Programming Language :: Python",
      ],
)