try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open('README') as file:
    long_description = file.read()

setup(name='flask-restful-swagger',
      version='0.19',
      url='https://github.com/aloha1003/line-flask-restful-swagger',
      zip_safe=False,
      packages=['flask_restful_swagger'],
      package_data={
        'flask_restful_swagger': [
          'static/*.*',
          'static/css/*.*',
          'static/images/*.*',
          'static/lib/*.*',
          'static/lib/shred/*.*',
          'templates/*.*'
        ]
      },
      description='Extrarct swagger specs from your flast-restful project',
      author='Aloha ',
      license='MIT',

      dependency_links=['https://github.com/aloha1003/LINE'],
      long_description=long_description,
      install_requires=['Flask-RESTful>=0.2.12',"Jinja2==2.6","Werkzeug==0.8.3","LINE","wsgiref==0.1.2"]
      )
