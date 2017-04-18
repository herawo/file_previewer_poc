import os

import tg
from PIL import Image
from preview_generator.model.preview import PreviewBuilder
from wand.image import Image as WImage
from shutil import copyfile

SMALL_PREVIEW_SIZE = (256, 256)
LARGE_PREVIEW_SIZE = (1024, 1024)

rootpath = tg.config.get('cache_root_folder_path')
document_path = rootpath + '/preview_generator/public/img/{d_id}'
preview_path = rootpath + '/preview_generator/public/img/cache/{d_id}/{p_id}'
cache_path = rootpath + '/preview_generator/public/img/cache/{d_id}'


class JpegPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print("New PNG preview builder")

    def build_small_preview(self, doc_id: int, page_id: int):
        """
        generate the jpg preview
        """
        im = Image.open(document_path.format(d_id=doc_id)
                        )
        try:
            os.mkdir(cache_path.format(d_id=doc_id))
        except OSError:
            pass

        temp = im.copy()

        temp = temp.resize(SMALL_PREVIEW_SIZE)

        temp.save(
            preview_path.format(d_id=doc_id, p_id=page_id) + '.jpg',
            'JPEG'
        )

    def exists_small_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.jpg'
        if os.path.exists(my_file):
            return True
        else:
            return False

    def build_large_preview(self, doc_id: int, page_id: int):
        """
        generate the jpg preview
        """
        im = Image.open(document_path.format(d_id=doc_id)
                        )
        try:
            os.mkdir(cache_path.format(d_id=doc_id))
        except OSError:
            pass

        temp = im.copy()

        temp = temp.resize(LARGE_PREVIEW_SIZE)

        temp.save(
            preview_path.format(d_id=doc_id, p_id=page_id) + '.jpeg',
            'JPEG'
        )

    def exists_large_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.jpeg'
        if os.path.exists(my_file):
            return True
        else:
            return False


class PngPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print("New PNG preview builder")

    def build_small_preview(self, doc_id: int, page_id: int):
        """
        generate the jpg preview
        """
        print("Construction d'un nouveau small preview")
        im = Image.open('preview_generator/public/img/{doc_id}'
                        .format(doc_id=doc_id)
                        )
        try:
            os.mkdir('preview_generator/public/img/cache/{doc_id}'.format(
                doc_id=doc_id))
        except OSError:
            pass

        temp = Image.new('RGB', SMALL_PREVIEW_SIZE, (255, 255, 255))

        height, width = im.size
        box = (0, 0, height, width)
        layer_copied = im.crop(box)
        layer_copied = layer_copied.resize(SMALL_PREVIEW_SIZE)
        temp.paste(layer_copied, (0, 0), layer_copied)

        temp.save(
            preview_path.format(d_id=doc_id, p_id=page_id) + '.jpg',
            'JPEG'
        )

    def exists_small_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.jpg'
        if os.path.exists(my_file):
            return True
        else:
            return False

    def build_large_preview(self, doc_id: int, page_id: int):
        """
        generate the jpg preview
        """
        print("Construction d'un nouveau Large preview")
        im = Image.open('preview_generator/public/img/{doc_id}'
                        .format(doc_id=doc_id)
                        )
        try:
            os.mkdir('preview_generator/public/img/cache/{doc_id}'.format(
                doc_id=doc_id))
        except OSError:
            pass

        temp = Image.new('RGB', LARGE_PREVIEW_SIZE, (255, 255, 255))

        height, width = im.size
        box = (0, 0, height, width)
        layer_copied = im.crop(box)
        layer_copied = layer_copied.resize(LARGE_PREVIEW_SIZE)
        temp.paste(layer_copied, (0, 0), layer_copied)

        temp.save(
            preview_path.format(d_id=doc_id, p_id=page_id) + '.jpeg',
            'JPEG'
        )

    def exists_large_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.jpeg'
        if os.path.exists(my_file):
            return True
        else:
            return False


class GifPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder Gif')

    def build_small_preview(self, doc_id: int, page_id: int):
        """
        generate the gif preview
        """
        im = Image.open(document_path.format(d_id=doc_id)
                        )
        try:
            os.mkdir(cache_path.format(d_id=doc_id))
        except OSError:
            pass

        temp = im.copy()

        temp = temp.resize(SMALL_PREVIEW_SIZE)
        temp = temp.convert('RGB')

        temp.save(
            preview_path.format(d_id=doc_id, p_id=page_id) + '.jpg'
            ,
            'JPEG'
        )

    def exists_small_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.jpg'
        if os.path.exists(my_file):
            return True
        else:
            return False


    def build_large_preview(self, doc_id: int, page_id: int):
        """
        generate the gif preview
        """
        im = Image.open(document_path.format(d_id=doc_id)
                        )
        try:
            os.mkdir(cache_path.format(d_id=doc_id))
        except OSError:
            pass

        temp = im.copy()

        temp = temp.resize(LARGE_PREVIEW_SIZE)
        temp = temp.convert('RGB')

        temp.save(
            preview_path.format(d_id=doc_id, p_id=page_id) + '.jpeg',
            'JPEG'
        )

    def exists_large_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.jpeg'
        if os.path.exists(my_file):
            return True
        else:
            return False


class BmpPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder Bmp')

    def build_small_preview(self, doc_id: int, page_id: int):
        """
        generate the gif preview
        """
        im = Image.open(document_path.format(d_id=doc_id))

        try:
            os.mkdir(cache_path.format(d_id=doc_id))
        except OSError:
            pass

        temp = im.copy()

        temp = temp.resize(SMALL_PREVIEW_SIZE)
        temp = temp.convert('RGB')

        temp.save(
            preview_path.format(d_id=doc_id, p_id=page_id) + '.jpg',
            'JPEG'
        )

    def exists_small_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.jpg'
        if os.path.exists(my_file):
            return True
        else:
            return False


    def build_large_preview(self, doc_id: int, page_id: int):
        """
        generate the gif preview
        """
        im = Image.open(document_path.format(d_id=doc_id))
        try:
            os.mkdir(cache_path.format(d_id=doc_id))
        except OSError:
            pass

        temp = im.copy()

        temp = temp.resize(LARGE_PREVIEW_SIZE)
        temp = temp.convert('RGB')

        temp.save(
            preview_path.format(d_id=doc_id, p_id=page_id) + '.jpeg',
            'JPEG'
        )

    def exists_large_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.jpeg'
        if os.path.exists(my_file):
            return True
        else:
            return False


class PdfPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder PDF')

    def build_small_preview(self, doc_id: int, page_id: int):
        """
        generate the pdf small preview
        """

        try:
            os.mkdir(cache_path.format(d_id=doc_id))
        except OSError:
            pass

        with WImage(
                filename=document_path.format(d_id=doc_id) + '[{p_id}]'.format(
                    p_id=page_id)
        ) as img:
            height, width = SMALL_PREVIEW_SIZE
            x = img.size[0]
            img.crop(width=x, height=x)
            img.resize(height, width)
            img.save(filename=
                     preview_path.format(d_id=doc_id, p_id=page_id) + '.jpg'
                     )

    def exists_small_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.jpg'
        if os.path.exists(my_file):
            return True
        else:
            return False


    def build_large_preview(self, doc_id: int, page_id: int):
        """
        generate the pdf small preview
        """

        print(doc_id, page_id)

        try:
            os.mkdir(cache_path.format(d_id=doc_id))
        except OSError:
            pass

        with WImage(
                filename=document_path.format(d_id=doc_id) + '[{p_id}]'.format(
                    p_id=page_id)
        ) as img:
            height, width = LARGE_PREVIEW_SIZE
            x = img.size[0]
            img.crop(width=x, height=x)
            img.resize(height, width)
            img.save(filename=preview_path.format(
                d_id=doc_id,
                p_id=page_id
            ) + '.jpeg'
                     )

    def exists_large_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.jpeg'
        if os.path.exists(my_file):
            return True
        else:
            return False


class DocPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder Doc')


class OdtPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder Odt')

    def build_small_preview(self, doc_id: int, page_id: int):
        """
        generate the text preview
        """

        try:
            os.mkdir(cache_path.format(d_id=doc_id))
        except OSError:
            pass

        my_file = preview_path.format(d_id=doc_id, p_id=doc_id) + '.pdf'
        if not os.path.exists(my_file):
            print("REBUILD")
            os.system('libreoffice --headless --convert-to pdf:writer_pdf_Export '
                      + document_path.format(d_id=doc_id) + ' --outdir '
                      + cache_path.format(d_id=doc_id)
                      + ' -env:UserInstallation='
                        'file:///tmp/LibreOffice_Conversion_${USER}')

        with WImage(
                #The pdf file is generated with name {doc_id}.pdf
                filename=preview_path.format(d_id=doc_id, p_id=doc_id)
                        + '.pdf[{p_id}]'.format(p_id=page_id)
        ) as img:
            height, width = SMALL_PREVIEW_SIZE
            x = img.size[0]
            img.crop(width=x, height=x)
            img.resize(height, width)
            img.save(filename=preview_path.format(
                d_id=doc_id,
                p_id=page_id
            ) + '.jpg'
                     )

    def exists_small_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.jpg'
        if os.path.exists(my_file):
            return True
        else:
            return False

    def build_large_preview(self, doc_id: int, page_id: int):
        """
        generate the large preview
        """

        try:
            os.mkdir(cache_path.format(d_id=doc_id))
        except OSError:
            pass

        my_file = preview_path.format(d_id=doc_id, p_id=doc_id) + '.pdf'
        if not os.path.exists(my_file):
            print("REBUILD")
            os.system('libreoffice --headless --convert-to pdf:writer_pdf_Export '
                      + document_path.format(d_id=doc_id) + ' --outdir '
                      + cache_path.format(d_id=doc_id)
                      + ' -env:UserInstallation='
                        'file:///tmp/LibreOffice_Conversion_${USER}')

        with WImage(
                #The pdf file is generated with name {doc_id}.pdf
                filename=preview_path.format(d_id=doc_id, p_id=doc_id)
                        + '.pdf[{p_id}]'.format(p_id=page_id)
        ) as img:
            height, width = LARGE_PREVIEW_SIZE
            x = img.size[0]
            img.crop(width=x, height=x)
            img.resize(height, width)
            img.save(filename=preview_path.format(
                d_id=doc_id,
                p_id=page_id
            ) + '.jpeg'
                     )

    def exists_large_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.jpeg'
        if os.path.exists(my_file):
            return True
        else:
            return False

    def build_pdf_preview(self, doc_id: int, page_id: int):
        """
        generate the text preview
        """

        try:
            os.mkdir(cache_path.format(d_id=doc_id))
        except OSError:
            pass

        my_file = preview_path.format(d_id=doc_id, p_id=doc_id) + '.pdf'
        if not os.path.exists(my_file):
            print("REBUILD")
            os.system('libreoffice --headless --convert-to pdf:writer_pdf_Export '
                      + document_path.format(d_id=doc_id) + ' --outdir '
                      + cache_path.format(d_id=doc_id)
                      + ' -env:UserInstallation='
                        'file:///tmp/LibreOffice_Conversion_${USER}')


    def exists_pdf_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=doc_id) + '.pdf'
        if os.path.exists(my_file):
            return True
        else:
            return False



class TextPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder Text')

    def build_text_preview(self, doc_id: int, page_id: int):
        """
        generate the text preview
        """

        try:
            os.mkdir(cache_path.format(d_id=doc_id))
        except OSError:
            pass

        copyfile(src=document_path.format(d_id=doc_id),
                 dst=preview_path.format(d_id=doc_id, p_id=page_id) + '.txt'
                 )

    def exists_text_preview(self, doc_id: int, page_id: int):
        """
        return true if the cache file exists
        """

        my_file = preview_path.format(d_id=doc_id, p_id=page_id) + '.txt'
        if os.path.exists(my_file):
            return True
        else:
            return False


class ZipPreviewBuilder(PreviewBuilder):
    def __init__(preview_root_folder_path):
        print('New Preview Builder Zip')
