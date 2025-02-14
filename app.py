import PyPDF2
import os

# Lectura de archivos dentro de la carpeta ``pdfs``
def only_pdf_files(files):
    return [f for f in files if f.endswith(".pdf")]
def read_dir(dir_path):
    files = os.listdir(dir_path)
    return only_pdf_files(files)

# Lectura de un archivo PDF
def read_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    return pdf_file_obj

def read_page(pdf_file_obj, page_number):
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    return pdf_reader.pages[page_number].extract_text()

def get_abstract(page_info):
    if "A B S T R A C T" in page_info: ABSTRACT = "A B S T R A C T"
    else: ABSTRACT = "ABSTRACT"
    if "1.INTRODUCTION" in page_info: FIN = "1.INTRODUCTION"
    elif "I. INTRODUCTION" in page_info: FIN = "I. INTRODUCTION"
    elif "1. INTRODUCTION" in page_info: FIN = "1. INTRODUCTION"
    elif "*CORRESPONDING" in page_info: FIN = "*CORRESPONDING"
    else: FIN = "INTRODUCTION"
    return page_info[page_info.find(ABSTRACT):page_info.find(FIN)]

def get_title(page_info):
    return page_info.splitlines()[1]

# Logica principal
def main():
    for i in read_dir("pdfs"):
        print(i)
        file_path = f"pdfs/{i}"
        pdf_file_obj = read_pdf(file_path)
        
        page_info = read_page(pdf_file_obj, 0)
        page_info = page_info.upper()
        print("TITLE")
        print(get_title(page_info))
        print("")
        print(get_abstract(page_info))
    
    pdf_file_obj.close()

def test_main():
    
       
    file_path = f"pdfs/sexto.pdf"
    pdf_file_obj = read_pdf(file_path)
    page_info = read_page(pdf_file_obj, 0)
    page_info = page_info.upper()
    print(get_abstract(page_info))
    #print("\n".join(page_info.splitlines()))
    pdf_file_obj.close()

if __name__ == "__main__":
    test_main()