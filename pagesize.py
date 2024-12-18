import sys
import pymupdf

def pagesize(input_pdf):
    # 打开PDF文件
    pdf = pymupdf.open(input_pdf)
    # 获取指定页面
    page = pdf[0]
    # 获取页面尺寸
    page_rect = page.rect
    print(f"Page dimensions:\n {page_rect.width} x {page_rect.height} points")

    return page_rect.width, page_rect.height

def main():
    if len(sys.argv) != 2:
        print("Usage: python SlideSplit.py <input_pdf>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    pagesize(input_pdf)

if __name__ == "__main__":
    main()
