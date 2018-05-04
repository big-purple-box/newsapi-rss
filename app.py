import cherrypy
import os
import requests
from rss import *

from urllib.parse import urlparse, urlencode

class RSSConvert(object):
    @cherrypy.expose
    def default(self, *args, **params):
        base_path = "https://newsapi.org"
        parse = urlparse(cherrypy.url())
        url_params = urlencode(params)
        url_path = "{}{}?{}".format(base_path, parse.path, url_params)
        r = requests.get(url_path)
        return get_rss_for_json(r.json())

config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    },
    '/assets': {
        'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__)),
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'assets',
    }
}

cherrypy.quickstart(RSSConvert(), '/', config=config)
