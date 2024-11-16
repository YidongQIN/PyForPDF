# PyPDF2 Gist
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
# 0. Set Up Dir
# pip install PyPDF2
# workdir = "c:/Users/yqin78/Downloads"
# 1. PDF Reader
# input1 = open("{}/.pdf".format(workdir), "rb")  # Need PDF file name
# reader1 = PdfFileReader(input1)
# reader1.getNumPages()
# reader1.getPage(0)
# reader1.getPage(1).rotateClockwise(90)
# 2. PDF Merge
# merger = PdfFileMerger()
# merger.merge(position=0, fileobj=input1, pages=(2, 6))
# merger.append(input1)
# with open("{}/merged.pdf".format(workdir), "wb") as merged:
#     merger.write(merged)
# 3. PDF Writer
# writer1 = PdfFileWriter()
# writer1.addPage(reader1.getPage(1))  # Need Page Number, first page is 0.
# writer1.addBlankPage()
# with open("{}/output.pdf".format(workdir), "wb") as output:
#     writer1.write(output)


def removePage(pdfpath, *pagenum):
    reader = PdfFileReader(open(pdfpath, "rb"))
    writer = PdfFileWriter()
    for i in range(0, reader.getNumPages()):
        if i+1 not in pagenum:
            writer.addPage(reader.getPage(i))
    with open("{}_removed.pdf".format(pdfpath[:-4]), "wb") as output:
        writer.write(output)


def rotatePage(pdfpath, *pagenum):
    reader = PdfFileReader(open(pdfpath, "rb"))
    writer = PdfFileWriter()
    for i in range(0, reader.getNumPages()):
        if i+1 in pagenum:
            writer.addPage(reader.getPage(i).rotateClockwise(90))
        else:
            writer.addPage(reader.getPage(i))
    with open("{}_rotated.pdf".format(pdfpath[:-4]), "wb") as output:
        writer.write(output)


def combinePDF(*pdffile):
    writer = PdfFileWriter()
    for pdf in pdffile:
        reader = PdfFileReader(open(pdf, "rb"))
        for i in range(0, reader.getNumPages()):
            writer.addPage(reader.getPage(i))
    with open(("combined.pdf"), "wb") as output:
        writer.write(output)


target = "c:\\Users\\yqin78\\Downloads\\1.pdf"
# removePage(target, 1)
# rotatePage(target, 1)
# folder = "c:\\Users\\yqin78\\Downloads"
# filenames = ["01.pdf", "02.pdf", "03.pdf"]
# targets = ["{}\\{}".format(folder, name) for name in filenames]
# print(targets)
# combinePDF(*targets)
