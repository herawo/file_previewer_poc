import tg
from tg import expose, RestController
from tg import tmpl_context

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
        print("Small")
        document_id = tg.request.controller_state.routing_args.get('id_doc')
        rootpath = tg.config.get('cache_root_folder_path')
        path = '{rp}/preview_generator/public/img/cache/{d_id}/{p_id}.jpg'\
            .format(rp=rootpath, d_id=document_id, p_id=page_id)
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(document_id)
        builder = factory.get_preview_builder(mimetype)
        print(mimetype)
        print(builder.__class__.__name__)
        if not builder.exists_small_preview(document_id, page_id):
            builder.build_small_preview(document_id, page_id)

        if builder.exists_small_preview(document_id, page_id):
            with open(path, 'rb') as handler:
                return handler.read()

        return None

    @expose(content_type='image/jpeg')
    def large(self, page_id: int):
        print("Large")
        document_id = tg.request.controller_state.routing_args.get('id_doc')
        rootpath = tg.config.get('cache_root_folder_path')
        print(document_id, page_id)
        path = '{rp}/preview_generator/public/img/cache/{d_id}/{p_id}.jpeg' \
            .format(rp=rootpath, d_id=document_id, p_id=page_id)
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(document_id)
        print(mimetype)
        builder = factory.get_preview_builder(mimetype)
        print(builder.__class__.__name__)
        if not builder.exists_large_preview(document_id, page_id):
            builder.build_large_preview(document_id, page_id)

        if builder.exists_large_preview(document_id, page_id):
            with open(path, 'rb') as handler:
                return handler.read()

        return None

    @expose(content_type='text/plain')
    def text(self, page_id: int):
        print("Texte")
        document_id = tg.request.controller_state.routing_args.get('id_doc')
        rootpath = tg.config.get('cache_root_folder_path')
        path = '{rp}/preview_generator/public/img/cache/{d_id}/{p_id}.txt' \
            .format(rp=rootpath, d_id=document_id, p_id=page_id)
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(document_id)
        builder = factory.get_preview_builder(mimetype)
        print(mimetype)
        print(builder.__class__.__name__)

        if not builder.exists_text_preview(document_id, page_id):
            builder.build_text_preview(document_id, page_id)

        if builder.exists_text_preview(document_id, page_id):
            with open(path, 'rb') as handler:
                return handler.read()

        return None

    @expose(content_type='application/pdf')
    def pdf(self, page_id: int):
        print("PDF")
        document_id = tg.request.controller_state.routing_args.get('id_doc')
        rootpath = tg.config.get('cache_root_folder_path')
        path = '{rp}/preview_generator/public/img/cache/{d_id}/{p_id}.pdf' \
            .format(rp=rootpath, d_id=document_id, p_id=document_id)
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(document_id)
        builder = factory.get_preview_builder(mimetype)
        if not builder.exists_pdf_preview(document_id, page_id):
            builder.build_pdf_preview(document_id, page_id)

        if builder.exists_pdf_preview(document_id, page_id):
            with open(path, 'rb') as handler:
                return handler.read()

        return None

    def html(self,page_id: int):
        print("HTML")
        return None