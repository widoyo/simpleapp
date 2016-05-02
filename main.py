# -*- encoding: utf-8 -*-

# main.py
import os

import cherrypy

from simpleapp.root import Root

ABS_PATH = os.path.dirname(os.path.abspath(__file__))

config = {
    '/css': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(ABS_PATH, 'static', 'css')
    },
    '/js': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(ABS_PATH, 'static', 'js')
    },
    '/img': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(ABS_PATH, 'static', 'img')
    },
}


def start():
    cherrypy.tree.mount(Root(), '/', config=config)
    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == "__main__":
    start()
