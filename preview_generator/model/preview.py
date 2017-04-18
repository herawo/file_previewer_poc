import magic





class PreviewBuilder(object):



    def __init__(self):
        print('New Preview Builder')

    def load_document(self, id):
        """
        ???
        """

    def build_small_preview(self, doc_id: int, page_id: int):
        """
        generate the jpg preview
        """

    def build_large_preview(self, doc_id: int, page_id: int):
        """
        generate the jpeg preview
        """

    def build_pdf_preview(self, doc_id: int, page_id: int):
        """
        generate the jpeg preview
        """

    def build_html_preview(self, doc_id: int, page_id: int):
        """
        generate the html preview
        """

    def build_json_preview(self, doc_id: int, page_id: int):
        """
        generate the json preview
        """

    def build_text_preview(self, doc_id: int, page_id: int):
        """ 
        return file content from the cache
        """

    def get_small_preview(self, doc_id: int, page_id: int):
        """ 
        return file content from the cache
        """
        return None

    def get_large_preview(self, doc_id: int, page_id: int):
        """ 
        return file content from the cache
        """
        return None

    def get_pdf_preview(self, doc_id: int, page_id: int):
        """ 
        return file content from the cache
        """
        return None

    def get_html_preview(self, doc_id: int, page_id: int):
        """ 
        return file content from the cache
        """
        return None

    def get_json_preview(self, doc_id: int, page_id: int):
        """ 
        return file content from the cache
        """
        return None

    def get_text_preview(self, doc_id: int, page_id: int):
        """ 
        return file content from the cache
        """
        return None

    def exists_small_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

    def exists_large_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """
        return False

    def exists_pdf_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """
        return False

    def exists_html_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """
        return False

    def exists_json_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """
        return False

    def exists_text_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """
        return False


class PreviewBuilderFactory(object):

    def __init__(self):
        print('new preview builder factory')

    def get_preview_builder(self, mimetype: str):

        from preview_generator.model.builder import \
            JpegPreviewBuilder,\
            PngPreviewBuilder, \
            GifPreviewBuilder, \
            BmpPreviewBuilder, \
            PdfPreviewBuilder, \
            TextPreviewBuilder,\
            OdtPreviewBuilder

        if 'image/jpeg' == mimetype:
            return JpegPreviewBuilder()

        elif 'image/png' == mimetype:
            return PngPreviewBuilder()

        elif 'image/gif' == mimetype:
            return GifPreviewBuilder()

        elif 'image/x-ms-bmp' == mimetype:
            return BmpPreviewBuilder()

        elif 'application/pdf' == mimetype:
            return PdfPreviewBuilder()

        elif 'text/plain' == mimetype:
            return TextPreviewBuilder()

        elif 'application/vnd.oasis.opendocument.text' == mimetype:
            return OdtPreviewBuilder()

        else:
            return PreviewBuilder()

    def get_document_file_path(self, id: int) -> str:
        """ return the absolute path of the file """


    def get_document_mimetype(self, id) -> str:
        """ 
        return the mimetype of the file. see python module mimetype
        """
        mime = magic.Magic(mime=True)
        str = mime.from_file('preview_generator/public/img/{id}'.format(id=id))
        return str





