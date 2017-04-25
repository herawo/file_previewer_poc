import tg
from routes import Mapper
from tg import expose
from tg import tmpl_context
from tgext.routes import RoutedController, route
from preview_generator.model.preview import PreviewBuilderFactory

__all__ = ['PagesController']


class PagesController(RoutedController):

    def _before(self, *args, **kw):
        tmpl_context.project_name = 'preview_generator'


    @expose()
    def _default(self):
        return '<h2> Error Loading Page</h2>'

    @expose('preview_generator.templates.pages')
    def previews_list(self, document_id: int):
        return dict(page='pages',
                    document_id=document_id
                    )

    @expose('preview_generator.templates.get_one_page')
    def single_preview(self, document_id: int, page_id: int):
        return dict(page='get_one_page',
                    document_id=document_id,
                    page_id=page_id
                    )

    @expose(content_type='image/jpeg')
    def small(self, document_id: int, page_id: int):
        print('Small')
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(document_id)
        builder = factory.get_preview_builder(mimetype)
        print('Document mimetype is', mimetype)
        return builder.get_small_preview(document_id, page_id)

    @expose(content_type='image/jpeg')
    def large(self, document_id: int, page_id: int):
        print("Large")
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(document_id)
        builder = factory.get_preview_builder(mimetype)
        print('Document mimetype is', mimetype)
        return builder.get_large_preview(document_id, page_id)

    @expose(content_type='text/plain')
    def text(self, document_id: int, page_id: int):
        print("Texte")
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(document_id)
        builder = factory.get_preview_builder(mimetype)
        print('Document mimetype is', mimetype)
        return builder.get_text_preview(document_id, page_id)

    @expose(content_type='application/pdf')
    def pdf(self, document_id: int, page_id: int):
        print("PDF")
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(document_id)
        builder = factory.get_preview_builder(mimetype)
        return builder.get_pdf_preview(document_id, page_id)


    @expose('text/html')
    def html(self, document_id: int, page_id: int):
        print("HTML")
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
