import tg
from tg import RestController, expose, tmpl_context
from preview_generator.model.preview import PreviewBuilderFactory

__all__ = ['SmallController',
           'LargeController',
           'JsonController',
           'TextController']

class SmallController(RestController):


    def _before(self, *args, **kw):
        tmpl_context.project_name = 'preview_generator'

    def get_preview(self, id) -> str:
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(id)
        builder = factory.get_preview_builder(mimetype)
        if not builder.exists_small_preview(id):
            builder.build_small_preview(id)
        return builder.get_small_preview(id)

    @expose('preview_generator.templates.small')
    def get_all(self):
        doc_id = tg.request.controller_state.routing_args.get('id_doc')
        url_small = self.get_preview(doc_id)

        return dict(page='small',
                    document_id=doc_id,
                    page_id=tg.request.controller_state.routing_args.get('id_page'),
                    url=url_small
        )

    @expose()
    def _default(self):
        return '<h2> Error Loading Page</h2>'


class LargeController(RestController):

    @expose()
    def _default(self):
        return '<h2> Error Loading Page</h2>'

    def _before(self, *args, **kw):
        tmpl_context.project_name = 'preview_generator'

    def get_preview(self, id) -> str:
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(id)
        builder = factory.get_preview_builder(mimetype)
        if not builder.exists_large_preview(id):
            builder.build_large_preview(id)
        return builder.get_large_preview(id)

    @expose('preview_generator.templates.large')
    def get_all(self):
        doc_id = tg.request.controller_state.routing_args.get('id_doc')
        url_large = self.get_preview(doc_id)

        return dict(page='large',
                    document_id=doc_id,
                    page_id=tg.request.controller_state.routing_args.get(
                        'id_page'),
                    url=url_large
                    )


class TextController(RestController):

    @expose()
    def _default(self):
        return '<h2> Format not supported yet </h2>'

    def _before(self, *args, **kw):
        tmpl_context.project_name = 'preview_generator'

    def get_preview(self, id) -> str:
        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(id)
        builder = factory.get_preview_builder(mimetype)
        if not builder.exists_text_preview(id):
            builder.build_text_preview(id)
        return builder.get_text_preview(id)

    @expose('preview_generator.templates.text')
    def get_all(self):
        doc_id = tg.request.controller_state.routing_args.get('id_doc')
        url_text = self.get_preview(doc_id)

        return dict(page='large',
                    document_id=doc_id,
                    page_id=tg.request.controller_state.routing_args.get(
                        'id_page'),
                    url=url_text
                    )


class JsonController(RestController):

    @expose()
    def _default(self):
        return '<h2> Error Loading Page</h2>'

    def _before(self, *args, **kw):
        tmpl_context.project_name = 'preview_generator'

    @expose()
    def get_all(self):
        return 'JSON'
