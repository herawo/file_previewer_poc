# -*- coding: utf-8 -*-
"""Main Controller"""
from routes import Mapper
from tg import expose
from tgext.routes import RoutedController



class RootController(RoutedController):

    mapper = Mapper()
    mapper.connect('/documents',
                   controller='documents', action='documents_list')
    mapper.connect('/documents/{document_id}',
                   controller='documents', action='single_document')
    mapper.connect('/documents/{document_id}/pages',
                   controller='pages', action='previews_list')
    mapper.connect('/documents/{document_id}/pages/{page_id}',
                   controller='pages', action='single_preview')
    mapper.connect('/documents/{document_id}/pages/{page_id}/small',
                   controller='pages', action='small')
    mapper.connect('/documents/{document_id}/pages/{page_id}/large',
                   controller='pages', action='large')
    mapper.connect('/documents/{document_id}/pages/{page_id}/pdf',
                   controller='pages', action='pdf')
    mapper.connect('/documents/{document_id}/pages/{page_id}/text',
                   controller='pages', action='text')
    mapper.connect('/documents/{document_id}/pages/{page_id}/html',
                   controller='pages', action='html')

    # documents = DocumentsController()

    @expose('preview_generator.templates.index')
    def index(self):
        return dict(page='index')

    @expose()
    def _default(self, *args, **kw):
        return "This page is not ready"

    @expose()
    def say_hello(self, name):
        return '<h3>Hello %s</h3>' % name
