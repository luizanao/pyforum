from pyramid.config import Configurator
from pyramid_jinja2 import renderer_factory
from prj.resources import Root
from gridfs import GridFS
from urlparse import urlparse
import pymongo


def main(global_config, **settings):
    """ This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve``.
    """

    settings = dict(settings)
    settings.setdefault('jinja2.i18n.domain', 'Prj')
    
    config = Configurator(settings=settings, root_factory=Root)
    config.add_translation_dirs('locale/')
    config.include('pyramid_jinja2')
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')
    
    config.add_static_view('static', 'static')
    config.add_view('prj.views.my_view',context='prj:resources.Root')
    
    

    #routes
    config.add_route('home', '/')
    config.add_route('last_five', '/last-five')
    config.add_route('new_topic', '/new-topic')
    config.add_route('find', '/find-topic')
    config.add_route('view_topic', '/topic/{url}')
    config.add_route('new_answer', '/topic/add-message/{url}')
    config.add_route('vote_up', '/vote/up/{url}/{id}')
    

    db_url = urlparse(settings['mongo_uri'])
    config.registry.db = pymongo.Connection(
       host=db_url.hostname,
       port=db_url.port,
   )
    

    #add my mongonDB "forum database" configured in development.py
    def add_db(request):
       db = config.registry.db[db_url.path[1:]]
       if db_url.username and db_url.password:
           db.authenticate(db_url.username, db_url.password)
       return db

    def add_fs(request):
        return GridFS(request.db)

    config.add_request_method(add_db, 'db', reify=True)
    config.add_request_method(add_fs, 'fs', reify=True)

    #scan app
    config.scan('prj')

    return config.make_wsgi_app()
