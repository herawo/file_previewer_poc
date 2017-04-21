import tg
from tg import expose, RestController
from tg import tmpl_context
import os

from preview_generator.controllers.pages import PagesController

rootpath = tg.config.get('cache_root_folder_path')
documents_path = rootpath + '/preview_generator/public/img'

__all__ = ['DocumentsController']

class DocumentsController(RestController):

    pages = PagesController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "preview_generator"

    @expose()
    def _default(self):
        return "<h2> Error Loading Documents</h2>"

    @expose('preview_generator.templates.documents')
    def get_all(self):
        files = os.listdir(documents_path)
        file_count = len(files) -1
        print(file_count)

        return dict(
                    page='documents',
                    document_nb=file_count
                    )

    @expose('preview_generator.templates.get_one_document')
    def get_one(self, id_doc):

        tg.tmpl_context.doc_id = id_doc

        return dict(
            page='get_one_document',
            document_id=id_doc,
        )






