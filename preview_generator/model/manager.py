from preview_generator.model.factory import PreviewBuilderFactory


class PreviewManager(object):

    cache_path = ''
    factory = PreviewBuilderFactory()

    def __init__(self, path: str):
        self.cache_path = path

    def get_nb_page(self, file_path, cache_path):
        mimetype = self.factory.get_document_mimetype(file_path)
        builder = self.factory.get_preview_builder(mimetype)
        page_nb = builder.get_page_number(file_path, cache_path)
        return page_nb

    def get_jpeg_preview(self, file_path: str, extension='.jpeg', page=None, height=256, width=None, force: bool=False):

        if width == None:
            width = height

        size = (height, width)

        mimetype = self.factory.get_document_mimetype(file_path)
        builder = self.factory.get_preview_builder(mimetype)
        print(builder)
        return builder.get_jpeg_preview(
            file_path=file_path,
            page_id=page,
            cache_path=self.cache_path,
            extension=extension,
            force=force,
            size=size
        )

    def get_pdf_preview(self, file_path: str, extension='.pdf', force: bool=False):

        mimetype = self.factory.get_document_mimetype(file_path)
        builder = self.factory.get_preview_builder(mimetype)
        return builder.get_pdf_preview(
            file_path=file_path,
            cache_path=self.cache_path,
            force=force,
            extension=extension
        )

    def get_text_preview(self, file_path: str, extension='.txt', page=0, force: bool=False):

        factory = PreviewBuilderFactory()
        mimetype = factory.get_document_mimetype(file_path)
        builder = factory.get_preview_builder(mimetype)
        return builder.get_text_preview(
            file_path=file_path,
            page_id=page,
            cache_path=self.cache_path,
            force=force,
            extension=extension
        )

    def get_html_preview(self, file_path: str, extension='.html', page=0, force: bool=False):
        mimetype = self.factory.get_document_mimetype(file_path)
        builder = self.factory.get_preview_builder(mimetype)
        return builder.get_html_preview(
            file_path=file_path,
            page_id=page,
            cache_path=self.cache_path,
            extension=extension
        )

    def get_json_preview(self, file_path: str, extension='.json', page=0, force: bool=False):
        mimetype = self.factory.get_document_mimetype(file_path)
        builder = self.factory.get_preview_builder(mimetype)
        return builder.get_json_preview(
            file_path=file_path,
            page_id=page,
            cache_path=self.cache_path,
            force=force,
            extension=extension
        )