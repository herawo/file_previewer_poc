import os


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

    def get_page_number(self, document_id):
        raise 'Number of pages not supported for this kind of Preview Builder.'\
              'Preview builder must implements a get_page_number method'

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

class OnePagePreviewBuilder(PreviewBuilder):
    '''
    Generic preview handler for single page document
    '''
    def get_page_number(self, document_id):
        return 1


class ImagePreviewBuilder(OnePagePreviewBuilder):
    '''
    Generic preview handler for an Image (except multi-pages images)
    '''






