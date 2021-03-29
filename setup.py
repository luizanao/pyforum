import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.txt")).read()
CHANGES = open(os.path.join(here, "CHANGES.txt")).read()

requires = [
    "pyramid",
    "pyramid_debugtoolbar",
    "waitress",
    "Chameleon==2.13-1",
    "FormEncode==1.2.6",
    "Jinja2==2.7.1",
    "Mako==0.9.0",
    "MarkupSafe==0.18",
    "PasteDeploy==1.5.0",
    "Pygments==2.7.4",
    "WebHelpers==1.3",
    "WebOb==1.2.3",
    "pymongo==2.6.3",
    "pyramid==1.4.5",
    "pyramid-jinja2==1.8",
    "pyramid-mako==0.3.1",
    "pyramid-simpleform==0.6.1",
    "repoze.lru==0.6",
    "translationstring==1.1",
    "venusian==1.0a8",
    "wsgiref==0.1.2",
    "zope.deprecation==4.0.2",
    "zope.interface==4.0.5",
]

setup(
    name="Prj",
    version="1.0",
    description="Prj",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="Luiz Felipe @luiz_anao",
    author_email="luizfelipe;.unesp@gmail.com",
    url="luizanao.com",
    keywords="web pyramid pylons pratice learn",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    test_suite="prj",
    entry_points="""\
      [paste.app_factory]
      main = prj:main
      """,
)
