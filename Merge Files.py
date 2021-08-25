# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:23:23 2021

@author: ashwi
"""

from PyPDF2 import PdfFileMerger

pdfs = ['2.pdf','3.pdf','4.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()