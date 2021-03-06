import os

import zipfile
from builtins import print
from io import BytesIO
from PIL import Image
from wand.color import Color
from wand.image import Image as WImage



def image_to_jpeg_pillow(png, size=(256, 256)) ->BytesIO:
    print('Converting png to jpeg of size ', size)
    temp = Image.new('RGB', size, (255, 255, 255))
    with Image.open(png) as image:
        height, width = image.size
        box = (0, 0, height, width)
        layer_copied = image.crop(box)
        layer_copied = layer_copied.resize(size)
        temp.paste(layer_copied, (0, 0), layer_copied)
        output = BytesIO()
        temp.save(output, 'jpeg')
        # output.write(content_as_bytes)
        output.seek(0, 0)
        return output


def image_to_jpeg_wand(jpeg, size=(256, 256)):
    '''
    for jpeg, gif and bmp
    :param jpeg: 
    :param size: 
    :return: 
    '''
    print('Converting an image to jpeg of size ', size)

    with WImage(file=jpeg) as jpeg2:
        jpeg_cp = WImage(jpeg2)
        jpeg_cp.resize(size[0], size[1])

        content_as_bytes = jpeg_cp.make_blob('jpeg')
        output = BytesIO()
        output.write(content_as_bytes)
        output.seek(0, 0)
        return output

def pdf_to_jpeg(pdf, size=(256,256)):

    print('convert pdf to jpeg of size ', size)
    with WImage(file=pdf) as img:
        height, width = img.size
        if height < width:
            breadth = height
        else:
            breadth = width
        with WImage(
            width=breadth,
            height=breadth,
            background=Color('white')
        ) as image:
            image.composite(
                img,
                top=0,
                left=0
            )
            image.crop(0, 0, width=breadth, height=breadth)
            image.resize(size[0], size[1])

            content_as_bytes = image.make_blob('jpeg')
            output = BytesIO()
            output.write(content_as_bytes)
            output.seek(0, 0)
            return output


def office_to_pdf(odt, cache_path, file_name):
    print('convert office document to pdf ')

    try:
        os.mkdir(cache_path + file_name + '_flag')
    except OSError:
        pass

    if not os.path.exists('{path}{file_name}'.format(
                        path=cache_path,
                        file_name=file_name)
    ):

        with open('{path}{file_name}'.format(
                        path=cache_path,
                        file_name=file_name), 'wb') \
        as odt_temp:
            odt.seek(0, 0)
            buffer = odt.read(1024)
            while buffer:
                odt_temp.write(buffer)
                buffer = odt.read(1024)

        try:
            os.makedirs(cache_path)
        except OSError:
            pass

        #TODO There's probably a cleaner way to convert to pdf
        os.system('libreoffice --headless --convert-to pdf:writer_pdf_Export '
                     + '{path}{extension}'.format(
                                                path=cache_path,
                                                extension=file_name
                                                 )
                     + ' --outdir ' + cache_path
                     + ' -env:UserInstallation='
                     + 'file:///tmp/LibreOffice_Conversion_${USER}')

    try:
        os.removedirs(cache_path + file_name + '_flag')
    except OSError:
        pass


    try:
        os.remove('{path}{file_name}'.format(
            path=cache_path,
            file_name=file_name
            )
        )
    except OSError:
        pass

    with open('{path}{file_name}.pdf'.format(
        path=cache_path,
        file_name=file_name
    ), 'rb') as pdf:
        pdf.seek(0, 0)
        content_as_bytes = pdf.read()
        output = BytesIO(content_as_bytes)
        output.seek(0, 0)

        return output

def txt_to_txt(text):
    return text

def zip_to_txt(zip):

    zz = zipfile.ZipFile(zip)
    output = BytesIO()
    for line, info in enumerate(zz.filelist):
        date = "%d-%02d-%02d %02d:%02d:%02d" % info.date_time[:6]
        # output.seek(0, 0)
        output.write(str.encode("%-46s %s %12d\n" % (info.filename, date, info.file_size)))
    output.seek(0, 0)
    return output

def zip_to_html(zip):
    zz = zipfile.ZipFile(zip)
    output = BytesIO()
    output.write(str.encode('<p><ul>'))
    for line, info in enumerate(zz.filelist):
        date = "%d-%02d-%02d %02d:%02d:%02d" % info.date_time[:6]
        # output.seek(0, 0)
        output.write(
            str.encode(
                "<li>%-46s %s %12d</li>\n" % (info.filename, date, info.file_size)
            )
        )
    output.write(str.encode('</ul></p>'))
    output.seek(0, 0)
    return output


def zip_to_json(zip)->BytesIO:
    a = 1

def html_to_html(html)->BytesIO:
    a = 1