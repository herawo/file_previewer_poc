from preview_generator.model import file_converter
from preview_generator.model.preview.generic_preview import ImagePreviewBuilder


class PngPreviewBuilder(ImagePreviewBuilder):

    mimetype = ['image/png']

    def build_jpeg_preview(self, file_path, cache_path, page_id, extension='.jpeg', size=(256,256)):
        """
        generate the jpg preview
        """

        # try:
        #     os.mkdir(cache_path.format(d_id=document_id))
        # except OSError:
        #     pass

        file_name = self.get_file_hash(file_path, size)
        with open(file_path, 'rb') as img:
            result = file_converter.image_to_jpeg_pillow(img, size)
            with open(
                    '{path}{extension}'.format(
                        path=cache_path + file_name,
                        extension=extension
                    ),
                    'wb'
            ) as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)