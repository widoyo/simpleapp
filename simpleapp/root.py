# -*- encoding: utf-8 -*-
# simpleapp/root.py

# Widoyo
import cherrypy


class Root(object):
    @cherrypy.expose
    def index(self):
        return 'Hello world'

    @cherrypy.expose
    def about(self):
        return 'About'
