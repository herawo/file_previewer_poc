import os

import tg
import time

from io import BytesIO

from preview_generator.controllers import file_converter
from preview_generator.model.preview import PreviewBuilder, ImagePreviewBuilder, \
    OnePagePreviewBuilder
from PyPDF2 import PdfFileReader, PdfFileWriter

SMALL_PREVIEW_SIZE = (256, 256)
LARGE_PREVIEW_SIZE = (1024, 1024)

rootpath = tg.config.get('cache_root_folder_path') +'/preview_generator/public/img'
document_path = rootpath + '/{d_id}'
cache_path = rootpath + '/cache/{d_id}'
preview_path = cache_path + '/{p_id}' # == /preview_generator/public/img/cache/{d_id}/{p_id}
flag_path = cache_path + '/flag' # == /preview_generator/public/img/cache/{d_id}/flag


class JpegPreviewBuilder(ImagePreviewBuilder):
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


class PngPreviewBuilder(ImagePreviewBuilder):
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


class GifPreviewBuilder(ImagePreviewBuilder):
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


class BmpPreviewBuilder(ImagePreviewBuilder):
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
            input_pdf = PdfFileReader(pdf)
            output_pdf = PdfFileWriter()
            output_pdf.addPage(input_pdf.getPage(int(page_id)))
            output_stream = BytesIO()
            output_pdf.write(output_stream)
            output_stream.seek(0, 0)
            result = file_converter.pdf_to_jpeg(output_stream)

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
            input_pdf = PdfFileReader(pdf)
            output_pdf = PdfFileWriter()
            output_pdf.addPage(input_pdf.getPage(int(page_id)))
            output_stream = BytesIO()
            output_pdf.write(output_stream)
            output_stream.seek(0, 0)
            result = file_converter.pdf_to_jpeg(output_stream, LARGE_PREVIEW_SIZE)

            with open(preview_path.format(d_id=document_id, p_id=page_id) + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)

    def get_page_number(self, document_id):

        try:
            os.mkdir(cache_path.format(d_id=document_id)+'/')
        except OSError:
            pass

        if not os.path.exists(cache_path.format(d_id=document_id) + '/page_nb'):
            with open(cache_path.format(d_id=document_id) + '/page_nb', 'w') as count:
                count.seek(0, 0)
                with open(document_path.format(d_id=document_id), 'rb') as doc:
                    inputpdf = PdfFileReader(doc)
                    count.write(str(inputpdf.numPages))
        with open(cache_path.format(d_id=document_id) + '/page_nb', 'r') as count:
            count.seek(0, 0)
            return count.read()

class OfficePreviewBuilder(PreviewBuilder):
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

            print(preview_path.format(d_id=document_id, p_id=document_id))
            if os.path.exists(
                    preview_path.format(d_id=document_id, p_id=document_id)+'.pdf'):
                result = open(
                    preview_path.format(d_id=document_id, p_id=document_id)+'.pdf', 'rb')

            else:
                if os.path.exists(flag_path.format(d_id=document_id)):
                    time.sleep(2)
                    self.build_pdf_preview(document_id, page_id, extension)

                else:
                    result = file_converter.office_to_pdf(odt, document_id)

            input_pdf = PdfFileReader(result)
            output_pdf = PdfFileWriter()
            output_pdf.addPage(input_pdf.getPage(int(page_id)))
            output_stream = BytesIO()
            output_pdf.write(output_stream)
            output_stream.seek(0, 0)
            result2 = file_converter.pdf_to_jpeg(output_stream)

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

        t1 = time.time()
        print('t1 :', time.time() - t1)

        try:
            os.mkdir(cache_path.format(d_id=document_id)+'/')
        except OSError:
            pass

        print(preview_path.format(d_id=document_id, p_id=document_id))

        with open(document_path.format(d_id=document_id), 'rb') as odt:
            print('t2 :', time.time() - t1)
            if os.path.exists(
                    preview_path.format(d_id=document_id, p_id=document_id)+'.pdf'):
                print('t3 :', time.time() - t1)
                result = open(
                    preview_path.format(d_id=document_id, p_id=document_id)+'.pdf', 'rb')

            else:
                if os.path.exists(flag_path.format(d_id=document_id)):
                    print('t4 :', time.time() - t1)
                    time.sleep(11)
                    self.build_pdf_preview(document_id, page_id, extension)
                    print('t5 :', time.time() - t1)

                else:
                    print('t6 :', time.time() - t1)
                    result = file_converter.office_to_pdf(odt, document_id)

            print('t7 :', time.time() - t1)
            input_pdf = PdfFileReader(result)
            output_pdf = PdfFileWriter()
            output_pdf.addPage(input_pdf.getPage(int(page_id)))
            output_stream = BytesIO()
            output_pdf.write(output_stream)
            output_stream.seek(0, 0)
            result2 = file_converter.pdf_to_jpeg(output_stream, LARGE_PREVIEW_SIZE)
            print('t8 :', time.time() - t1)
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

    def get_page_number(self, document_id):

        try:
            os.mkdir(cache_path.format(d_id=document_id)+'/')
        except OSError:
            pass

        if not os.path.exists(cache_path.format(d_id=document_id) + '/page_nb'):
            self.build_pdf_preview(document_id, 0)

        with open(cache_path.format(d_id=document_id) + '/page_nb', 'w') as count:
            count.seek(0, 0)
            if not os.path.exists(preview_path.format(
                    d_id=document_id,
                    p_id=document_id
            )
            + '.pdf'):
                self.build_pdf_preview(document_id, 0)

            with open(preview_path.format(d_id=document_id,
                                          p_id=document_id) + '.pdf',
                      'rb') as doc:
                inputpdf = PdfFileReader(doc)
                count.write(str(inputpdf.numPages))
        with open(cache_path.format(d_id=document_id) + '/page_nb', 'r') as count:
            count.seek(0, 0)
            return count.read()





    def build_pdf_preview(self, document_id: int, page_id: int, extension='.pdf'):
        """
        generate the pdf large preview
        """

        try:
            os.mkdir(cache_path.format(d_id=document_id))
        except OSError:
            pass

        print(preview_path.format(d_id=document_id, p_id=document_id))

        with open(document_path.format(d_id=document_id), 'rb') as odt:
            print('path ', preview_path.format(d_id=document_id, p_id=document_id))

            if os.path.exists(
                    preview_path.format(d_id=document_id, p_id=document_id)+'.pdf'):
                result = open(
                    preview_path.format(d_id=document_id, p_id=document_id)+'.pdf', 'rb')

            else:
                if os.path.exists(flag_path.format(d_id=document_id)):
                    time.sleep(11)
                    self.build_pdf_preview(document_id, page_id, extension)

                else:
                    result = file_converter.office_to_pdf(odt, document_id)

            with open(preview_path.format(d_id=document_id, p_id=document_id) + extension, 'wb') as pdf:
                buffer = result.read(1024)
                while buffer:
                    pdf.write(buffer)
                    buffer = result.read(1024)


class TextPreviewBuilder(OnePagePreviewBuilder):
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

class ZipPreviewBuilder(OnePagePreviewBuilder):
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

