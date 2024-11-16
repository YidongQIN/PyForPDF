import pymupdf
from pdfCropMargins import crop

input_pdf = "L8.pdf"
# width 842pt height 595pt

src = pymupdf.open(input_pdf)
doc = pymupdf.open()  # empty output PDF

# 打开PDF文件
pdf = pymupdf.open(input_pdf)
# 获取指定页面
page = pdf[0]
# 获取页面尺寸
page_rect = page.rect
print(f"Page dimensions:\n {page_rect.width} x {page_rect.height} points")
