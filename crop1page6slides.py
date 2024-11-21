# cropslides.py
# For the PDF with 6 slides printed per page
# Split to one slide per page
# Crop the white margin

import pymupdf
from pdfCropMargins import crop

input_pdf = "L11.pdf"

src = pymupdf.open(input_pdf)
doc = pymupdf.open()  # empty output PDF

for spage in src:  # for each page in input
    r = spage.rect  # input page rectangle
    d = pymupdf.Rect(spage.cropbox_position,  # CropBox displacement if not
                  spage.cropbox_position)  # starting at (0, 0)
    # measure the dimensions
    cm_p = 1/2.54*72 # width convert 2.54cm to 72point
    x1 =  1.80*cm_p # distance of the left cornor to the left page edge
    x2 = 10.05*cm_p
    x3 = 11.50*cm_p
    x4 = 19.75*cm_p
    y1 =  2.75*cm_p
    y2 =  8.95*cm_p
    y3 = 10.85*cm_p
    y4 = 17.05*cm_p
    y5 = 18.95*cm_p
    y6 = 25.15*cm_p
    # rectangles of 6 slides
    r11 = pymupdf.Rect(x1, y1, x2, y2)
    r12 = pymupdf.Rect(x3, y1, x4, y2)
    r21 = pymupdf.Rect(x1, y3, x2, y4)
    r22 = pymupdf.Rect(x3, y3, x4, y4)
    r31 = pymupdf.Rect(x1, y5, x2, y6)
    r32 = pymupdf.Rect(x3, y5, x4, y6)
    rect_list = [r11, r12, r21, r22, r31, r32]  # put them in a list

    for rx in rect_list:  # run thru rect list
        rx += d  # add the CropBox displacement
        page = doc.new_page(-1,  # new output page with rx dimensions
                           width = rx.width,
                           height = rx.height)
        page.show_pdf_page(
                page.rect,  # fill all new page with the image
                src,  # input document
                spage.number,  # input page number
                clip = rx,  # which part to use of input page
            )

# that's it, save output file
out_pdf = "split-" + src.name
doc.save(out_pdf,
         garbage=3,  # eliminate duplicate objects
         deflate=True,  # compress stuff where possible
)

# pdfCropMargins to clean the extra white margin
crop(["-p", "20", "-u", "-s", out_pdf])
# crop(["-p", "0", "-gui", "paper2.pdf"])
