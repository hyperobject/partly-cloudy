from setuptools import setup


setup(name = 'partlycloudy',
      version = '0.1.1',
      author = 'Connor Hudson',
      author_email = 'pypi@tekhne-blog.appspotmail.com',
      url = 'https://github.com/technoboy10/partly-cloudy',
      description = 'A ridiculously lightweight Python wrapper for the littleBits Cloud API',
      license = 'MIT',
      packages = ['partlycloudy'],
      install_requires = [
          'requests == 2.4.0',
      ],
      classifiers = [
        "Programming Language :: Python",
      ],
)
