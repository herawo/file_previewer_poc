import os

import tg
from tg import expose, RestController
from tg import tmpl_context
import zipfile

from preview_generator.model.preview import PreviewBuilderFactory

__all__ = ['PagesController']


class PagesController(RestController):

    def _before(self, *args, **kw):
        tmpl_context.project_name = 'preview_generator'

    @expose()
    def _default(self):
        return '<h2> Error Loading Page</h2>'

    @expose('preview_generator.templates.pages')
    def get_all(self):
        return dict(page='pages',
                    document_id=tg.request.controller_state.routing_args.get('id_doc')
                    )

    @expose('preview_generator.templates.get_one_page')
    def get_one(self, id_page: int):
        return dict(page='get_one_page',
                    document_id=tg.request.controller_state.routing_args.get('id_doc'),
                    page_id=id_page
                    )

    @expose(content_type='image/jpeg')
    def small(self, page_id: int):
        print('Building small preview')
        document_id = tg.request.controller_state.routing_args.get('id_doc')
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(document_id)
        builder = factory.get_preview_builder(mimetype)
        print('Document mimetype is', mimetype)
        return builder.get_small_preview(document_id, page_id)

    @expose(content_type='image/jpeg')
    def large(self, page_id: int):
        print("Large")
        document_id = tg.request.controller_state.routing_args.get('id_doc')
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(document_id)
        builder = factory.get_preview_builder(mimetype)
        print('Document mimetype is', mimetype)
        return builder.get_large_preview(document_id, page_id)

    @expose(content_type='text/plain')
    def text(self, page_id: int):
        print("Texte")
        document_id = tg.request.controller_state.routing_args.get('id_doc')
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(document_id)
        builder = factory.get_preview_builder(mimetype)
        print('Document mimetype is', mimetype)
        return builder.get_text_preview(document_id, page_id)

    @expose(content_type='application/pdf')
    def pdf(self, page_id: int):
        print("PDF")
        document_id = tg.request.controller_state.routing_args.get('id_doc')
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(document_id)
        builder = factory.get_preview_builder(mimetype)
        return builder.get_pdf_preview(document_id, page_id)


    @expose('text/html')
    def html(self, page_id: int):

        print("HTML")
        document_id = tg.request.controller_state.routing_args.get('id_doc')
        rootpath = tg.config.get('cache_root_folder_path')
        path = '{rp}/preview_generator/public/img/cache/{d_id}/{p_id}.html' \
            .format(rp=rootpath, d_id=document_id, p_id=page_id)
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(document_id)
        builder = factory.get_preview_builder(mimetype)
        print(mimetype)
        print(builder.__class__.__name__)

        if not builder.exists_html_preview(document_id, page_id):
            builder.build_html_preview(document_id, page_id)

        if builder.exists_html_preview(document_id, page_id):
            with open(path, 'rb') as handler:
                return handler.read()

        return None
