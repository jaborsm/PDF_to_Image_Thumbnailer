This python function will thumbnail the first pdf page into an image of 300 by 450 

Ensure to create a virtualenv and install requirements.py as shown in the below installation script
   
Please Run Command as will show below

   virutalenv env && source env/bin/activate && pip install -r requirements.py
   
   project_dir = os.getcwd()
   
   create_thumbnail_to_pdf(project_dir + "/example_pdfs/sample.pdf", project_dir+'/thumbnails/', 'Test')
   
July 2022
