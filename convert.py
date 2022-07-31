#   This python function will thumbnail the first pdf page into an image of 300 by 450 
#
#   ensure to create a virtualenv and install requirements.py as shown in the below installation script
#   Please Run Command as will show below
#
#   virutalenv env && source env/bin/activate && pip install -r requirements.py
#   create_thumbnail_to_pdf(Full_path_of_File, Full_Path_of_Direcotry_to_be_Saved, FileName_in_qutes)
#
#   https://github.com/jaborsm/
#   July 2022
#

import os 
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader
from PyPDF2.errors import PyPdfError


def create_thumbnail_to_pdf(pdf_file_url, save_dir, filename):
    try:
       PdfFileReader(open(pdf_file_url, "rb"))
       images = convert_from_path(pdf_file_url, size=(300,450), )
       images[0].save(save_dir + filename +'.jpg', 'JPEG')
    except PyPdfError:
       print("invalid PDF file or File not found")
    except UnicodeDecodeError:
            print("invalid PDF file or File not found")
    else:
       print("Encountered an Error While Proccessing")


#project_dir = os.getcwd()
#create_thumbnail_to_pdf(project_dir + "/example_pdfs/sample.pdf", project_dir+'/thumbnails/', 'Test')
