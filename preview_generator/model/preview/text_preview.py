from preview_generator.model import file_converter
from preview_generator.model.preview.generic_preview import OnePagePreviewBuilder

class TextPreviewBuilder(OnePagePreviewBuilder):

    def build_text_preview(self, file_path, cache_path, page_id: int, extension='.txt'):
        """
        generate the text preview
        """

        # try:
        #     os.mkdir(cache_path.format(d_id=document_id))
        # except OSError:
        #     pass

        file_name = self.get_file_hash(file_path)

        with open(file_path, 'rb') as img:
            result = file_converter.txt_to_txt(img)
            with open('{path}_{page_id}_{extension}'.format(
                        path=cache_path + file_name,
                        page_id=page_id,
                        extension=extension
                    ),
                    'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)
