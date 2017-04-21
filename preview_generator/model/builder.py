import os

import tg
import time

from preview_generator.controllers import file_converter
from preview_generator.model.preview import PreviewBuilder

SMALL_PREVIEW_SIZE = (256, 256)
LARGE_PREVIEW_SIZE = (1024, 1024)

rootpath = tg.config.get('cache_root_folder_path') +'/preview_generator/public/img'
document_path = rootpath + '/{d_id}'
cache_path = rootpath + '/cache/{d_id}'
preview_path = cache_path + '/{p_id}' # == /preview_generator/public/img/cache/{d_id}/{p_id}
flag_path = cache_path + '/flag' # == /preview_generator/public/img/cache/{d_id}/flag


class JpegPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print("New PNG preview builder")

    def build_small_preview(self, document_id: int, page_id: int, extension='.jpg'):
        """
        generate the jpg preview
        """

        print('Building Document {d_id} page {p_id}'.format(d_id=document_id,
                                                           p_id=page_id))

        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as img:
            result = file_converter.jpeg_to_jpeg(img)
            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)


    def build_large_preview(self, document_id: int, page_id: int, extension='.jpeg'):
        """
        generate the jpeg preview
        """

        print('Building Document {d_id} page {p_id}'.format(d_id=document_id,
                                                           p_id=page_id))

        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as img:
            result = file_converter.jpeg_to_jpeg(img, LARGE_PREVIEW_SIZE)
            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)


class PngPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print("New PNG preview builder")

    def build_small_preview(self, document_id: int, page_id: int, extension='.jpg'):
        """
        generate the jpg preview
        """

        print('Building Document {d_id} page {p_id}'.format(d_id=document_id,
                                                           p_id=page_id))

        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as img:
            result = file_converter.png_to_jpeg(img)
            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)


    def build_large_preview(self, document_id, page_id, extension='.jpeg'):
        """
        generate the jpg preview
        """

        print('Building Document {d_id} page {p_id}'.format(d_id=document_id,
                                                           p_id=page_id))

        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as img:
            result = file_converter.png_to_jpeg(img, LARGE_PREVIEW_SIZE)
            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)


class GifPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder Gif')

    def build_small_preview(self, document_id: int, page_id: int, extension='.jpg'):
        """
        generate the gif preview
        """

        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as img:
            result = file_converter.gif_to_jpeg(img)
            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)


    def build_large_preview(self, document_id: int, page_id: int, extension='.jpeg'):
        """
        generate the gif preview
        """
        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as img:
            result = file_converter.gif_to_jpeg(img)
            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)


class BmpPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder Bmp')

    def build_small_preview(self, document_id: int, page_id: int, extension='.jpeg'):
        """
        generate the bmp preview
        """
        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as img:
            result = file_converter.gif_to_jpeg(img)
            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)


    def build_large_preview(self, document_id: int, page_id: int, extension='.jpeg'):
        """
        generate the bmp preview
        """
        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as img:
            result = file_converter.gif_to_jpeg(img, LARGE_PREVIEW_SIZE)
            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)


class PdfPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder PDF')


    def build_small_preview(self, document_id: int, page_id: int, extension='.jpg'):
        """
        generate the pdf small preview
        """
        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as pdf:
            result = file_converter.pdf_to_jpeg(pdf, page_id)  # BytesIO

            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)


    def build_large_preview(self, document_id: int, page_id: int, extension='.jpeg'):
        """
        generate the pdf large preview
        """
        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as pdf:
            result = file_converter.pdf_to_jpeg(pdf, page_id, LARGE_PREVIEW_SIZE)  # BytesIO

            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)





class DocPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder Doc')


class OdtPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder Odt')

    def build_small_preview(self, document_id: int, page_id: int, extension='.jpg'):
        """
        generate the text preview
        """

        try:
            os.mkdir(cache_path.format(d_id=document_id)+'/')
        except OSError:
            pass



        with open(document_path.format(d_id=document_id), 'rb') as odt:

            if os.path.exists(flag_path):
                time.sleep(11)
                if os.path.exists(preview_path.format(d_id=document_id, p_id=document_id)):
                    result = open(preview_path.format(d_id=document_id, p_id=document_id))
                else:
                    result = file_converter.odt_to_pdf(odt, document_id)
            else:
                result = file_converter.odt_to_pdf(odt, document_id)  # BytesIO
            result2 = file_converter.pdf_to_jpeg(result, page_id)
            with open(
                    preview_path.format(
                         d_id=document_id,
                         p_id=page_id) + extension,
                    'wb') \
            as jpeg:
                buffer = result2.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result2.read(1024)

    def build_large_preview(self, document_id: int, page_id: int, extension='.jpeg'):
        """
        generate the large preview
        """



        try:
            os.mkdir(cache_path.format(d_id=document_id)+'/')
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as odt:
            if os.path.exists(flag_path):
                time.sleep(11)
                if os.path.exists(preview_path.format(d_id=document_id, p_id=document_id)):
                    result = open(preview_path.format(d_id=document_id, p_id=document_id))
                else:
                    result = file_converter.odt_to_pdf(odt, document_id)
            else:
                result = file_converter.odt_to_pdf(odt, document_id)  # BytesIO
            result2 = file_converter.pdf_to_jpeg(result, page_id, LARGE_PREVIEW_SIZE)
            with open(
                    preview_path.format(
                         d_id=document_id,
                         p_id=page_id) + extension,
                    'wb') \
            as jpeg:
                buffer = result2.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result2.read(1024)


    def build_pdf_preview(self, document_id: int, page_id: int, extension='.pdf'):
        """
        generate the pdf large preview
        """

        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as odt:

            print(os.listdir(cache_path.format(d_id=document_id)))
            if os.path.exists(flag_path.format(d_id=document_id)):
                if os.path.exists(preview_path.format(d_id=document_id, p_id=document_id)):
                    result = open(preview_path.format(d_id=document_id, p_id=document_id))

                else:
                    time.sleep(11)
                    result = file_converter.odt_to_pdf(odt, document_id)
            else:
                if os.path.exists(preview_path.format(d_id=document_id, p_id=document_id)):
                    result = open(preview_path.format(d_id=document_id, p_id=document_id))
                else:
                    result = file_converter.odt_to_pdf(odt, document_id)  # BytesIO

            with open(preview_path.format(d_id=document_id, p_id=document_id) + extension, 'wb') as pdf:
                buffer = result.read(1024)
                while buffer:
                    pdf.write(buffer)
                    buffer = result.read(1024)





class TextPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder Text')

    def build_text_preview(self, document_id: int, page_id: int, extension='.txt'):
        """
        generate the text preview
        """

        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as img:
            result = file_converter.txt_to_txt(img)
            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)

class ZipPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder Zip')

    def build_text_preview(self, document_id: int, page_id: int, extension='.txt'):
        """
        generate the text preview
        """

        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as img:
            result = file_converter.zip_to_txt(img)
            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)



    def exists_text_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.txt'
        if os.path.exists(my_file):
            return True
        else:
            return False


    def build_html_preview(self, document_id: int, page_id: int, extension='.html'):
        """
        generate the text preview
        """

        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        with open(document_path.format(d_id=document_id), 'rb') as img:
            result = file_converter.zip_to_html(img)
            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)


    def exists_html_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.html'
        if os.path.exists(my_file):
            return True
        else:
            return False