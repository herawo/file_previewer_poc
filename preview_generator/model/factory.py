import magic

from preview_generator.model.preview.bmp_preview import BmpPreviewBuilder
from preview_generator.model.preview.generic_preview import PreviewBuilder
from preview_generator.model.preview.gif_preview import GifPreviewBuilder
from preview_generator.model.preview.jpeg_preview import JpegPreviewBuilder
from preview_generator.model.preview.odt_preview import OfficePreviewBuilder
from preview_generator.model.preview.pdf_preview import PdfPreviewBuilder
from preview_generator.model.preview.png_preview import PngPreviewBuilder
from preview_generator.model.preview.text_preview import TextPreviewBuilder
from preview_generator.model.preview.zip_preview import ZipPreviewBuilder


class PreviewBuilderFactory(object):
    def __init__(self):
        pass

    def get_preview_builder(self, mimetype: str):

        compress = ['application/x-compressed',
                    'application/x-zip-compressed',
                    'application/zip',
                    'multipart/x-zip',
                    'application/x-tar'
                    ]

        office = [
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
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

    def get_document_mimetype(self, file_path) -> str:
        """ 
        return the mimetype of the file. see python module mimetype
        """
        mime = magic.Magic(mime=True)
        str = mime.from_file(file_path)
        return str

