# import os
# import time
# from io import BytesIO
#
# from PyPDF2 import PdfFileReader
# from PyPDF2 import PdfFileWriter
#
# from preview_generator.model import file_converter
# from preview_generator.model.preview.generic_preview import ImagePreviewBuilder
# from preview_generator.model.preview.generic_preview import \
#     OnePagePreviewBuilder
# from preview_generator.model.preview.generic_preview import PreviewBuilder
#
#
# class JpegPreviewBuilder(ImagePreviewBuilder):
#
#
#     def build_jpeg_preview(self, file_path, cache_path, page_id: int, extension='.jpeg', size=(256,256)):
#         """
#         generate the jpeg preview
#         """
#
#         # try:
#         #     os.mkdir(cache_path.format(d_id=document_id))
#         # except OSError:
#         #     pass
#
#         file_name = self.get_file_hash(file_path, size)
#         with open(file_path, 'rb') as img:
#             result = file_converter.image_to_jpeg_wand(img, size)
#             with open('{path}_{page_id}_{extension}'.format(
#                             path=cache_path + file_name,
#                             page_id=page_id,
#                             extension=extension
#                     ),
#                     'wb') as jpeg:
#                 buffer = result.read(1024)
#                 while buffer:
#                     jpeg.write(buffer)
#                     buffer = result.read(1024)
#
#
# class PngPreviewBuilder(ImagePreviewBuilder):
#
#     def build_jpeg_preview(self, file_path, cache_path, page_id, extension='.jpeg', size=(256,256)):
#         """
#         generate the jpg preview
#         """
#
#         # try:
#         #     os.mkdir(cache_path.format(d_id=document_id))
#         # except OSError:
#         #     pass
#
#         file_name = self.get_file_hash(file_path,size)
#         with open(file_path, 'rb') as img:
#             result = file_converter.image_to_jpeg_pillow(img, size)
#             with open(
#                     '{path}_{page_id}_{extension}'.format(
#                         path=cache_path + file_name,
#                         page_id=page_id,
#                         extension=extension
#                     ),
#                     'wb'
#             ) as jpeg:
#                 buffer = result.read(1024)
#                 while buffer:
#                     jpeg.write(buffer)
#                     buffer = result.read(1024)
#
#
# class GifPreviewBuilder(ImagePreviewBuilder):
#
#     def build_jpeg_preview(self, file_path, cache_path, page_id: int, extension='.jpeg', size=(256,256)):
#         """
#         generate the gif preview
#         """
#         # try:
#         #     os.mkdir(cache_path.format(d_id=document_id))
#         # except OSError:
#         #     pass
#
#         file_name = self.get_file_hash(file_path, size)
#
#         with open(file_path, 'rb') as img:
#             result = file_converter.image_to_jpeg_wand(img, size)
#             with open('{path}_{page_id}_{extension}'.format(
#                             path=cache_path + file_name,
#                             page_id=page_id,
#                             extension=extension
#                     ),
#                     'wb') as jpeg:
#                 buffer = result.read(1024)
#                 while buffer:
#                     jpeg.write(buffer)
#                     buffer = result.read(1024)
#
#
# class BmpPreviewBuilder(ImagePreviewBuilder):
#
#     def build_jpeg_preview(self, file_path, cache_path, page_id: int, extension='.jpeg', size=(256,256)):
#         """
#         generate the bmp preview
#         """
#         # try:
#         #     os.mkdir(cache_path.format(d_id=document_id))
#         # except OSError:
#         #     pass
#
#         file_name = self.get_file_hash(file_path, size)
#         with open(file_path, 'rb') as img:
#             result = file_converter.image_to_jpeg_wand(img, size)
#             with open('{path}_{page_id}_{extension}'.format(
#                             path=cache_path + file_name,
#                             page_id=page_id,
#                             extension=extension
#                     ), 'wb') as jpeg:
#                 buffer = result.read(1024)
#                 while buffer:
#                     jpeg.write(buffer)
#                     buffer = result.read(1024)
#
#
# class PdfPreviewBuilder(PreviewBuilder):
#
#     def build_jpeg_preview(self, file_path, cache_path, page_id: int, extension='.jpg', size=(256,256)):
#         """
#         generate the pdf small preview
#         """
#         # try:
#         #     os.mkdir(cache_path.format(d_id=document_id))
#         # except OSError:
#         #     pass
#
#         file_name = self.get_file_hash(file_path, size)
#         with open(file_path, 'rb') as pdf:
#             input_pdf = PdfFileReader(pdf)
#             output_pdf = PdfFileWriter()
#             output_pdf.addPage(input_pdf.getPage(int(page_id)))
#             output_stream = BytesIO()
#             output_pdf.write(output_stream)
#             output_stream.seek(0, 0)
#             result = file_converter.pdf_to_jpeg(output_stream, size)
#
#             with open('{path}_{page_id}_{extension}'.format(
#                             path=cache_path + file_name,
#                             page_id=page_id,
#                             extension=extension
#                     ), 'wb') as jpeg:
#                 buffer = result.read(1024)
#                 while buffer:
#                     jpeg.write(buffer)
#                     buffer = result.read(1024)
#
#     def get_page_number(self, file_path, cache_path):
#
#         # try:
#         #     os.mkdir(cache_path.format(d_id=document_id)+'/')
#         # except OSError:
#         #     pass
#
#         file_name = self.get_file_hash(file_path)
#
#         with open(cache_path + file_name + '_page_nb', 'w') as count:
#             count.seek(0, 0)
#
#             with open(file_path, 'rb') as doc:
#                 inputpdf = PdfFileReader(doc)
#                 count.write(str(inputpdf.numPages))
#         with open(cache_path + file_name + '_page_nb', 'r') as count:
#             count.seek(0, 0)
#             return count.read()
#
# class OfficePreviewBuilder(PreviewBuilder):
#
#     def build_jpeg_preview(self, file_path, cache_path, page_id: int, extension='.jpg', size=(256,256)):
#         """
#         generate the text preview
#         """
#
#         # try:
#         #     os.mkdir(cache_path.format(d_id=document_id)+'/')
#         # except OSError:
#         #     pass
#
#
#         with open(file_path, 'rb') as odt:
#
#             file_name = self.get_file_hash(file_path)
#             if os.path.exists(
#                     '{path}{file_name}.pdf'.format(
#                         path=cache_path,
#                         file_name=file_name
#                     )):
#                 result = open(
#                     '{path}.pdf'.format(
#                         path=cache_path + file_name,
#                     ), 'rb')
#
#             else:
#                 if os.path.exists(cache_path + file_name + '_flag'):
#                     time.sleep(2)
#                     self.build_pdf_preview(
#                         file_path=file_path,
#                         cache_path=cache_path,
#                         extension=extension
#                     )
#                 else:
#                     result = file_converter.office_to_pdf(odt, cache_path, file_name)
#
#             input_pdf = PdfFileReader(result)
#             output_pdf = PdfFileWriter()
#             output_pdf.addPage(input_pdf.getPage(int(page_id)))
#             output_stream = BytesIO()
#             output_pdf.write(output_stream)
#             output_stream.seek(0, 0)
#             result2 = file_converter.pdf_to_jpeg(output_stream, size)
#
#
#
#             file_name = self.get_file_hash(file_path, size)
#
#             with open(
#                     '{path}{file_name}_{page_id}_{extension}'.format(
#                         file_name=file_name,
#                         path=cache_path,
#                         page_id=page_id,
#                         extension=extension
#                     ),
#                     'wb') \
#             as jpeg:
#                 buffer = result2.read(1024)
#                 while buffer:
#                     jpeg.write(buffer)
#                     buffer = result2.read(1024)
#
#
#     def get_page_number(self, file_path, cache_path):
#
#         # try:
#         #     os.mkdir(cache_path.format(d_id=document_id)+'/')
#         # except OSError:
#         #     pass
#
#         file_name = self.get_file_hash(file_path)
#
#         if not os.path.exists(cache_path + file_name + '.pdf'):
#             self.build_pdf_preview(
#                 file_path=file_path,
#                 cache_path=cache_path,
#                 extension='.pdf'
#             )
#
#         with open(cache_path + file_name + '_page_nb', 'w') as count:
#             count.seek(0, 0)
#             if not os.path.exists(cache_path + file_name + '.pdf'):
#                 self.build_pdf_preview(file_path, cache_path)
#
#             with open(cache_path + file_name + '.pdf', 'rb') as doc:
#                 inputpdf = PdfFileReader(doc)
#                 count.write(str(inputpdf.numPages))
#         with open(cache_path + file_name + '_page_nb', 'r') as count:
#             count.seek(0, 0)
#             return count.read()
#
#
#
#
#
#     def build_pdf_preview(self, file_path, cache_path, extension='.pdf'):
#         """
#         generate the pdf large preview
#         """
#
#         # try:
#         #     os.mkdir(cache_path.format(d_id=document_id))
#         # except OSError:
#         #     pass
#
#         with open(file_path, 'rb') as odt:
#
#             file_name = self.get_file_hash(file_path)
#
#             if os.path.exists('{path}_0_.pdf'.format(
#                         path=cache_path + file_name)):
#                 result = open('{path}_0_.pdf'.format(
#                         path=cache_path + file_name), 'rb')
#
#             else:
#                 if os.path.exists(cache_path + file_name + '_flag'):
#                     time.sleep(2)
#                     self.build_pdf_preview(file_path, cache_path, extension)
#                 else:
#                     result = file_converter.office_to_pdf(odt, cache_path, file_name)
#                     # os.remove('{cache_path}{file_name}'.format(
#                     #     cache_path=cache_path,
#                     #     file_name=file_name,
#                     # ))
#
#             with open(cache_path + file_name + extension, 'wb') as pdf:
#                 buffer = result.read(1024)
#                 while buffer:
#                     pdf.write(buffer)
#                     buffer = result.read(1024)
#
#
# class TextPreviewBuilder(OnePagePreviewBuilder):
#
#     def build_text_preview(self, file_path, cache_path, page_id: int, extension='.txt'):
#         """
#         generate the text preview
#         """
#
#         # try:
#         #     os.mkdir(cache_path.format(d_id=document_id))
#         # except OSError:
#         #     pass
#
#         file_name = self.get_file_hash(file_path)
#
#         with open(file_path, 'rb') as img:
#             result = file_converter.txt_to_txt(img)
#             with open('{path}_{page_id}_{extension}'.format(
#                         path=cache_path + file_name,
#                         page_id=page_id,
#                         extension=extension
#                     ),
#                     'wb') as jpeg:
#                 buffer = result.read(1024)
#                 while buffer:
#                     jpeg.write(buffer)
#                     buffer = result.read(1024)
#
# class ZipPreviewBuilder(OnePagePreviewBuilder):
#
#     def build_text_preview(self, file_path, cache_path, page_id: int, extension='.txt'):
#         """
#         generate the text preview
#         """
#
#         # try:
#         #     os.mkdir(cache_path.format(d_id=document_id))
#         # except OSError:
#         #     pass
#
#         file_name = self.get_file_hash(file_path)
#
#         with open(file_path, 'rb') as img:
#             result = file_converter.zip_to_txt(img)
#             with open(cache_path + file_name + '_0_' + extension, 'wb') as jpeg:
#                 buffer = result.read(1024)
#                 while buffer:
#                     jpeg.write(buffer)
#                     buffer = result.read(1024)
#
#
#     def build_html_preview(self, file_path, cache_path, page_id: int, extension='.html'):
#         """
#         generate the text preview
#         """
#
#         # try:
#         #     os.mkdir(cache_path.format(d_id=document_id))
#         # except OSError:
#         #     pass
#
#         file_name = self.get_file_hash(file_path)
#
#         with open(file_path, 'rb') as img:
#             result = file_converter.zip_to_html(img)
#             with open(cache_path + file_name + '_0_' + extension, 'wb') as jpeg:
#                 buffer = result.read(1024)
#                 while buffer:
#                     jpeg.write(buffer)
#                     buffer = result.read(1024)
#
