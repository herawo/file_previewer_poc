import os
import uuid
import zipfile
from builtins import print
from io import BytesIO

import tg
from PIL import Image
from wand.color import Color
from wand.image import Image as WImage
import time

SMALL_PREVIEW_SIZE = (256, 256)
LARGE_PREVIEW_SIZE = (1024, 1024)

rootpath = tg.config.get('cache_root_folder_path') +'/preview_generator/public/img'
document_path = rootpath + '/{d_id}'
cache_path = rootpath + '/cache/{d_id}'
preview_path = cache_path + '/{p_id}'
flag_path = cache_path + '/flag' # == /preview_generator/public/img/cache/{d_id}/flag




def png_to_jpeg(png: BytesIO, size=SMALL_PREVIEW_SIZE) ->BytesIO:
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


def jpeg_to_jpeg(jpeg: BytesIO, size=SMALL_PREVIEW_SIZE):
    print('Converting jpeg to jpeg of size ', size)

    with WImage(file=jpeg) as jpeg2:
        jpeg_cp = WImage(jpeg2)
        jpeg_cp.resize(size[0], size[1])

        content_as_bytes = jpeg_cp.make_blob('jpeg')
        output = BytesIO()
        output.write(content_as_bytes)
        output.seek(0, 0)
        return output


def bmp_to_jpeg(bmp: BytesIO, size=SMALL_PREVIEW_SIZE)->BytesIO:
    print('Converting gif to jpeg of size ', size)
    with WImage(file=bmp) as jpeg2:
        bmp_cp = WImage(jpeg2)
        bmp_cp.resize(size[0], size[1])

        content_as_bytes = bmp_cp.make_blob('jpeg')
        output = BytesIO()
        output.write(content_as_bytes)
        output.seek(0, 0)
        return output

def gif_to_jpeg(gif: BytesIO, size=SMALL_PREVIEW_SIZE)->BytesIO:
    print('Converting gif to jpeg of size ', size)

    with WImage(file=gif) as jpeg2:
        gif_cp = WImage(jpeg2)
        gif_cp.resize(size[0], size[1])

        content_as_bytes = gif_cp.make_blob('jpeg')
        output = BytesIO()
        output.write(content_as_bytes)
        output.seek(0, 0)
        return output

def pdf_to_jpeg(pdf: BytesIO, page_id, size=SMALL_PREVIEW_SIZE):

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
                img.sequence[int(page_id)],
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

def ods_to_pdf(ods: BytesIO, document_id)->BytesIO:
    a= 1

def office_to_pdf(odt: BytesIO, document_id)->BytesIO:
    print('convert office document to pdf ')


    file_name = str(uuid.uuid4())
    file_path = cache_path.format(d_id=document_id) + '/' + file_name

    try:
        os.mkdir(flag_path.format(d_id=document_id))
    except OSError:
        pass

    if not os.path.exists(preview_path.format(d_id=document_id, p_id=document_id) + '.pdf'):
        print("REBUILD")

        with open(file_path, 'wb') as odt_temp:
            odt.seek(0, 0)
            buffer = odt.read(1024)
            while buffer:
                odt_temp.write(buffer)
                buffer = odt.read(1024)

        #TODO There's probably a cleaner way to convert to pdf
        os.system('libreoffice --headless --convert-to pdf:writer_pdf_Export '
                  + file_path
                  + ' --outdir ' + cache_path.format(d_id=document_id)
                  + ' -env:UserInstallation='
                    'file:///tmp/LibreOffice_Conversion_${USER}')

    try:
        os.removedirs(flag_path.format(d_id=document_id))
    except OSError:
        print('ERROR 1')
        pass

    try:
        os.remove(file_path)
        os.rename(file_path + '.pdf', preview_path.format(d_id=document_id,
                                                          p_id=document_id) + '.pdf')
    except OSError:
        print('ERROR 2')
        pass

    with open(preview_path.format(
            d_id=document_id,
            p_id=document_id
    )+ '.pdf', 'rb') as pdf:
        pdf.seek(0, 0)
        content_as_bytes = pdf.read()
        output = BytesIO(content_as_bytes)
        output.seek(0, 0)

        return output

def txt_to_txt(text: BytesIO)->BytesIO:
    return text

def zip_to_txt(zip: BytesIO)->BytesIO:

    zz = zipfile.ZipFile(zip)
    output = BytesIO()
    for line, info in enumerate(zz.filelist):
        date = "%d-%02d-%02d %02d:%02d:%02d" % info.date_time[:6]
        # output.seek(0, 0)
        output.write(str.encode("%-46s %s %12d\n" % (info.filename, date, info.file_size)))
    output.seek(0, 0)
    return output

def zip_to_html(zip: BytesIO)->BytesIO:
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


def zip_to_json(zip: BytesIO)->BytesIO:
    a = 1

def html_to_html(html: BytesIO)->BytesIO:
    a = 1