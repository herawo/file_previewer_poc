import tg
from tg import expose
from tg import tmpl_context
from tgext.routes import RoutedController
from preview_generator.model.factory import PreviewBuilderFactory
from preview_generator.model.manager import PreviewManager

rootpath = tg.config.get('cache_root_folder_path') +'/preview_generator/public/img'
document_path = rootpath + '/{d_id}'
cache_path = rootpath + '/cache/'

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
        preview_manager = PreviewManager(path=cache_path)
        page_nb = preview_manager.get_nb_page(
            file_path=document_path.format(d_id=document_id),
            cache_path=cache_path
        )

        return dict(page='get_one_page',
                    page_nb=page_nb,
                    document_id=document_id,
                    page_id=page_id,
                    )

    @expose(content_type='image/jpeg')
    def small(self, document_id: int, page_id: int):
        print('Affichage du small')
        preview_manager = PreviewManager(path=cache_path)
        return preview_manager.get_jpeg_preview(
            file_path=document_path.format(d_id=document_id),
            page=page_id,
            height=256,
            width=256
        )

    @expose(content_type='image/jpeg')
    def large(self, document_id: int, page_id: int):
        print('Affichage du large')
        preview_manager = PreviewManager(path=cache_path)
        return preview_manager.get_jpeg_preview(
            file_path=document_path.format(d_id=document_id),
            page=page_id,
            height=1024
        )
    @expose(content_type='text/plain')
    def text(self, document_id: int, page_id: int):
        print('Affichage du text')
        preview_manager = PreviewManager(path=cache_path)
        return preview_manager.get_text_preview(
            file_path=document_path.format(d_id=document_id),
            page=page_id
        )

    @expose(content_type='application/pdf')
    def pdf(self, document_id: int, page_id: int):
        print('Affichage du pdf')
        preview_manager = PreviewManager(path=cache_path)
        return preview_manager.get_pdf_preview(
            file_path=document_path.format(d_id=document_id)
        )


    @expose('text/html')
    def html(self, document_id: int, page_id: int):
        print('Affichage du html')
        preview_manager = PreviewManager(path=cache_path)
        return preview_manager.get_html_preview(
            file_path=document_path.format(d_id=document_id),
            page=page_id
        )
