import sys
import fitz  # PyMuPDF
from pdfCropMargins import crop

# 固定参数
_a4_page_width = 612  # 标准A4纸宽度，单位为 pt（2.54 cm = 1 inch = 72 points）
_a4_page_height = 792  # 标准A4纸高度，单位为 pt

def measure_pdf(input_doc):
    page = input_doc[0]  # 第一页
    page_rect = page.rect
    width = page_rect.width
    height = page_rect.height
    print(f"Page dimensions:\n{width} x {height} points")
    return width, height

def slide_3_2(width, height):
    _w_margin_ratio = 0.08
    _h_margin_ratio = 0.095
    _w_space_ratio = 0.065
    _h_space_ratio = 0.06
    _w_slide_ratio = 0.40
    _h_slide_ratio = 0.23
    slide_crop_boxes = [
        [width * (_w_margin_ratio), height * (_h_margin_ratio),
         width * (_w_slide_ratio+_w_space_ratio), height * (_h_slide_ratio+_h_margin_ratio)],  # 左上
        [width * (1-_w_margin_ratio-_w_slide_ratio), height * (_h_margin_ratio),
         width * (1-_w_margin_ratio), height * (_h_slide_ratio+_h_margin_ratio)],  # 右上
        [width * (_w_margin_ratio), height * (0.5-0.5*_h_slide_ratio),
         width * (_w_slide_ratio+_w_margin_ratio), height * (0.5+0.5*_h_slide_ratio)],  # 左中
        [width * (1-_w_margin_ratio-_w_slide_ratio), height * (0.5-0.5*_h_slide_ratio),
         width * (1-_w_margin_ratio), height * (0.5+0.5*_h_slide_ratio)],  # 右中
        [width * (_w_margin_ratio), height * (1-_h_margin_ratio-_h_slide_ratio),
         width * (_w_slide_ratio+_w_space_ratio), height * (1-_h_margin_ratio)],  # 左下
        [width * (1-_w_margin_ratio-_w_slide_ratio), height * (1-_h_margin_ratio-_h_slide_ratio),
         width * (1-_w_margin_ratio), height * (1-_h_margin_ratio)]   # 右下
    ]
    return slide_crop_boxes

def slide_3_1(width, height):
    _w_margin_ratio = 0.08
    _h_margin_ratio = 0.14# 0.13
    _w_slide_ratio = 0.40# 0.42
    _h_slide_ratio = 0.205
    slide_crop_boxes = [
        [width * (_w_margin_ratio), height * (_h_margin_ratio),
         width * (_w_slide_ratio+_w_margin_ratio), height * (_h_slide_ratio+_h_margin_ratio)],  # 左上
        [width * (_w_margin_ratio), height * (0.5-0.5*_h_slide_ratio),
         width * (_w_slide_ratio+_w_margin_ratio), height * (0.5+0.5*_h_slide_ratio)],  # 左中
        [width * (_w_margin_ratio), height * (1-_h_margin_ratio-_h_slide_ratio),
         width * (_w_slide_ratio+_w_margin_ratio), height * (1-_h_margin_ratio)],  # 左下
    ]
    return slide_crop_boxes

def slide_2_2(width, height):
    _w_margin_ratio = 0.10
    _h_margin_ratio = 0.10
    _w_space_ratio = 0.10
    _h_space_ratio = 0.06
    slide_crop_boxes = [
        [width * (_w_margin_ratio), height * (_h_margin_ratio),
         width * (0.5-0.5*_w_space_ratio), height * (0.5-0.5*_h_space_ratio)],  # 左上
        [width * (0.5+0.5*_w_space_ratio), height * (_h_margin_ratio),
         width * (1-_w_space_ratio), height * (0.5-0.5*_h_space_ratio)],  # 右上
        [width * (_w_margin_ratio), height * (0.5+0.5*_h_space_ratio),
         width * (0.5-0.5*_w_space_ratio), height * (1-_h_margin_ratio)],  # 左下
        [width * (0.5+0.5*_w_space_ratio), height * (0.5+0.5*_h_space_ratio),
         width * (1-_w_space_ratio), height * (1-_h_margin_ratio)]   # 右下
    ]
    return slide_crop_boxes

def slide_2_1(width, height):
    _w_margin_ratio = 0.08
    _h_margin_ratio = 0.08
    # _w_space_ratio = 0.08
    _h_space_ratio = 0.08
    slide_crop_boxes = [
        [width * (_w_margin_ratio), height * (_h_margin_ratio),
         width * (1-_w_margin_ratio), height * (0.5-0.5*_h_space_ratio)],  # 上
        [width * (_w_margin_ratio), height * (0.5+0.5*_h_space_ratio),
         width * (1-_w_margin_ratio), height * (1-_h_margin_ratio)],  # 下
    ]
    return slide_crop_boxes

def crop_box_coord(crop_type, width = _a4_page_width, height = _a4_page_height):
    crop_box = []
    if crop_type == "a":
        slide_coord = slide_3_2(width, height)
    elif crop_type == "b":
        slide_coord = slide_2_2(width, height)
    elif crop_type == "c":
        slide_coord = slide_2_1(width, height)
    elif crop_type == "d":
        slide_coord = slide_3_1(width, height)
    else:
        print("Invalid input. Please enter numeric values.")

    for slide in slide_coord:
        crop_box.append(fitz.Rect(slide))

    return crop_box

def main():
    if len(sys.argv) != 2:
        print("Usage: python SlideSplit.py <input_pdf>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = "split-" + input_pdf

    # 打开PDF文件
    input_doc = fitz.open(input_pdf)

    # 创建一个新的PDF文档来保存裁切后的幻灯片
    output_doc = fitz.open()

    page_size = measure_pdf(input_doc)

    print("Please select Slide layouts ():")
    print("a. 6 Slides (3 rows 2 columns)")
    print("b. 4 Slides (2 rows 2 columns)")
    print("c. 2 Slides (2 rows 1 columns)")
    print("d. 3 Slides (3 rows 1 columns)")
    try:
        crop_type = input("Slides Layout:\n")
        # crop_width = float(input("Width: "))
        # crop_height = float(input("Height: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)

    # 生成裁剪框列表
    slide_boxes = crop_box_coord(crop_type, page_size[0], page_size[1])

    for singlepage in input_doc:
        r = singlepage.rect  # input page rectangle
        d = fitz.Rect(singlepage.cropbox_position,  # CropBox displacement if not
                  singlepage.cropbox_position)  # starting at (0, 0)
        # 遍历每页的裁切框
        for rx in slide_boxes:
            rx += d  # add the CropBox displacement
            page = output_doc.new_page(-1,  # new output page with rx dimensions
                            width = rx.width,
                            height = rx.height)
            page.show_pdf_page(
                page.rect,  # fill all new page with the image
                input_doc,  # input document
                singlepage.number,  # input page number
                clip = rx,  # which part to use of input page
            )

    # 保存裁切后的PDF文件
    output_doc.save(output_pdf,
                    garbage=3,  # eliminate duplicate objects
                    deflate=True,  # compress stuff where possible
                    )
    output_doc.close()
    input_doc.close()

    # 裁剪边框
    # crop(["-p 0", "-s", "-u", "--replaceOriginal", output_pdf])
    crop(["-p 0", "-s", "--replaceOriginal", output_pdf])
    print(f"PDF cropped and saved as {output_pdf}")

if __name__ == "__main__":
    main()
