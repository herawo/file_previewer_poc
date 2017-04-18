# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, AppConfig, tmpl_context

from preview_generator.controllers.documents import DocumentsController
from preview_generator.lib.base import BaseController


class RootController(BaseController):

    documents = DocumentsController()

    @expose('preview_generator.templates.index')
    def index(self):
        return dict(page='index')


    @expose()
    def _default(self, *args, **kw):
        return "This page is not ready"

    @expose()
    def say_hello(self, name):
        return '<h3>Hello %s</h3>' % name




