import os
from io import BytesIO
import hashlib

class PreviewBuilder(object):

    def __init__(self):
        print('New Preview Builder')

    def get_file_hash(self, file_path, size=None):
        if size == None:
            file_name = os.path.basename(file_path)
        else:
            file_name = '{fn}-{fh}x{fw}'.format(
                fn=os.path.basename(file_path),
                fh=str(size[0]),
                fw=str(size[1]),
            )

        file_hash = hashlib.md5(file_path.encode('utf-8')).hexdigest()
        return '{fn}-{fh}'.format(fn=file_name, fh=file_hash)

    def get_page_number(self, file_path, cache_path):
        raise Exception('Number of pages not supported for this kind of Preview'
                        ' Builder. Preview builder must implement a '\
                        'get_page_number method')

    def build_jpeg_preview(self, file_path, cache_path, page_id: int, extension='.jpg', size=(256,256)):
        """
        generate the jpg preview
        """
        pass

    def build_pdf_preview(self, file_path, cache_path, extension='.pdf'):
        """
        generate the jpeg preview
        """
        pass

    def build_html_preview(self, file_path, cache_path, page_id: int, extension='.html'):
        """
        generate the html preview
        """
        pass

    def build_json_preview(self, file_path, cache_path, page_id: int, extension='.json'):
        """
        generate the json preview
        """
        pass

    def build_text_preview(self, file_path, cache_path, page_id: int, extension='.txt'):
        """ 
        return file content from the cache
        """
        pass

    def get_jpeg_preview(self, file_path: str, page_id, cache_path, extension='.jpeg', size=(256,256)):

        file_name = self.get_file_hash(file_path, size)
        if not self.exists_preview(cache_path + file_name, page_id, extension):
            self.build_jpeg_preview(
                file_path=file_path,
                cache_path=cache_path,
                page_id=page_id,
                extension=extension,
                size=size
            )
        if self.exists_preview(cache_path + file_name, page_id, extension):
            with open(
                    '{path}{file_name}_{page_id}_{extension}'.format(
                        path=cache_path,
                        file_name=file_name,
                        page_id=page_id,
                        extension=extension
                    ),
                    'rb'
            ) as handler:
                return handler.read()

        return None

    def get_pdf_preview(self, file_path: str, cache_path, extension='.pdf') -> BytesIO:
        """ 
        return file content from the cache
        """
        file_name = self.get_file_hash(file_path)
        if not self.exists_preview(
                path=cache_path + file_name,
                extension=extension):
            self.build_pdf_preview(
                file_path=file_path,
                cache_path=cache_path,
                extension=extension
            )

        if self.exists_preview(
                path=cache_path + file_name,
                extension=extension
        ):

            with open(
                    '{path}{file_name}.pdf'.format(
                        path=cache_path,
                        file_name=file_name,
                    ),
                    'rb'
            ) as handler:
                return handler.read()

        return None

    def get_html_preview(self, file_path: str, cache_path, page_id: int, extension='.html'):
        """ 
        return file content from the cache
        """
        file_name = self.get_file_hash(file_path)
        if not self.exists_preview(cache_path + file_name, page_id, extension):
            self.build_html_preview(
                file_path=file_path,
                cache_path=cache_path,
                page_id=page_id,
                extension=extension
            )
        if self.exists_preview(cache_path + file_name, page_id, extension):
            with open(
                    '{path}_{page_id}_{extension}'.format(
                        path=cache_path + file_name,
                        page_id=page_id,
                        extension=extension
                    ),
                    'rb'
            ) as handler:
                return handler.read()

        return None

    def get_json_preview(self, doc_id: int, page_id: int):
        """ 
        return file content from the cache
        """
        return None

    def get_text_preview(self, file_path: str, cache_path, page_id: int, extension='.txt') -> BytesIO:
        """ 
        return file content from the cache
        """
        file_name = self.get_file_hash(file_path)
        if not self.exists_preview(cache_path + file_name, page_id, extension):
            self.build_text_preview(
                file_path=file_path,
                cache_path=cache_path,
                page_id=page_id,
                extension=extension
            )
        if self.exists_preview(cache_path + file_name, page_id, extension):
            with open(
                    '{path}_{page_id}_{extension}'.format(
                        path=cache_path + file_name,
                        page_id=page_id,
                        extension=extension
                    ),
                    'rb'
            ) as handler:
                return handler.read()

        return None

    def exists_preview(self, path, page_id=None, extension=''):
        """
        return true if the cache file exists
        """
        if page_id == None:
            full_path = '{path}{extension}'.format(
                path=path,
                extension=extension
            )
        else:
            full_path = '{path}_{page_id}_{extension}'.format(
                path=path,
                page_id=page_id,
                extension=extension
            )

        print(full_path)
        if os.path.exists(full_path):
            return True
        else:
            return False



    def register(self):
        pass


class OnePagePreviewBuilder(PreviewBuilder):
    '''
    Generic preview handler for single page document
    '''
    def get_page_number(self, file_path, cache_path):
        return 1


class ImagePreviewBuilder(OnePagePreviewBuilder):
    '''
    Generic preview handler for an Image (except multi-pages images)
    '''






