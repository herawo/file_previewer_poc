import os

import magic
import tg
from io import BytesIO

rootpath = tg.config.get('cache_root_folder_path') +'/preview_generator/public/img'
document_path = rootpath + '/{d_id}'
cache_path = rootpath + '/cache/{d_id}'
preview_path = cache_path + '/{p_id}' # == /preview_generator/public/img/cache/{d_id}/{p_id}
flag_path = cache_path + '/flag' # == /preview_generator/public/img/cache/{d_id}/flag



class PreviewBuilder(object):



    def __init__(self):
        print('New Preview Builder')

    def load_document(self, id):
        """
        ???
        """

    def build_small_preview(self, document_id: int, page_id: int, extension='.jpg'):
        """
        generate the jpg preview
        """

    def build_large_preview(self, document_id: int, page_id: int, extension='.jpg'):
        """
        generate the jpeg preview
        """

    def build_pdf_preview(self, document_id: int, page_id: int, extension='.pdf'):
        """
        generate the jpeg preview
        """

    def build_html_preview(self, document_id: int, page_id: int, extension='.html'):
        """
        generate the html preview
        """

    def build_json_preview(self, document_id: int, page_id: int, extension='.json'):
        """
        generate the json preview
        """

    def build_text_preview(self, document_id: int, page_id: int, extension='.txt'):
        """ 
        return file content from the cache
        """

    def get_small_preview(self, document_id, page_id, extension='.jpg') -> BytesIO:
        print('Loading Document {d_id} page {p_id}'.format(d_id=document_id, p_id=page_id))
        path = preview_path.format(d_id=document_id, p_id=page_id) + extension
        if not self.exists_small_preview(document_id, page_id):
            self.build_small_preview(document_id, page_id, extension)

        if self.exists_small_preview(document_id, page_id):
            with open(path, 'rb') as handler:
                return handler.read()

        return None

    def get_large_preview(self, document_id, page_id, extension='.jpeg') -> BytesIO:
        print('Loading Document {d_id} page {p_id}'.format(d_id=document_id, p_id=page_id))
        path = preview_path.format(d_id=document_id, p_id=page_id) + extension
        if not self.exists_large_preview(document_id, page_id):
            self.build_large_preview(document_id, page_id, extension)

        if self.exists_large_preview(document_id, page_id):
            with open(path, 'rb') as handler:
                return handler.read()

        return None

    def get_pdf_preview(self, document_id, page_id, extension='.pdf') -> BytesIO:
        """ 
        return file content from the cache
        """
        print('Loading Document {d_id}'.format(d_id=document_id))
        path = preview_path.format(d_id=document_id, p_id=document_id) + extension
        if not self.exists_pdf_preview(document_id, page_id):
            self.build_pdf_preview(document_id, page_id)

        if self.exists_pdf_preview(document_id, page_id):
            with open(path, 'rb') as handler:
                return handler.read()

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

    def get_text_preview(self, document_id, page_id, extension='.txt') -> BytesIO:
        print('Loading Document {d_id} page {p_id}'.format(d_id=document_id, p_id=page_id))
        path = preview_path.format(d_id=document_id, p_id=page_id) + extension
        if not self.exists_text_preview(document_id, page_id):
            self.build_text_preview(document_id, page_id, extension)

        if self.exists_text_preview(document_id, page_id):
            with open(path, 'rb') as handler:
                return handler.read()

        return None

    def exists_small_preview(self, doc_id: int, page_id: int, extension='.jpg'):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + extension
        if os.path.exists(my_file):
            return True
        else:
            return False

    def exists_large_preview(self, doc_id: int, page_id: int, extension='.jpeg'):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + extension
        if os.path.exists(my_file):
            return True
        else:
            return False

    def exists_pdf_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=doc_id) + '.pdf'
        if os.path.exists(my_file):
            return True
        else:
            return False

    def exists_html_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.html'
        if os.path.exists(my_file):
            return True
        else:
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

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.txt'
        if os.path.exists(my_file):
            return True
        else:
            return False

class PreviewBuilderFactory(object):

    def __init__(self):
        print('new preview builder factory')

    def get_preview_builder(self, mimetype: str):

        from preview_generator.model.builder import \
            JpegPreviewBuilder, \
            PngPreviewBuilder, \
            GifPreviewBuilder, \
            BmpPreviewBuilder, \
            PdfPreviewBuilder, \
            TextPreviewBuilder, \
            OfficePreviewBuilder, \
            ZipPreviewBuilder

        compress = ['application/x-compressed',
                    'application/x-zip-compressed',
                    'application/zip',
                    'multipart/x-zip',
                    'application/x-tar'
                    ]

        office = ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                  'application/vnd.oasis.opendocument.text',
                  'application/vnd.oasis.opendocument.spreadsheet',
                  'application/msword',
                  'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                  'application/vnd.openxmlformats-officedocument.wordprocessingml.template',
                  'application/vnd.ms-word.document.macroEnabled.12',
                  'application/vnd.ms-excel',
                  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                  'application/vnd.openxmlformats-officedocument.spreadsheetml.template',
                  'application/vnd.ms-excel.sheet.macroEnabled.12',
                  'application/vnd.ms-excel.template.macroEnabled.12',
                  'application/vnd.ms-excel.addin.macroEnabled.12',
                  'application/vnd.ms-excel.sheet.binary.macroEnabled.12',
                  'application/vnd.ms-powerpoint',
                  'application/vnd.openxmlformats-fficedocument.presentationml.presentation',
                  'application/vnd.openxmlformats-officedocument.presentationml.template',
                  'application/vnd.openxmlformats-officedocument.presentationml.slideshow',
                  'application/vnd.ms-powerpoint.addin.macroEnabled.12',
                  'application/vnd.ms-powerpoint.presentation.macroEnabled.12',
                  'application/vnd.ms-powerpoint.template.macroEnabled.12',
                  'application/vnd.ms-powerpoint.slideshow.macroEnabled.12',
                  'application/vnd.oasis.opendocument.spreadsheet',
                  'application/vnd.oasis.opendocument.text',
                  ' application/vnd.oasis.opendocument.text-template',
                  'application/vnd.oasis.opendocument.text-web',
                  'application/vnd.oasis.opendocument.text-master',
                  'application/vnd.oasis.opendocument.graphics',
                  'application/vnd.oasis.opendocument.graphics-template',
                  'application/vnd.oasis.opendocument.presentation',
                  'application/vnd.oasis.opendocument.presentation-template',
                  'application/vnd.oasis.opendocument.spreadsheet-template',
                  'application/vnd.oasis.opendocument.chart',
                  'application/vnd.oasis.opendocument.chart',
                  'application/vnd.oasis.opendocument.formula',
                  'application/vnd.oasis.opendocument.database',
                  'application/vnd.oasis.opendocument.image',
                  'application/vnd.openofficeorg.extension'
                 ]

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

        elif mimetype in office:
            return OfficePreviewBuilder()

        elif mimetype in compress:
            return ZipPreviewBuilder()






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





