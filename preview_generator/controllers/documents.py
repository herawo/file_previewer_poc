import tg
from tg import expose
from tg import tmpl_context
import os
from tgext.routes import RoutedController, route

rootpath = tg.config.get('cache_root_folder_path')
documents_path = rootpath + '/preview_generator/public/img'

__all__ = ['DocumentsController']

class DocumentsController(RoutedController):

    def _before(self, *args, **kw):
        tmpl_context.project_name = "preview_generator"

    @expose()
    def _default(self):
        return "<h2> Error Loading Documents</h2>"

    @expose('preview_generator.templates.documents')
    @route('')
    def documents_list(self):
        files = os.listdir(documents_path)
        file_count = len(files) - 1
        print(file_count)

        return dict(
                    page='documents',
                    document_nb=file_count
                    )

    @expose('preview_generator.templates.get_one_document')
    def single_document(self, document_id):

        tg.tmpl_context.doc_id = document_id

        return dict(
            page='get_one_document',
            document_id=document_id,
        )






