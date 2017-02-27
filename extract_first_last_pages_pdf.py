#!/usr/bin/python

import sys
import argparse
from PyPDF2 import PdfFileWriter, PdfFileReader
import os.path

def main():
    
    parser = argparse.ArgumentParser(description='Combine the first and last pages '\
            + 'of multiple PDFs in a single file.')
    parser.add_argument("dir", default='./', help="Directory containing "\
            + "the PDF files", metavar ="DIR")
    parser.add_argument("output", default="combined.pdf", help="Output file",
            metavar="OUTPUT")
    parser.add_argument("--list", nargs='+', metavar="FNAME", help="List with the PDF files in a particular order")

    args = parser.parse_args()

    indir = os.path.abspath(args.dir)

    outpdf = PdfFileWriter()

    if None == args.list:
        list = [x for x in os.listdir(indir) if ".pdf" == os.path.splitext(x)[1]]
    else:
        list = [ os.path.join(indir, x)  for x in args.list ]

    for fname in list:
        # pyPDF requires the input stream to be open at the time of writing
        f = open(fname, "rb")
        inpdf = PdfFileReader(f)
        outpdf.addPage(inpdf.getPage(0))
        if inpdf.getNumPages() > 1:
          outpdf.addPage(inpdf.getPage(inpdf.getNumPages()-1))

    with open(args.output, "wb") as outf:
        outpdf.write(outf)

if __name__ == "__main__":
    main()
